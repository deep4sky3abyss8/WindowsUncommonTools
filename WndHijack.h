/*--------------------------------------------------------------------------

[ WndHijack.h ]

This module/header Let You disable user control prg window .

HIJACK_COMMANDs -> 0:Failed / 1:Clear


[Note]

    * It's not working on Unix-based Operating Systems .
    * No need ';' at the End of commands .
    * Changes will not reset End of prg -> everything is manual -> don't forget RESET at the end
    * Commands must be out of funcs .
    * Every command will return [0] for error , check return value 
    
    * It's OK for old version CMD/Terminals .
    * It's Implemented in a header file to make manual complie more easy -> Just need to include and Use .



Usage Exp :

    #include "./PATH to /WndHijack.h"

    int status = HIJACK_CLOSE_btm

    if ( status ){
        Printf(" now try to close prg by btm [X]... ");
        RESET_HIJACKING
    }


Good Luck ...
Deep4SkyAbyss
--------------------------------------------------------------------------*/

#ifndef WINDOW_HIJACK_H
#define WINDOW_HIJACK_H

#include <windows.h>

#define HIJACKED 1;

//------------------------------------------------------------

static int Force_Full_screen(void){

    // -> getting manual terminal wnd handel
    HWND hwnd = GetConsoleWindow() ;
    
    if ( hwnd ) 
        SendMessage( hwnd , WM_SYSCOMMAND , SC_MAXIMIZE , 0 );

    else        
        return 0 ;
    
    return HIJACKED ;
} 
//------------------------------------------------------------

static int Force_Block_Minimize(void){

    HWND hwnd = GetConsoleWindow();
    if ( hwnd ) {
        HMENU hmenu = GetSystemMenu(hwnd , FALSE );
        
        if ( hmenu )    
            DeleteMenu( hmenu ,SC_MINIMIZE ,MF_BYCOMMAND );
        else            
            return 0;

        return HIJACKED ;
    }
    else    return 0 ;
}
//------------------------------------------------------------

static int Force_Block_Maximize(void){

    HWND hwnd = GetConsoleWindow();
    if ( hwnd ) {
        HMENU hmenu = GetSystemMenu(hwnd , FALSE );
        
        if ( hmenu ){  
            DeleteMenu( hmenu ,SC_MAXIMIZE ,MF_BYCOMMAND );
            DeleteMenu(hmenu, SC_RESTORE, MF_BYCOMMAND);
        }
        else            
            return 0;

        return HIJACKED ;
    }
    else    return 0 ;
}
//------------------------------------------------------------

static int Force_Block_Close(void){

    HWND hwnd = GetConsoleWindow();
    if ( hwnd ) {
        HMENU hmenu = GetSystemMenu(hwnd , FALSE );
        
        if ( hmenu )    
            DeleteMenu( hmenu ,SC_CLOSE ,MF_BYCOMMAND );
        else            
            return 0;

        return HIJACKED ;
    }
    else    return 0 ;
}
//------------------------------------------------------------

static int reset_btms(void){

    HWND hwnd = GetConsoleWindow();

    if ( hwnd )     GetSystemMenu( hwnd , TRUE ) ;
    else            return 0 ;

    return 1;
}
//------------------------------------------------------------


#define     HIJACK_FULL_SCREEN          Force_Full_screen();
#define     HIJACK_MINIMIZE_btm         Force_Block_Minimize();
#define     HIJACK_MAXIMIZE_bmt         Force_Block_Maximize();
#define     HIJACK_CLOSE_btm            Force_Block_Close();
#define     RESET_HIJACKING             reset_btms();


#endif
