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


Usage Exp :

    #include "./PATH to /colorama.h"

    RED
    Printf("hello world!");
    RESET


Good Luck ...
Deep4SkyAbyss
--------------------------------------------------------------------------*/

#ifndef COLORAMA_H
#define COLORAMA_H

#include <stdio.h>
#include <windows.h>


enum COLORS {
    BLACK = 0,
    RED = 4,
    GREEN = 2,
    YELLOW = 6,
    BLUE = 1,
    MAGENTA = 5,
    CYAN = 3,
    WHITE = 7,
    RESET = 7
};

static void set_color(int color) {

    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
}
//------------------------------------------------------------


#define     RED          set_color(RED);
#define     GREEN        set_color(GREEN);
#define     YELLOW       set_color(YELLOW);
#define     RESET        set_color(RESET);
#define     BLUE         set_color(BLUE);

#endif 
