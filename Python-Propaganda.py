# File: python_propaganda.py

import this
import time

def print_ascii_python():
    print(r"""
             ___       ___           ___           ___     
            /\__\     /\__\         /\  \         /\__\    
           /::|  |   /::|  |       /::\  \       /:/  /    
          /:|:|  |  /:|:|  |      /:/\:\  \     /:/__/     
         /:/|:|  |__/:/|:|  |__  /:/  \:\  \   /::\  \ ___ 
        /:/ |:| /\__\/ |:| /\__\/:/__/ \:\__\ /:/\:\  /\__\
        \/__|:|/:/  /  |:|/:/  / \:\  \ /:/  / \/__\:\/:/  /
            |:/:/  /   |:/:/  /   \:\  /:/  /       \::/  / 
            |::/  /    |::/  /     \:\/:/  /        /:/  /  
            /:/  /     /:/  /       \::/  /        /:/  /   
            \/__/      \/__/         \/__/         \/__/    
    """)
    time.sleep(1)
    print("🐍 Python: Simple, Readable, Powerful.\n")

def compare_languages():
    slogans = [
        "Why use semicolons when you can use indentation?",
        "Forget curly braces — embrace whitespace!",
        "Dynamic typing? Yes please!",
        "One import to rule them all: `import this`",
        "Python — the pseudocode that actually runs.",
        "Indentation is not a bug. It's a feature.",
    ]
    for slogan in slogans:
        print(f"📢 {slogan}")
        time.sleep(1)

def show_power():
    print("\n💪 Python Powers:")
    powers = [
        "🔬 Science (NumPy, SciPy)",
        "📊 Data (Pandas, Matplotlib)",
        "🤖 AI (TensorFlow, PyTorch)",
        "🌐 Web (Django, Flask)",
        "🐧 OS Scripts (Cross-platform magic)",
        "📱 Apps (Kivy, BeeWare)",
        "💾 Automation (Everything!)"
    ]
    for power in powers:
        print(power)
        time.sleep(0.7)

def call_to_action():
    print("\n🚀 Join the movement.")
    time.sleep(1)
    print("Write Python. Readable code is revolutionary.")
    print("From zero to hero, Python welcomes all.\n")
    time.sleep(1)
    print(">>> import antigravity  # Experience lift-off\n")

if __name__ == "__main__":
    print_ascii_python()
    compare_languages()
    show_power()
    call_to_action()
