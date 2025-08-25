# ================================================================================

# This module can reduce user control over the console window.

# This modulu had implemented better By C in Uncommon-windows-Api-funcs github repo .

# [!] These types of function can hurt User-experience .
# [!] Be take care when using these functions ...
# [!] This module will not work on non-Windows platforms .



# Good Luck
# SkyAbyss

# ================================================================================

import ctypes

#=================================================================================
def HijackScreen():
    try:
            kernel32 = ctypes.windll.kernel32
            user32 = ctypes.windll.user32
            
            hwnd = kernel32.GetConsoleWindow()
            
            if hwnd:
                
                SW_MAXIMIZE = 3
                user32.ShowWindow(hwnd, SW_MAXIMIZE )
                
                return True
    
    except Exception as e:
        return False
    
#=================================================================================
def HijackMinimize():                                               # [!] -> must be off in dev system , mabey program crashed .
    
    try:
        
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        
        # 
        hwnd = kernel32.GetConsoleWindow()
        
        if hwnd:
            # 
            hMenu = user32.GetSystemMenu(hwnd, 0)
            if hMenu:
                
                SC_MIN = 0xF020
                MF_DISABLED = 0x00000000
                
                user32.DeleteMenu(hMenu, SC_MIN , MF_DISABLED )      # -> disable MINIMIZE      [ _ ]
                user32.DrawMenuBar(hwnd)                             # -> set changes
            
                return True
                
    except Exception as e:
        pass
    
    return False

#=================================================================================
def HijackMaximize():                                               # [!] -> must be off in dev system , mabey program crashed .
    try:
        
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        
        # 
        hwnd = kernel32.GetConsoleWindow()
        
        if hwnd:
            # 
            hMenu = user32.GetSystemMenu(hwnd, 0)
            if hMenu:
                
                SC_MAX = 0xF030
                SC_RST = 0xf120
                MF_DISABLED = 0x00000000
                
                user32.DeleteMenu(hMenu, SC_MAX, MF_DISABLED )      # -> disable MAXSIZE       [ # ]
                user32.DeleteMenu(hMenu, SC_RST, MF_DISABLED )      # -> disable MAXSIZE-restore
                
                user32.DrawMenuBar(hwnd)                            # -> set changes
                
                return True
                
    except Exception as e:
        pass
    
    return False
    
#=================================================================================
def HijackClose():                                                  # [!] -> must be off in dev system , mabey program crashed .
    try:
        
        kernel32 = ctypes.windll.kernel32
        user32 = ctypes.windll.user32
        
        hwnd = kernel32.GetConsoleWindow()
        
        if hwnd:
            # 
            hMenu = user32.GetSystemMenu(hwnd, 0)
            if hMenu:
                
                SC_CLOSE = 0xF060
                MF_DISABLED = 0x00000000
                
                user32.DeleteMenu(hMenu, SC_CLOSE , MF_DISABLED )      # -> disable CLOSE         [ X ]
                user32.DrawMenuBar(hwnd)                               # -> set changes
                
                return True
                
    except Exception as e:
        pass
    
    return False

#=================================================================================
#=================================================================================