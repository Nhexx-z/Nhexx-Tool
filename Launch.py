import time
import os
import shutil
import getpass
import sys

# ===== CONFIG =====
secret_code = "nhexx"

COLOR = "\033[0m"     # Blanc par défaut
RESET = "\033[0m"

COLORS = {
    "1": ("\033[92m", "Vert"),
    "2": ("\033[91m", "Rouge"),
    "3": ("\033[94m", "Bleu"),
    "4": ("\033[95m", "Violet"),
    "5": ("\033[0m",  "Blanc")
}

# ===== TERMINAL UTILS =====
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def step(text, delay=0.6):
    print(COLOR + f"{text} ..." + RESET, end="", flush=True)
    time.sleep(delay)
    print("\r" + COLOR + f"{text} [enable]" + RESET)

def color_input(prompt=""):
    print(COLOR, end="")
    value = input(prompt)
    print(RESET, end="")
    return value

def masked_input(prompt=""):
    print(COLOR, end="")
    value = getpass.getpass(prompt)
    print(RESET, end="")
    return value

def pause():
    color_input("\nAppuyez sur Entrée pour revenir au menu...")

# ===== DISPLAY =====
def show_logo():
    cols = shutil.get_terminal_size().columns
    logo = [
        " ███╗   ██╗██╗  ██╗███████╗ ██╗  ██╗ ██╗  ██╗",
        " ████╗  ██║██║  ██║██╔════╝ ╚██╗██╔╝ ╚██╗██╔╝",
        " ██╔██╗ ██║███████║█████╗   ╚███╔╝   ╚███╔╝ ",
        " ██║╚██╗██║██╔══██║██╔══╝   ██╔██╗   ██╔██╗ ",
        " ██║ ╚████║██║  ██║███████╗██╔╝ ██╗ ██╔╝ ██╗",
        " ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═╝  ╚═╝",
        "",
        "             N H E X X   T O O L",
    ]
    for line in logo:
        print(COLOR + line.center(cols) + RESET)

def show_menu():
    print(COLOR + "\n[1] Modules" + RESET)
    print(COLOR + "[2] Scan" + RESET)
    print(COLOR + "[3] Settings" + RESET)
    print(COLOR + "[4] Exit" + RESET)

# ===== PAGES =====
def modules():
    clear()
    print(COLOR + "=== MODULES ===" + RESET)
    print(COLOR + "- Module réseau" + RESET)
    print(COLOR + "- Module système" + RESET)
    print(COLOR + "- Module analyse" + RESET)
    pause()

def scan():
    clear()
    print(COLOR + "=== SCAN ===" + RESET)
    step("Scan des ports", 0.5)
    step("Analyse réseau", 0.5)
    step("Collecte des données", 0.5)
    print(COLOR + "\nScan terminé [enable]" + RESET)
    pause()

def settings():
    global COLOR
    while True:
        clear()
        print(COLOR + "=== SETTINGS ===\n" + RESET)
        print(COLOR + "Changer la couleur du tool :\n" + RESET)

        for k, v in COLORS.items():
            print(COLOR + f"[{k}] {v[1]}" + RESET)

        print(COLOR + "[0] Retour" + RESET)

        choice = color_input("\n> ")

        if choice in COLORS:
            COLOR = COLORS[choice][0]
            print(COLOR + "\nCouleur appliquée [enable]" + RESET)
            time.sleep(0.8)
        elif choice == "0":
            break
        else:
            print(COLOR + "Choix invalide ❌" + RESET)
            time.sleep(0.8)

# ===== MAIN =====
hide_cursor()

try:
    code = masked_input("Entrez votre code unique pour accéder au tool : ")

    if code == secret_code:
        print()
        step("Chargement")
        step("Initialisation")
        step("Vérification des permissions")
        step("Connexion aux services")

        time.sleep(0.6)

        while True:
            clear()
            show_logo()
            show_menu()
            choice = color_input("\n> ")

            if choice == "1":
                modules()
            elif choice == "2":
                scan()
            elif choice == "3":
                settings()
            elif choice == "4":
                print(COLOR + "Fermeture du tool..." + RESET)
                time.sleep(1)
                break
            else:
                print(COLOR + "Choix invalide ❌" + RESET)
                time.sleep(1)
    else:
        print("\nAccès refusé ❌")

finally:
    show_cursor()
