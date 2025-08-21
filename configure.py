import os
import sys


def main():
    print("WAF configure")
    print("[1] 32 bits(x86)")
    print("[2] 64 bits(x64)")
    arch = int(input("Choice > "))
    if arch != 1 and arch != 2:
        raise Exception("You should enter a valid choice")

    print("[1] debug")
    print("[2] release")
    typee = int(input("Choice > "))    
    if typee != 1 and typee != 2:
        raise Exception("You should enter a valid choice")
    
    print("[1] hl2")
    print("[2] hl2mp")
    print("[3] episodic")
    print("[4] cstrike")    
    game = int(input("Choice > "))    
    if game != 1 and game != 2 and game != 3 and game != 4:
        raise Exception("You should enter a valid choice")
    
    # architecture
    if arch == 1:
        cfg_arch = "" # 32 bits is default, i dont need to type anything
    else:
        cfg_arch = "--64bits" 
    
    # type
    if typee == 1:
        cfg_type = "debug"
    else:
        cfg_type = "release"

    # game    
    if game == 1:
        cfg_game = "hl2"
    if game == 2:
        cfg_game = "hl2mp"
    if game == 3:
        cfg_game = "episodic"
    if game == 4:
        cfg_game = "cstrike"

    os.system("python waf configure -T " + cfg_type + " " + cfg_arch + " --build-games " + cfg_game + " --prefix BUILD_" + cfg_game)



if __name__ == '__main__':
    main()
