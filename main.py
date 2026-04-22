def analyze_code(code):
    code = code.lower()
    lines = code.split("\n")
    errors = []

    for i, line in enumerate(lines):
        line = line.strip()

        # Skip empty lines and comments
        if line == "" or line.startswith("#"):
            continue

        # 🔴 Rule 1: Missing ':' in for loop
        if line.startswith("for") and ":" not in line:
            errors.append({
                "line": i + 1,
                "error": "Syntax Error",
                "explanation": "A 'for' loop requires ':' at the end.",
                "fix": "Add ':' at the end of the for loop line."
            })

        # 🔴 Rule 2: Missing ':' in if
        if line.startswith("if") and ":" not in line:
            errors.append({
                "line": i + 1,
                "error": "Syntax Error",
                "explanation": "An 'if' statement requires ':' at the end.",
                "fix": "Add ':' at the end of the if condition."
            })

        # 🟡 Rule 3: Assignment vs comparison (only in if)
        if line.startswith("if") and "=" in line and "==" not in line:
            errors.append({
                "line": i + 1,
                "error": "Logic Error",
                "explanation": "You might be using '=' instead of '==' in a condition.",
                "fix": "Use '==' for comparison."
            })

        # 🟣 Rule 4: Print syntax
        if line.startswith("print") and ("(" not in line or ")" not in line):
            errors.append({
                "line": i + 1,
                "error": "Syntax Error",
                "explanation": "Print function requires parentheses in Python.",
                "fix": "Use print('text') format."
            })

        # 🔵 Rule 5: Indentation check
        if line.endswith(":"):
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if not (next_line.startswith(" ") or next_line.startswith("\t")):
                    errors.append({
                        "line": i + 2,
                        "error": "Indentation Error",
                        "explanation": "Expected an indented block after ':'.",
                        "fix": "Indent the next line."
                    })

    return errors


# 🧾 Function to read multi-line input
def get_user_code():
    print("Paste your code (type END to finish):")
    lines = []

    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)

    return "\n".join(lines)


# 🖥️ Function to display results
def display_results(errors):
    print("\n🔍 Adronix V3 Analysis:")

    if not errors:
        print("✅ No obvious errors found")
    else:
        for i, err in enumerate(errors, 1):
            print(f"\n{i}. Line {err['line']}")
            print("Error:", err["error"])
            print("Explanation:", err["explanation"])
            print("Fix:", err["fix"])


# 🚀 Main program
def main():
    user_code = get_user_code()
    result = analyze_code(user_code)
    display_results(result)


# ▶️ Run program
if __name__ == "__main__":
    main()