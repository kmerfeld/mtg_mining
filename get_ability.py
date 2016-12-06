from mtgjson import CardDb

def get_ability(card):
    

    try:
        this = card.text

        if "Deathtouch" in this:
            return "Deathtouch"
        elif "Double strike" in this:
            return "Double strike"
        elif "First strike" in this:
            return "First strike"
        elif "Flash" in this:
            return "Flash"
        elif "Flying" in this:
            return "Flying"
        elif "Haste" in this:
            return "Haste"
        elif "Hexproof" in this:
            return "Hexproof"
        elif "Indestructible" in this:
            return "Indestructible"
        elif "Lifelink" in this:
            return "Lifelink"
        elif "Menace" in this:
            return "Menace"
        elif "Prowess" in this:
            return "Prowess"
        elif "Reach" in this:
            return "Reach"
        elif "Trample" in this:
            return "Trample"
        elif "Vigilance" in this:
            return "Vigilance"
        else:
            return "none"
    except:
        return "none"
    

