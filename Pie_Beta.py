import tkinter as tk
import sys
import time

# ==========================================
# PART 1: Console Loading Sequence with Timing
# ==========================================
print("---- Cookie clicker 3ds... for 3ds import ----")
time.sleep(1)
print("printing your game 10%")
time.sleep(0.5)
print("printing your game 20%")
time.sleep(0.5)
print("did you know, This is a demo made in thonny linux mint")
time.sleep(0.5)
print("Error 404 trying again")
time.sleep(0.3)
print("99.99%")
time.sleep(0.5)
print("Completed select demo buttons & Coin Shop loaded!")

# ==========================================
# PART 2: Game Variables
# ==========================================
score = 0
coins = 0
cookies_per_click = 1
coin_multiplier = 1
cheats_enabled = False

# ==========================================
# PART 3: Main Game Logic & Shop Functions
# ==========================================
def click_counter():
    global score, cookies_per_click, cheats_enabled
    if cheats_enabled:
        score = score + (cookies_per_click * 10)  # Troll 10x multiplier
    else:
        score = score + cookies_per_click
    update_main_display()

def update_main_display():
    counter_label.config(text=f"Cookies: {score} | 🪙 Coins: {coins}")

def buy_powerup():
    global score, cookies_per_click, cheats_enabled
    cost = 0 if cheats_enabled else 100
    if score >= cost:
        score = score - cost
        cookies_per_click = cookies_per_click + 1
        update_main_display()
        status_label.config(text=f"Success! 1-Up bought! Now getting +{cookies_per_click} per click! 🍄", fg="green")
    else:
        status_label.config(text=f"Not enough cookies! Need {cost}.", fg="red")

def buy_cheat_mode():
    global score, cheats_enabled
    cost = 0 if cheats_enabled else 200
    if score >= cost:
        score = score - cost
        cheats_enabled = True
        status_label.config(text="🧌 TROLL CHEAT MODE UNLOCKED! EVERYTHING IS FREE! 🧌", fg="purple")
        cheat_btn.config(text="🧌 CHEATS ACTIVE (FREE STUFF!)", state="disabled", bg="thistle")
        update_main_display()
    else:
        status_label.config(text="Need 200 cookies for Cheat Mode!", fg="red")

def buy_ban_hammer():
    global score, cheats_enabled
    cost = 0 if cheats_enabled else 1000000
    if score >= cost:
        score = score - cost
        window.config(bg="red")
        title_label.config(bg="red", fg="white")
        status_label.config(text="🔨 BAN HAMMER DEPLOYED! CRITICAL ERROR...", bg="red", fg="yellow", font=("Arial", 11, "bold"))
        counter_label.config(bg="red", fg="white")
        window.after(1500, crash_game)
    else:
        status_label.config(text="Need 1,000,000 cookies for the Ban Hammer!", fg="red")

def crash_game():
    window.destroy()
    print("CRITICAL ERROR 404: Ban Hammer activated. Game crashed successfully.")
    sys.exit()

def reset_game():
    global score, coins, cookies_per_click, coin_multiplier, cheats_enabled
    score = 0
    coins = 0
    cookies_per_click = 1
    coin_multiplier = 1
    cheats_enabled = False
    update_main_display()
    status_label.config(text="Game reset.", fg="blue")
    cheat_btn.config(text="🧌 Buy Cheat Mode - Cost: 200", state="normal", bg="plum")


