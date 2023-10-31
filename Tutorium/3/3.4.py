temp = input("Ist die Temperatur warm oder kalt?")
weather = input("Ist das Wetter sonnig, regnerisch oder verschneit?")

if temp == "kalt":
    if weather == "sonnig":
        print("Tragen Sie eine dicke Jacke und Sonnebrille!")
    elif weather == "regnerisch":
        print("Tragen Sie eine dicke Jacke und nehmen Sie einen Regenschirm mit!")
    elif weather == "verschneit":
        print("Trage Sie eine dicke Jacke, Mütze und Handschuhe!")
elif temp == "warm":
    if weather == "sonnig":
        print("Tragen Sie eine Sonnenbrille und eine kurze Hose!")
    elif weather == "regnerisch":
        print("Tragen Sie eine kurze Hose und nehmen Sie einen Regenschirm mit!")
    elif weather == "verschneit":
        print("Tragen Sie eine kurze Hose, Mütze und Handschuhe!")