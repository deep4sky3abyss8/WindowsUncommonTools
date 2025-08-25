/*--------------------------------------------------------------------------

[ colorama.h ]

This module/header Let You change [ windows ] terminal text color .

[Note]

    * It's not working on Unix-based Operating Systems .
    * No need ';' at the End of commands .
    * color change will not reset End of prg -> everything is manual .
    * Commands must be out of funcs .
    * It's OK for old version CMD/Terminals .
    * It's Implemented in a header file to make manual complie more easy -> Just need to include and Use .
    * Eachone FORE/BACK if use , another one will reset .
    * if need both , must use function manually .


Usage Exp :

    #include "./PATH to /colorama.h"

    FORE_RED
    Printf(" red text ");                 -> Fore: Red / Back: defualt
    FORE_RESET

    BACK_YELLOW
    Printf(" yellow back ");              -> Fore: defualt / Back: Yellow
    BACK_RESET

    set_color( YELLOW | RED << 4 );       -> Fore: Yellow / Back: Red


Good Luck ...
Deep4SkyAbyss
--------------------------------------------------------------------------*/

#ifndef COLORAMA_H
#define COLORAMA_H

#include <windows.h>


static HANDLE hconsole = NULL;
static int    chseen   = 0 ;


enum COLORS {
    BLACK   = 0,
    RED     = 4,
    GREEN   = 2,
    YELLOW  = 6,
    BLUE    = 1,
    MAGENTA = 5,
    CYAN    = 3,
    WHITE   = 7,
    RESET   = 7
};


static int set_color(int color) {

    if ( !chseen ){
        hconsole = GetStdHandle( STD_OUTPUT_HANDLE );
        chseen = 1 ;
    }

    // there is an error in getting handel control
    if ( !hconsole || hconsole == INVALID_HANDLE_VALUE )
        return 0 ;

    SetConsoleTextAttribute(hconsole, color);
    return 1 ;
}




#define     FORE_RED          set_color(RED);
#define     FORE_BLACK        set_color(BLACK);
#define     FORE_MAGENTA      set_color(MAGENTA);
#define     FORE_CYAN         set_color(CYAN);
#define     FORE_GREEN        set_color(GREEN);
#define     FORE_YELLOW       set_color(YELLOW);
#define     FORE_BLUE         set_color(BLUE);
#define     FORE_RESET        set_color(RESET);

#define     BACK_RED          set_color( RED << 4 );
#define     BACK_MAGENTA      set_color( MAGENTA << 4 );
#define     BACK_CYAN         set_color( CYAN << 4 );
#define     BACK_WHITE        set_color( WHITE << 4 );
#define     BACK_GREEN        set_color( GREEN << 4 );
#define     BACK_YELLOW       set_color( YELLOW << 4 );
#define     BACK_BLUE         set_color( BLUE << 4 );
#define     BACK_RESET        set_color( BLACK << 4 );


#endif 