# ==========================================
# PART 4: Coin Shop Popup Window
# ==========================================
def open_coin_shop():
    coin_win = tk.Toplevel(window)
    coin_win.title("🪙 Exclusive Coin Shop")
    coin_win.geometry("400x380")
    coin_win.config(bg="#332233")

    title = tk.Label(coin_win, text="🪙 THE EXCLUSIVE COIN SHOP 🪙", font=("Arial", 13, "bold"), fg="gold", bg="#332233")
    title.pack(pady=10)

    coin_status = tk.Label(coin_win, text=f"Your Balance: 🪙 {coins} Coins", font=("Arial", 11, "bold"), fg="cyan", bg="#332233")
    coin_status.pack(pady=5)

    def update_coin_shop_label():
        coin_status.config(text=f"Your Balance: 🪙 {coins} Coins")
        update_main_display()

    def buy_golden_cookie():
        global score, coins
        if coins >= 5:
            coins -= 5
            score += 500
            update_coin_shop_label()
            shop_msg.config(text="Purchased! +500 Cookies added! 🍪", fg="lightgreen")
        else:
            shop_msg.config(text="Not enough coins! Win 1v1 Battles to get more.", fg="red")

    def buy_coin_click_boost():
        global coins, cookies_per_click
        if coins >= 10:
            coins -= 10
            cookies_per_click += 5
            update_coin_shop_label()
            shop_msg.config(text="Purchased! +5 Permanent Click Power! ⚡", fg="lightgreen")
        else:
            shop_msg.config(text="Not enough coins! Need 10.", fg="red")

    def buy_troll_shield():
        global coins, coin_multiplier
        if coins >= 20:
            coins -= 20
            coin_multiplier *= 2
            update_coin_shop_label()
            shop_msg.config(text="Purchased! Battle coin rewards doubled! 🛡️", fg="lightgreen")
        else:
            shop_msg.config(text="Not enough coins! Need 20.", fg="red")

    shop_msg = tk.Label(coin_win, text="Spend your hard-earned battle coins here!", font=("Arial", 9, "italic"), fg="white", bg="#332233")
    shop_msg.pack(pady=5)

    # Coin Shop Buttons
    tk.Button(coin_win, text="🍪 Buy +500 Cookies (Cost: 5 Coins)", font=("Arial", 10, "bold"), bg="gold", width=32, command=buy_golden_cookie).pack(pady=8)
    tk.Button(coin_win, text="⚡ Buy +5 Click Power (Cost: 10 Coins)", font=("Arial", 10, "bold"), bg="orange", width=32, command=buy_coin_click_boost).pack(pady=8)
    tk.Button(coin_win, text="🛡️ Buy 2x Coin Multiplier (Cost: 20 Coins)", font=("Arial", 10, "bold"), bg="plum", width=32, command=buy_troll_shield).pack(pady=8)

    tk.Button(coin_win, text="Close Coin Shop", font=("Arial", 9), bg="gray", command=coin_win.destroy).pack(pady=15)


# ==========================================
# PART 5: 1v1 Battle Arena Mode Window
# ==========================================
def open_battle_arena():
    battle_win = tk.Toplevel(window)
    battle_win.title("⚔️ 1v1 Cookie Battle Arena")
    battle_win.geometry("420x460")
    battle_win.config(bg="#222244")

    battle_data = {"p_score": 0, "ai_score": 0, "target": 30, "ai_speed": 300, "active": False}

    title = tk.Label(battle_win, text="⚔️ 1v1 CLICK BATTLE ⚔️", font=("Arial", 14, "bold"), fg="gold", bg="#222244")
    title.pack(pady=10)

    instruction = tk.Label(battle_win, text="Select Difficulty to Start Battle:", font=("Arial", 10), fg="white", bg="#222244")
    instruction.pack(pady=5)

    score_display = tk.Label(battle_win, text="You: 0  vs  AI: 0", font=("Arial", 14, "bold"), fg="cyan", bg="#222244")
    score_display.pack(pady=15)

    click_arena_btn = tk.Button(battle_win, text="⚔️ CLICK AS FAST AS YOU CAN! ⚔️", font=("Arial", 12, "bold"), bg="orange", fg="black", state="disabled")
    click_arena_btn.pack(pady=15, ipadx=10, ipady=10)

    result_label = tk.Label(battle_win, text="", font=("Arial", 11, "bold"), fg="yellow", bg="#222244")
    result_label.pack(pady=10)

    def start_battle(difficulty):
        battle_data["p_score"] = 0
        battle_data["ai_score"] = 0
        battle_data["active"] = True
        result_label.config(text="BATTLE STARTED! CLICK!", fg="lightgreen")
        click_arena_btn.config(state="normal")
        
        if difficulty == "easy":
            battle_data["ai_speed"] = 450
        elif difficulty == "mid":
            battle_data["ai_speed"] = 250
        elif difficulty == "hardcore":
            battle_data["ai_speed"] = 110
            
        battle_win.after(battle_data["ai_speed"], ai_tick)

    def player_battle_click():
        if not battle_data["active"]:
            return
        battle_data["p_score"] += 1
        score_display.config(text=f"You: {battle_data['p_score']}  vs  AI: {battle_data['ai_score']}")
        
        if battle_data["p_score"] >= battle_data["target"]:
            battle_data["active"] = False
            click_arena_btn.config(state="disabled")
            
            # Calculate rewards with multiplier!
            global score, coins, coin_multiplier
            earned_cookies = 1000
            earned_coins = 12 * coin_multiplier
            
            result_label.config(text=f"🎉 VICTORY! +{earned_cookies} Cookies & +{earned_coins} Coins!", fg="gold")
            
            score += earned_cookies
            coins += earned_coins
            update_main_display()
            battle_win.after(2200, battle_win.destroy)

    def ai_tick():
        if not battle_data["active"]:
            return
        battle_data["ai_score"] += 1
        score_display.config(text=f"You: {battle_data['p_score']}  vs  AI: {battle_data['ai_score']}")
        
        if battle_data["ai_score"] >= battle_data["target"]:
            battle_data["active"] = False
            click_arena_btn.config(state="disabled")
            result_label.config(text="💀 DEFEAT! The AI crushed you.", fg="red")
            battle_win.after(2200, battle_win.destroy)
        else:
            battle_win.after(battle_data["ai_speed"], ai_tick)

    click_arena_btn.config(command=player_battle_click)

    diff_frame = tk.Frame(battle_win, bg="#222244")
    diff_frame.pack(pady=10)

    tk.Button(diff_frame, text="Easy", bg="lightblue", font=("Arial", 9, "bold"), width=9, command=lambda: start_battle("easy")).pack(side="left", padx=5)
    tk.Button(diff_frame, text="Mid", bg="yellow", font=("Arial", 9, "bold"), width=9, command=lambda: start_battle("mid")).pack(side="left", padx=5)
    tk.Button(diff_frame, text="Hardcore", bg="crimson", fg="white", font=("Arial", 9, "bold"), width=9, command=lambda: start_battle("hardcore")).pack(side="left", padx=5)


