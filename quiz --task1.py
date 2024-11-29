import random

# Questions and answers for each category
QUIZ_DATA = {
    "Python": [
        {"question": "What is the correct file extension for Python files?", 
         "options": [".py", ".python", ".pt", ".p"], 
         "answer": ".py", 
         "explanation": "Python files use the `.py` extension."},
        {"question": "Which keyword is used to define a function in Python?", 
         "options": ["function", "def", "fun", "lambda"], 
         "answer": "def", 
         "explanation": "The `def` keyword is used to define a function in Python."},
        {"question": "How do you insert comments in Python code?", 
         "options": ["/* comment */", "// comment", "# comment", "<!-- comment -->"], 
         "answer": "# comment", 
         "explanation": "Comments in Python are created using the `#` symbol."},
        {"question": "Which data type is immutable in Python?", 
         "options": ["List", "Set", "Dictionary", "Tuple"], 
         "answer": "Tuple", 
         "explanation": "Tuples are immutable in Python, meaning their values cannot be changed."},
    {
        "question": "What is the correct way to create a dictionary in Python?",
        "options": ["{}", "[]", "()", "None of the above"],
        "answer": "{}",
        "explanation": "Dictionaries are created using curly braces `{}` in Python."
    },
    {
        "question": "Which Python module is used to generate random numbers?",
        "options": ["math", "random", "numbers", "os"],
        "answer": "random",
        "explanation": "The `random` module in Python is used to generate random numbers."
    },
    {
        "question": "How do you create a variable with the floating-point value 3.14?",
        "options": ["x = 3.14", "x = float(3.14)", "Both of the above", "None of the above"],
        "answer": "Both of the above",
        "explanation": "You can create a floating-point variable using either `x = 3.14` or `x = float(3.14)`."
    },
    {
        "question": "What does the `append()` method do in Python?",
        "options": ["Adds an item to the end of a list", "Removes an item from a list", "Replaces an item in a list", "Sorts a list"],
        "answer": "Adds an item to the end of a list",
        "explanation": "The `append()` method adds an item to the end of a list."
    },
    {
        "question": "What is the output of `print(type('hello'))`?",
        "options": ["<class 'string'>", "<class 'str'>", "<type 'string'>", "None of the above"],
        "answer": "<class 'str'>",
        "explanation": "The type of a string literal in Python is `<class 'str'>`."
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["int", "float", "double", "str"],
        "answer": "double",
        "explanation": "Python does not have a `double` data type; `float` is used for decimal values."
    },
    {
        "question": "Which keyword is used for error handling in Python?",
        "options": ["try", "catch", "handle", "except"],
        "answer": "try",
        "explanation": "The `try` keyword is used to define a block of code to test for errors in Python."
    },
    {
        "question": "What is the purpose of the `is` operator in Python?",
        "options": ["Check equality", "Check object identity", "Check membership", "None of the above"],
        "answer": "Check object identity",
        "explanation": "The `is` operator checks if two variables refer to the same object in memory."
    },
    {
        "question": "Which built-in function is used to get the length of a list in Python?",
        "options": ["length()", "len()", "size()", "count()"],
        "answer": "len()",
        "explanation": "The `len()` function is used to get the length of a list in Python."
    },
    {
        "question": "What is the correct way to create a dictionary in Python?",
        "options": ["{}", "[]", "()", "None of the above"],
        "answer": "{}",
        "explanation": "Dictionaries are created using curly braces `{}` in Python."
    },
    {
        "question": "Which Python module is used to generate random numbers?",
        "options": ["math", "random", "numbers", "os"],
        "answer": "random",
        "explanation": "The `random` module in Python is used to generate random numbers."
    },
    {
        "question": "How do you create a variable with the floating-point value 3.14?",
        "options": ["x = 3.14", "x = float(3.14)", "Both of the above", "None of the above"],
        "answer": "Both of the above",
        "explanation": "You can create a floating-point variable using either `x = 3.14` or `x = float(3.14)`."
    },
    {
        "question": "What does the `append()` method do in Python?",
        "options": ["Adds an item to the end of a list", "Removes an item from a list", "Replaces an item in a list", "Sorts a list"],
        "answer": "Adds an item to the end of a list",
        "explanation": "The `append()` method adds an item to the end of a list."
    },
    {
        "question": "What is the output of `print(type('hello'))`?",
        "options": ["<class 'string'>", "<class 'str'>", "<type 'string'>", "None of the above"],
        "answer": "<class 'str'>",
        "explanation": "The type of a string literal in Python is `<class 'str'>`."
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["int", "float", "double", "str"],
        "answer": "double",
        "explanation": "Python does not have a `double` data type; `float` is used for decimal values."
    },
    {
        "question": "Which keyword is used for error handling in Python?",
        "options": ["try", "catch", "handle", "except"],
        "answer": "try",
        "explanation": "The `try` keyword is used to define a block of code to test for errors in Python."
    },
    {
        "question": "What is the purpose of the `is` operator in Python?",
        "options": ["Check equality", "Check object identity", "Check membership", "None of the above"],
        "answer": "Check object identity",
        "explanation": "The `is` operator checks if two variables refer to the same object in memory."
    },
    {
        "question": "What will be the output of `print(bool(0))`?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False",
        "explanation": "In Python, `0` is considered `False` when converted to a boolean."
    }
    ],
    "Java": [
        {"question": "What is the correct way to declare a variable in Java?", 
         "options": ["var x = 10;", "int x = 10;", "x = 10;", "dim x = 10;"], 
         "answer": "int x = 10;", 
         "explanation": "In Java, variables must be declared with a data type, such as `int`."},
        {"question": "Which keyword is used to create a subclass in Java?", 
         "options": ["inherits", "extends", "implements", "derives"], 
         "answer": "extends", 
         "explanation": "The `extends` keyword is used in Java to inherit from a superclass."},
        {"question": "Which method is the entry point for a Java application?", 
         "options": ["start()", "main()", "init()", "run()"], 
         "answer": "main()", 
         "explanation": "Every Java application starts execution from the `main()` method."},
        {"question": "What is the size of an `int` in Java?", 
         "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on the platform"], 
         "answer": "4 bytes", 
         "explanation": "In Java, an `int` is always 4 bytes, regardless of the platform."},
        {"question": "Which package contains the `Scanner` class in Java?", 
         "options": ["java.io", "java.net", "java.util", "java.lang"], 
         "answer": "java.util", 
         "explanation": "The `Scanner` class is part of the `java.util` package."},
        {
        "question": "Which keyword is used to define a constant in Java?",
        "options": ["final", "const", "static", "constant"],
        "answer": "final",
        "explanation": "In Java, the `final` keyword is used to declare constants."
    },
    {
        "question": "What is the purpose of the `super` keyword in Java?",
        "options": ["Access methods of a subclass", "Access methods of a superclass", "Define a superclass", "Define a subclass"],
        "answer": "Access methods of a superclass",
        "explanation": "The `super` keyword is used to access methods and constructors of the superclass."
    },
    {
        "question": "What is the default value of a boolean in Java?",
        "options": ["true", "false", "null", "0"],
        "answer": "false",
        "explanation": "The default value of a boolean in Java is `false`."
    },
    {
        "question": "Which operator is used to compare two values in Java?",
        "options": ["=", "==", "===", "!="],
        "answer": "==",
        "explanation": "The `==` operator is used to compare two values for equality in Java."
    },
    {
        "question": "Which keyword is used to define an interface in Java?",
        "options": ["class", "interface", "implements", "extends"],
        "answer": "interface",
        "explanation": "The `interface` keyword is used to define an interface in Java."
    },
    {
        "question": "What is the size of a `double` in Java?",
        "options": ["4 bytes", "8 bytes", "16 bytes", "Platform dependent"],
        "answer": "8 bytes",
        "explanation": "A `double` in Java is always 8 bytes, regardless of the platform."
    },
    {
        "question": "What is the output of `System.out.println(10 / 3);`?",
        "options": ["3.33", "3", "Error", "None of the above"],
        "answer": "3",
        "explanation": "In Java, integer division truncates the result, so 10 / 3 is 3."
    },
    {
        "question": "Which of the following is not a valid access modifier in Java?",
        "options": ["private", "protected", "public", "internal"],
        "answer": "internal",
        "explanation": "Java does not have an `internal` access modifier; it is used in C#."
    },
    {
        "question": "Which method is used to compare two strings in Java?",
        "options": ["==", "compareTo()", "equals()", "compare()"],
        "answer": "equals()",
        "explanation": "The `equals()` method is used to compare the content of two strings in Java."
    },
    {
        "question": "What is the purpose of the `finally` block in Java?",
        "options": ["Handle exceptions", "Execute code after `try-catch`", "Exit the program", "None of the above"],
        "answer": "Execute code after `try-catch`",
        "explanation": "The `finally` block is used to execute code after `try-catch`, regardless of whether an exception was thrown."
    }
    ],
    "C++": [
        {"question": "Which operator is used to access members of a class in C++?", 
         "options": [".", "->", "::", "&"], 
         "answer": ".", 
         "explanation": "The `.` operator is used to access class members in C++."},
        {"question": "Which header file is required to use `cout`?", 
         "options": ["<iostream>", "<stdio.h>", "<stdlib.h>", "<conio.h>"], 
         "answer": "<iostream>", 
         "explanation": "`cout` is defined in the `<iostream>` header file."},
        {"question": "What is the size of a `char` in C++?", 
         "options": ["1 byte", "2 bytes", "4 bytes", "Depends on the platform"], 
         "answer": "1 byte", 
         "explanation": "In C++, a `char` is always 1 byte."},
        {"question": "Which keyword is used to declare a constant in C++?", 
         "options": ["const", "final", "static", "define"], 
         "answer": "const", 
         "explanation": "The `const` keyword is used to declare constants in C++."},
        {"question": "What is the output of `cout << 5 / 2;`?", 
         "options": ["2.5", "2", "5.2", "Error"], 
         "answer": "2", 
         "explanation": "In C++, integer division truncates the result, so 5/2 is 2."},
        {
        "question": "Which type of inheritance is used in the following syntax: `class B : public A`?",
        "options": ["Private", "Public", "Protected", "Hybrid"],
        "answer": "Public",
        "explanation": "The `public` keyword indicates public inheritance in C++."
    },
    {
        "question": "What does the `this` pointer point to in C++?",
        "options": ["The current object", "The base class", "The next object", "The previous object"],
        "answer": "The current object",
        "explanation": "The `this` pointer in C++ points to the current instance of the class."
    },
     {
        "question": "Which loop is guaranteed to execute at least once in C++?",
        "options": ["for", "while", "do-while", "None of the above"],
        "answer": "do-while",
        "explanation": "The `do-while` loop executes the body first and then checks the condition, ensuring at least one iteration."
    },
    {
        "question": "What is the default access specifier for class members in C++?",
        "options": ["private", "public", "protected", "None"],
        "answer": "private",
        "explanation": "By default, class members are private in C++."
    },
    {
        "question": "Which operator is overloaded for object assignment in C++?",
        "options": ["+", "=", "==", "->"],
        "answer": "=",
        "explanation": "The assignment operator (`=`) is overloaded for assigning one object to another in C++."
    },
    {
        "question": "Which function is used to allocate memory dynamically in C++?",
        "options": ["malloc", "new", "calloc", "alloc"],
        "answer": "new",
        "explanation": "The `new` keyword is used to allocate memory dynamically in C++."
    },
    {
        "question": "What is a pure virtual function in C++?",
        "options": ["A function with no implementation", "A function that returns void", "A function with `virtual` keyword", "A function that cannot be overridden"],
        "answer": "A function with no implementation",
        "explanation": "A pure virtual function is declared by assigning `= 0` in its declaration and has no implementation."
    },
    {
        "question": "Which keyword is used to handle exceptions in C++?",
        "options": ["try", "catch", "throw", "All of the above"],
        "answer": "All of the above",
        "explanation": "`try`, `catch`, and `throw` are used to handle exceptions in C++."
    },
    {
        "question": "What is the output of `cout << sizeof(int);` on most platforms?",
        "options": ["2", "4", "8", "Depends on the platform"],
        "answer": "4",
        "explanation": "On most platforms, the size of an `int` is 4 bytes."
    },
    {
        "question": "Which data structure uses LIFO (Last In, First Out)?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": "Stack",
        "explanation": "A stack operates on the principle of LIFO (Last In, First Out)."
    }        
    ]
}

# Function to run the quiz
def run_quiz(category):
    print(f"\nStarting {category} Quiz!")
    questions = random.sample(QUIZ_DATA[category], 5)
    score = 0

    for idx, question_data in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question_data['question']}")
        for i, option in enumerate(question_data["options"], 1):
            print(f"{i}. {option}")
        answer = input("Your answer (1-4): ").strip()
        
        if answer.isdigit() and 1 <= int(answer) <= 4:
            chosen_option = question_data["options"][int(answer) - 1]
            if chosen_option == question_data["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {question_data['answer']}")
            print(f"Explanation: {question_data['explanation']}")
        else:
            print("Invalid input. Skipping question.")

    print(f"\nQuiz Complete! You scored {score} out of 5.")
    if score < 3:
        print("Don't worry! Keep practicing to improve your skills.")

# Main function
def main():
    print("=== Programming Language Quiz ===")
    while True:
        print("\nSelect a category:")
        print("1. Python")
        print("2. Java")
        print("3. C++")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            run_quiz("Python")
        elif choice == "2":
            run_quiz("Java")
        elif choice == "3":
            run_quiz("C++")
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
