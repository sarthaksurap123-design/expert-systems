
rules = {
    "flu": ["fever", "cough", "fatigue"],
    "cold": ["cough", "fatigue"],
    "migraine": ["headache", "fever"]
}


def ask(symptom):
    answer = input(f"Do you have {symptom}? (yes/no): ").lower()
    return answer == "yes"


def prove(goal, visited):
    if goal in visited:
        return False
    visited.add(goal)

  
    if goal not in rules:
        return ask(goal)

   
    for subgoal in rules[goal]:
        if not prove(subgoal, visited):
            return False
    return True

def expert_system():
    print("=== Prolog-like Expert System ===\n")

    for disease in rules:
        if prove(disease, set()):
            print(f"\nDiagnosis: You may have {disease.upper()}")
            return

    print("\nNo disease detected.")

# Run
expert_system()