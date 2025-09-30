def get_student_scores():
    scores = []
    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(1, num_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter score for subject {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return scores

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def main():
    print("=== Student Results Calculator ===")
    student_name = input("Enter student's name: ")
    num_terms = int(input("Enter number of terms: "))
    all_term_averages = []
    for term in range(1, num_terms + 1):
        print(f"\n--- Term {term} ---")
        scores = get_student_scores()
        avg = calculate_average(scores)
        all_term_averages.append(avg)
        print(f"Average for Term {term}: {avg:.2f}")

    overall_average = calculate_average(all_term_averages)
    print(f"\n{student_name}'s average per term:")
    for idx, avg in enumerate(all_term_averages, 1):
        print(f"  Term {idx}: {avg:.2f}")
    print(f"\nOverall average across {num_terms} terms: {overall_average:.2f}")

if __name__ == "__main__":
    main()


    # To create a .env file for storing your Postgres database credentials, you can use the following code:
    env_content = (
        "DB_HOST=localhost\n"
        "DB_PORT=5432\n"
        "DB_NAME=service\n"
        "DB_USER=postgres\n"
        "DB_PASSWORD=1100211Matt.\n"
    )

    with open('.env', 'w') as env_file:
        env_file.write(env_content)

    print(".env file created with Postgres database credentials. Please update the values as needed.")



    # INSERT_YOUR_CODE
    # Example usage of the Profile class from profile.py

    # Import Profile class (assuming profile.py is in the same directory or in the Python path)
    # from profile import Profile

    # For demonstration, let's create a new profile for a student
    student_profile = {
        "name": student_name,
        "favorite_language": "Python",
        "hobby": "Reading",
        "tech_stack": ["Python", "Pandas", "Jupyter Notebook"],
        "github_username": "student-github",
        "fun_fact": "Loves solving puzzles!"
    }

    # Since we can't import Profile here, let's just show how it would be used:
    # profile = Profile(**student_profile)
    # profile.introduce()
    # profile.show_stack()
    # print(f"GitHub: {profile.github_link()}")
    # print(f"Fun Fact: {profile.fun_fact}")

    print("\n--- Student Profile Example ---")
    print(f"Name: {student_profile['name']}")
    print(f"Favorite Language: {student_profile['favorite_language']}")
    print(f"Hobby: {student_profile['hobby']}")
    print("Tech Stack:")
    for i, tech in enumerate(student_profile['tech_stack'], 1):
        print(f"  {i}. {tech}")
    print(f"GitHub: https://github.com/{student_profile['github_username']}")
    print(f"Fun Fact: {student_profile['fun_fact']}")
    # INSERT_YOUR_CODE

    # Fix for NameError: name 'student_name' is not defined
    # If student_name is not already defined above, prompt the user for it here.
    try:
        student_name
    except NameError:
        student_name = input("Enter student's name for profile: ")
        # INSERT_YOUR_CODE

        # Simple HTML and CSS frontend for the student profile
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Student Profile</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .profile-container {{
                    background: #fff;
                    max-width: 400px;
                    margin: 40px auto;
                    padding: 30px 40px;
                    border-radius: 10px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                h2 {{
                    color: #333;
                    margin-top: 0;
                }}
                .tech-stack {{
                    list-style: decimal inside;
                    padding-left: 0;
                }}
                .label {{
                    font-weight: bold;
                    color: #555;
                }}
                .github-link {{
                    color: #0366d6;
                    text-decoration: none;
                }}
                .fun-fact {{
                    background: #e7f3fe;
                    padding: 10px;
                    border-radius: 5px;
                    margin-top: 15px;
                    color: #1a4b7a;
                }}
            </style>
        </head>
        <body>
            <div class="profile-container">
                <h2>{student_profile['name']}</h2>
                <p><span class="label">Favorite Language:</span> {student_profile['favorite_language']}</p>
                <p><span class="label">Hobby:</span> {student_profile['hobby']}</p>
                <p><span class="label">Tech Stack:</span></p>
                <ol class="tech-stack">
                    {''.join(f'<li>{tech}</li>' for tech in student_profile['tech_stack'])}
                </ol>
                <p><span class="label">GitHub:</span> <a class="github-link" href="https://github.com/{student_profile['github_username']}" target="_blank">{student_profile['github_username']}</a></p>
                <div class="fun-fact">
                    <span class="label">Fun Fact:</span> {student_profile['fun_fact']}
                </div>
            </div>
        </body>
        </html>
        """

        # Save the HTML to a file
        with open("student_profile.html", "w", encoding="utf-8") as f:
            f.write(html_template)

        print("\nstudent_profile.html has been created. Open it in your browser to view the student profile frontend.")