# ==========================================
# PART 6: Main GUI Window Layout
# ==========================================
window = tk.Tk()
window.title("Cookie Clicker, Battle Arena & Coin Shop")
window.geometry("450x690")

title_label = tk.Label(window, text="🍪 Cookie, Troll & Coin Clicker 🍪", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

status_label = tk.Label(window, text="Welcome! Win battles, earn coins, hit the shops.", font=("Arial", 10, "italic"), fg="blue")
status_label.pack(pady=5)

counter_label = tk.Label(window, text="Cookies: 0 | 🪙 Coins: 0", font=("Arial", 14, "bold"))
counter_label.pack(pady=10)

click_btn = tk.Button(window, text="CLICK FOR COOKIES!", font=("Arial", 12, "bold"), bg="gold", command=click_counter)
click_btn.pack(pady=10)

# --- SHOP & MODES SECTION ---
shop_title = tk.Label(window, text="--- SHOPS & MODES ---", font=("Arial", 12, "bold"))
shop_title.pack(pady=5)

# 1v1 Battle Mode Button
battle_btn = tk.Button(window, text="⚔️ Play 1v1 Battle Mode (Win Coins)", font=("Arial", 10, "bold"), bg="deepskyblue", fg="black", command=open_battle_arena)
battle_btn.pack(pady=5)

# Coin Shop Button (NEW!)
coin_shop_btn = tk.Button(window, text="🪙 Open Exclusive Coin Shop", font=("Arial", 10, "bold"), bg="gold", fg="black", command=open_coin_shop)
coin_shop_btn.pack(pady=5)

cheat_btn = tk.Button(window, text="🧌 Buy Cheat Mode - Cost: 200 Cookies", font=("Arial", 10, "bold"), bg="plum", command=buy_cheat_mode)
cheat_btn.pack(pady=5)

buy_btn = tk.Button(window, text="Buy 1-Up (+1 Click) - Cost: 100 Cookies", font=("Arial", 10), bg="lightgreen", command=buy_powerup)
buy_btn.pack(pady=5)

ban_btn = tk.Button(window, text="🔨 Buy Ban Hammer - Cost: 1,000,000", font=("Arial", 10, "bold"), bg="crimson", fg="white", command=buy_ban_hammer)
ban_btn.pack(pady=5)

reset_btn = tk.Button(window, text="Reset Game", font=("Arial", 9), command=reset_game)
reset_btn.pack(pady=15)

window.mainloop()