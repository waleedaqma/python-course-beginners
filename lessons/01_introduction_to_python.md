# Lesson 1: Introduction to Python and Setup

## 🎯 What You'll Learn
- What Python is and why it's popular
- How to install Python on your computer
- How to verify your installation
- Basic concepts about programming

## 🐍 What is Python?

Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. It's known for its:

- **Simple and readable syntax** - Python code looks almost like English!
- **Versatility** - Used for web development, data science, AI, automation, and more
- **Large community** - Tons of libraries and resources available
- **Cross-platform** - Works on Windows, Mac, and Linux

## 💻 Installing Python

### Step 1: Download Python
1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Choose the latest version (currently Python 3.12+)
4. Download the installer for your operating system

### Step 2: Install Python
**Windows:**
- Run the downloaded `.exe` file
- **Important**: Check "Add Python to PATH" during installation
- Click "Install Now"

**Mac:**
- Run the `.pkg` file
- Follow the installation wizard

**Linux:**
- Python usually comes pre-installed
- If not: `sudo apt-get install python3` (Ubuntu/Debian)

### Step 3: Verify Installation
Open your terminal/command prompt and type:

```bash
python --version
# or
python3 --version
```

You should see something like: `Python 3.12.0`

## 🔧 Setting Up Your Development Environment

### Option 1: IDLE (Python's Built-in Editor)
- Comes with Python installation
- Good for beginners
- Simple and lightweight

### Option 2: VS Code (Recommended)
1. Download [VS Code](https://code.visualstudio.com/)
2. Install the Python extension
3. Create a new folder for your Python projects
4. Open the folder in VS Code

### Option 3: PyCharm
- Professional Python IDE
- More features but heavier
- Good for larger projects

## 🚀 Your First Python Program

Let's write a simple "Hello, World!" program to test everything:

1. Open your chosen editor
2. Create a new file called `hello.py`
3. Type this code:

```python
print("Hello, World!")
print("Welcome to Python!")
print("I'm excited to learn programming!")
```

4. Save the file
5. Run it:
   - **Terminal**: Navigate to the file directory and type `python hello.py`
   - **VS Code**: Click the play button or press F5
   - **IDLE**: Press F5

## 📝 Understanding the Code

Let's break down what we just wrote:

- `print()` is a **function** - it tells Python to display something
- The text inside quotes `"..."` is called a **string** - it's just text
- Each line is a **statement** - a complete instruction for Python
- The `#` symbol creates **comments** - notes that Python ignores

## 🎯 Key Concepts

- **Program**: A set of instructions for the computer
- **Code**: The actual text we write in Python
- **Run/Execute**: To make the program work
- **Output**: What the program displays or produces

## ✅ Practice Exercise

Try these variations of the Hello World program:

1. **Personalized greeting**: Ask for the user's name and greet them
2. **Multiple lines**: Print your favorite programming quote
3. **Numbers**: Print your age and favorite number

## 🔍 Troubleshooting

**"Python is not recognized" error:**
- Python wasn't added to PATH during installation
- Reinstall Python and check "Add Python to PATH"

**"Permission denied" error:**
- Try running as administrator (Windows)
- Use `sudo` on Mac/Linux

## 📚 What's Next?

In the next lesson, we'll:
- Learn about variables and data types
- Write more interactive programs
- Understand how to store and manipulate information

## 💡 Pro Tips

- **Practice daily** - even 15 minutes helps!
- **Don't memorize** - focus on understanding concepts
- **Experiment** - change code and see what happens
- **Ask questions** - there are no stupid questions in programming!

---

**🎉 Congratulations!** You've completed your first Python lesson and written your first program. You're officially a programmer now!

**Next**: [Lesson 2: Your First Python Program](../lessons/02_first_program.md)
