def get_input(file_path):
    all_workflows = False
    workflows = []
    parts = []
    with open(file_path) as input:
        for line in input:
            line = line.strip()
            if line == "":
                all_workflows = True
                continue
            if not all_workflows:
                workflows.append(line)
            else:
                parts.append(line)
    return workflows, parts

def comparer(part_number: int, operator: str, rule_number):
    if operator == "<":
        return part_number < rule_number
    if operator == ">":
        return part_number > rule_number

def workflows_in_dict(workflows: list):
    dict_workflows = {}
    for workflow in workflows:
        key, rules = workflow.replace("}", "").split("{")
        dict_workflows[key] = {}
        rules = rules.split(",")
        for index, rule in enumerate(rules):
            try:
                rule, next_key = rule.split(":")
                if "<" in rule:
                    operator = "<"
                    letter, number = rule.split("<")
                    if letter not in dict_workflows[key]:
                        dict_workflows[key][index] = {}
                    dict_workflows[key][index][letter] = ({"operator": operator, "number": int(number), "next_key": next_key})
                if ">" in rule:
                    operator = ">"
                    letter, number = rule.split(">")
                    if letter not in dict_workflows[key]:
                        dict_workflows[key][index] = {}
                    dict_workflows[key][index][letter] = ({"operator": operator, "number": int(number), "next_key": next_key})
            except:
                next_key = rule
                dict_workflows[key]["next_key"] = next_key
    return dict_workflows

def parts_in_dict(parts: list):
    dict_parts = {}
    for i, part in enumerate(parts):
        part = part.replace("{","").replace("}","").split(",")
        dict_parts[i] = {}
        rating_sum = 0
        for p in part:
            rating_letter, rating_number = p.split("=")
            dict_parts[i][rating_letter] = int(rating_number)
            rating_sum += int(rating_number)
        dict_parts[i]["sum"] = rating_sum
    return dict_parts

def go_trough(dict_parts: dict, dict_workflows: dict):
    rating_sum = 0
    for part in dict_parts:
        key = "in"
        while key != "R" and key != "A":
            found_new_des = False
            for index in dict_workflows[key]:
                if index != "next_key":
                    for letter in dict_workflows[key][index]:
                        part_number = dict_parts[part][letter]
                        work_number = dict_workflows[key][index][letter]["number"]
                        operator = dict_workflows[key][index][letter]["operator"]
                        next_key = dict_workflows[key][index][letter]["next_key"]
                        if comparer(part_number, operator, work_number):
                            key = next_key
                            found_new_des = True
                            if key == "A":
                                rating_sum += dict_parts[part]["sum"]
                            break
                    if found_new_des:
                        break
                else:
                    key = dict_workflows[key]["next_key"]
                    if key == "A":
                        rating_sum += dict_parts[part]["sum"]
    return rating_sum

                




workflows, parts = get_input("day19/input.txt")
dict_workflows = workflows_in_dict(workflows)
dict_parts = parts_in_dict(parts)
rating_sum = go_trough(dict_parts, dict_workflows)

print(rating_sum)

