---
title: Using Cursors
description: This section provides code samples that show how to perform tasks related to cursors.
ms.assetid: eab7b781-783e-4fc5-868d-6ff773c40a21
keywords:
- resources,cursors
- cursors,custom
- custom cursors
- hourglass cursor
- cursors,creating
- cursors,hourglass
- creating cursors
- destroying cursors
- displaying cursors
- confining cursors
- cursors,destroying
- cursors,displaying
- cursors,confining
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Cursors

This section discusses the following topics.

-   [Creating a Cursor](#creating-a-cursor)
-   [Displaying a Cursor](#displaying-a-cursor)
-   [Confining a Cursor](#confining-a-cursor)
-   [Using Cursor Functions to Create a Mousetrap](#using-cursor-functions-to-create-a-mousetrap)
-   [Using the Keyboard to Move the Cursor](#using-the-keyboard-to-move-the-cursor)

## Creating a Cursor

The following example creates two cursor handles: one for the standard hourglass cursor and one for a custom cursor included as a resource in the application's resource-definition file.


```
HINSTANCE hinst;            // handle to current instance 
HCURSOR hCurs1, hCurs2;     // cursor handles 
 
// Create a standard hourglass cursor. 
 
hCurs1 = LoadCursor(NULL, IDC_WAIT); 
 
// Create a custom cursor based on a resource. 
 
hCurs2 = LoadCursor(hinst, MAKEINTRESOURCE(240)); 
```



You should implement custom cursors as resources. Rather than create the cursors at run time, use the [**LoadCursor**](/windows/win32/Winuser/nf-winuser-loadcursora?branch=master), [**LoadCursorFromFile**](/windows/win32/Winuser/nf-winuser-loadcursorfromfilea?branch=master), or [**LoadImage**](/windows/win32/Winuser/nf-winuser-loadimagea?branch=master) function to avoid device dependence, to simplify localization, and to enable applications to share cursor designs.

The following example uses the [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master) function to create a custom cursor at run time. The example is included here to illustrate how the system interprets cursor masks.


```
HINSTANCE hinst;            // handle to current instance  
HCURSOR hCurs1, hCurs2;     // cursor handles 
 
HCURSOR hCurs3;             // cursor handle 
 
// Yin-shaped cursor AND mask 
 
BYTE ANDmaskCursor[] = 
{ 
    0xFF, 0xFC, 0x3F, 0xFF,   // line 1 
    0xFF, 0xC0, 0x1F, 0xFF,   // line 2 
    0xFF, 0x00, 0x3F, 0xFF,   // line 3 
    0xFE, 0x00, 0xFF, 0xFF,   // line 4 
 
    0xF7, 0x01, 0xFF, 0xFF,   // line 5 
    0xF0, 0x03, 0xFF, 0xFF,   // line 6 
    0xF0, 0x03, 0xFF, 0xFF,   // line 7 
    0xE0, 0x07, 0xFF, 0xFF,   // line 8 
 
    0xC0, 0x07, 0xFF, 0xFF,   // line 9 
    0xC0, 0x0F, 0xFF, 0xFF,   // line 10 
    0x80, 0x0F, 0xFF, 0xFF,   // line 11 
    0x80, 0x0F, 0xFF, 0xFF,   // line 12 
 
    0x80, 0x07, 0xFF, 0xFF,   // line 13 
    0x00, 0x07, 0xFF, 0xFF,   // line 14 
    0x00, 0x03, 0xFF, 0xFF,   // line 15 
    0x00, 0x00, 0xFF, 0xFF,   // line 16 
 
    0x00, 0x00, 0x7F, 0xFF,   // line 17 
    0x00, 0x00, 0x1F, 0xFF,   // line 18 
    0x00, 0x00, 0x0F, 0xFF,   // line 19 
    0x80, 0x00, 0x0F, 0xFF,   // line 20 
 
    0x80, 0x00, 0x07, 0xFF,   // line 21 
    0x80, 0x00, 0x07, 0xFF,   // line 22 
    0xC0, 0x00, 0x07, 0xFF,   // line 23 
    0xC0, 0x00, 0x0F, 0xFF,   // line 24 
 
    0xE0, 0x00, 0x0F, 0xFF,   // line 25 
    0xF0, 0x00, 0x1F, 0xFF,   // line 26 
    0xF0, 0x00, 0x1F, 0xFF,   // line 27 
    0xF8, 0x00, 0x3F, 0xFF,   // line 28 
 
    0xFE, 0x00, 0x7F, 0xFF,   // line 29 
    0xFF, 0x00, 0xFF, 0xFF,   // line 30 
    0xFF, 0xC3, 0xFF, 0xFF,   // line 31 
    0xFF, 0xFF, 0xFF, 0xFF    // line 32 
};
 
// Yin-shaped cursor XOR mask 
 
BYTE XORmaskCursor[] = 
{ 
    0x00, 0x00, 0x00, 0x00,   // line 1 
    0x00, 0x03, 0xC0, 0x00,   // line 2 
    0x00, 0x3F, 0x00, 0x00,   // line 3 
    0x00, 0xFE, 0x00, 0x00,   // line 4 
 
    0x0E, 0xFC, 0x00, 0x00,   // line 5 
    0x07, 0xF8, 0x00, 0x00,   // line 6 
    0x07, 0xF8, 0x00, 0x00,   // line 7 
    0x0F, 0xF0, 0x00, 0x00,   // line 8 
 
    0x1F, 0xF0, 0x00, 0x00,   // line 9 
    0x1F, 0xE0, 0x00, 0x00,   // line 10 
    0x3F, 0xE0, 0x00, 0x00,   // line 11 
    0x3F, 0xE0, 0x00, 0x00,   // line 12 
 
    0x3F, 0xF0, 0x00, 0x00,   // line 13 
    0x7F, 0xF0, 0x00, 0x00,   // line 14 
    0x7F, 0xF8, 0x00, 0x00,   // line 15 
    0x7F, 0xFC, 0x00, 0x00,   // line 16 
 
    0x7F, 0xFF, 0x00, 0x00,   // line 17 
    0x7F, 0xFF, 0x80, 0x00,   // line 18 
    0x7F, 0xFF, 0xE0, 0x00,   // line 19 
    0x3F, 0xFF, 0xE0, 0x00,   // line 20 
 
    0x3F, 0xC7, 0xF0, 0x00,   // line 21 
    0x3F, 0x83, 0xF0, 0x00,   // line 22 
    0x1F, 0x83, 0xF0, 0x00,   // line 23 
    0x1F, 0x83, 0xE0, 0x00,   // line 24 
 
    0x0F, 0xC7, 0xE0, 0x00,   // line 25 
    0x07, 0xFF, 0xC0, 0x00,   // line 26 
    0x07, 0xFF, 0xC0, 0x00,   // line 27 
    0x01, 0xFF, 0x80, 0x00,   // line 28 
 
    0x00, 0xFF, 0x00, 0x00,   // line 29 
    0x00, 0x3C, 0x00, 0x00,   // line 30 
    0x00, 0x00, 0x00, 0x00,   // line 31 
    0x00, 0x00, 0x00, 0x00    // line 32 
};
 
// Create a custom cursor at run time. 
 
hCurs3 = CreateCursor( hinst,   // app. instance 
             19,                // horizontal position of hot spot 
             2,                 // vertical position of hot spot 
             32,                // cursor width 
             32,                // cursor height 
             ANDmaskCursor,     // AND mask 
             XORmaskCursor );   // XOR mask 
```



To create the cursor, [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master) applies the following truth table to the **AND** and **XOR** masks.



| AND mask | XOR mask | Display        |
|----------|----------|----------------|
| 0        | 0        | Black          |
| 0        | 1        | White          |
| 1        | 0        | Screen         |
| 1        | 1        | Reverse screen |



 

For more information, see [Bitmaps](https://msdn.microsoft.com/library/windows/desktop/dd183377).

Before closing, you must use the [**DestroyCursor**](/windows/win32/Winuser/nf-winuser-destroycursor?branch=master) function to destroy any cursors you created with [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master). It is not necessary to destroy cursors created by other functions.

## Displaying a Cursor

The system automatically displays the class cursor (the cursor associated with the window to which the cursor is pointing). You can assign a class cursor while registering a window class. The following example illustrates this by assigning a cursor handle to the **hCursor** member of the [**WNDCLASS**](https://msdn.microsoft.com/library/windows/desktop/ms633576) structure identified by the *wc* parameter.


```
WNDCLASS  wc; 
 
// Fill the window class structure with parameters that 
// describe the main window. 
 
wc.style = NULL;                        // class style(s) 
wc.lpfnWndProc = (WNDPROC) MainWndProc; // window procedure 
wc.cbClsExtra = 0;           // no per-class extra data 
wc.cbWndExtra = 0;           // no per-window extra data 
wc.hInstance = hinst;        // application that owns the class 
wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);     // class icon 
wc.hCursor = LoadCursor(hinst, MAKEINTRESOURCE(230)); // class cursor 
wc.hbrBackground = GetStockObject(WHITE_BRUSH); // class background 
wc.lpszMenuName =  "GenericMenu";               // class menu 
wc.lpszClassName = "GenericWClass"              // class name 
 
// Register the window class. 
 
return RegisterClass(&amp;wc); 
```



When the window class is registered, the cursor identified by 230 in the application's resource-definition file is the default cursor for all windows based on the class.

Your application can change the design of the cursor by using the [**SetCursor**](/windows/win32/Winuser/nf-winuser-setcursor?branch=master) function and specifying a different cursor handle. However, when the cursor moves, the system redraws the class cursor at the new location. To prevent the class cursor from being redrawn, you must process the [**WM\_SETCURSOR**](wm-setcursor.md) message. Each time the cursor moves and mouse input is not captured, the system sends this message to the window in which the cursor is moving.

You can specify different cursors for different conditions while processing [**WM\_SETCURSOR**](wm-setcursor.md). For example, the following example shows how to display the cursor whenever the cursor moves over the icon of a minimized application.


```
case WM_SETCURSOR: 
 
    // If the window is minimized, draw the hCurs3 cursor. 
    // If the window is not minimized, draw the default 
    // cursor (class cursor). 
 
    if (IsIconic(hwnd)) 
    { 
        SetCursor(hCurs3); 
        break; 
    } 
```



When the window is not minimized, the system displays the class cursor.

You can replace a class cursor by using the [**SetClassLong**](https://msdn.microsoft.com/library/windows/desktop/ms633588) function. This function changes the default window settings for all windows of a specified class. The following example replaces the existing class cursor with the `hCurs2` cursor.


```
// Change the cursor for window class represented by hwnd. 
 
SetClassLong(hwnd,    // window handle 
    GCL_HCURSOR,      // change cursor 
    (LONG) hCurs2);   // new cursor 
```



For more information, see [Window Classes](https://msdn.microsoft.com/library/windows/desktop/ms632596) and [Mouse Input](https://msdn.microsoft.com/library/windows/desktop/ms645533).

## Confining a Cursor

The following example confines the cursor to the application's window and then restores the cursor to its previous window. The example uses the [**GetClipCursor**](/windows/win32/Winuser/nf-winuser-getclipcursor?branch=master) function to record the area in which the cursor can move and the [**ClipCursor**](/windows/win32/Winuser/nf-winuser-clipcursor?branch=master) function to confine and restore the cursor.


```
RECT rcClip;           // new area for ClipCursor
RECT rcOldClip;        // previous area for ClipCursor
 
// Record the area in which the cursor can move. 
 
GetClipCursor(&amp;rcOldClip); 
 
// Get the dimensions of the application's window. 
 
GetWindowRect(hwnd, &amp;rcClip); 
 
// Confine the cursor to the application's window. 
 
ClipCursor(&amp;rcClip); 
 
   // 
   // Process input from the confined cursor. 
   // 
 
// Restore the cursor to its previous area. 
 
ClipCursor(&amp;rcOldClip); 
```



Because there is only one cursor at a time available in the system, an application that confines the cursor must restore the cursor before relinquishing control to another window.

## Using Cursor Functions to Create a Mousetrap

The following example uses the [**SetCursorPos**](/windows/win32/Winuser/nf-winuser-setcursorpos?branch=master), [**GetCursorPos**](/windows/win32/Winuser/nf-winuser-getcursorpos?branch=master), [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master), [**LoadCursor**](/windows/win32/Winuser/nf-winuser-loadcursora?branch=master), and [**SetCursor**](/windows/win32/Winuser/nf-winuser-setcursor?branch=master) functions to create a simple mousetrap. It also uses cursor and timer functions to monitor the cursor's position every 10 seconds. If the cursor position has not changed in the last 10 seconds and the application's main window is minimized, the application changes the cursor and moves it to the mousetrap icon.

An example for a similar mousetrap is included in [Icons](icons.md). It uses the [**LoadCursor**](/windows/win32/Winuser/nf-winuser-loadcursora?branch=master) and [**LoadIcon**](/windows/win32/Winuser/nf-winuser-loadicona?branch=master) functions instead of the more device-dependent [**CreateCursor**](/windows/win32/Winuser/nf-winuser-createcursor?branch=master) and [**CreateIcon**](/windows/win32/Winuser/nf-winuser-createicon?branch=master) functions.


```
HICON hIcon1;               // icon handles 
POINT ptOld;                // previous cursor location 
HCURSOR hCurs1;             // cursor handle 
 
 
// The following cursor masks are defined in a code 
// example that appears earlier in this section. 
 
// Yin-shaped cursor AND and XOR masks 
 
BYTE ANDmaskCursor[] = ... 
BYTE XORmaskCursor[] = ... 
 
// Yang-shaped icon AND mask 
 
BYTE ANDmaskIcon[] = {0xFF, 0xFF, 0xFF, 0xFF,  // line 1 
                      0xFF, 0xFF, 0xC3, 0xFF,  // line 2 
                      0xFF, 0xFF, 0x00, 0xFF,  // line 3 
                      0xFF, 0xFE, 0x00, 0x7F,  // line 4 
 
                      0xFF, 0xFC, 0x00, 0x1F,  // line 5 
                      0xFF, 0xF8, 0x00, 0x0F,  // line 6 
                      0xFF, 0xF8, 0x00, 0x0F,  // line 7 
                      0xFF, 0xF0, 0x00, 0x07,  // line 8 
 
                      0xFF, 0xF0, 0x00, 0x03,  // line 9 
                      0xFF, 0xE0, 0x00, 0x03,  // line 10 
                      0xFF, 0xE0, 0x00, 0x01,  // line 11 
                      0xFF, 0xE0, 0x00, 0x01,  // line 12 
 
                      0xFF, 0xF0, 0x00, 0x01,  // line 13 
                      0xFF, 0xF0, 0x00, 0x00,  // line 14 
                      0xFF, 0xF8, 0x00, 0x00,  // line 15 
                      0xFF, 0xFC, 0x00, 0x00,  // line 16 
 
                      0xFF, 0xFF, 0x00, 0x00,  // line 17 
                      0xFF, 0xFF, 0x80, 0x00,  // line 18 
                      0xFF, 0xFF, 0xE0, 0x00,  // line 19 
                      0xFF, 0xFF, 0xE0, 0x01,  // line 20 
 
                      0xFF, 0xFF, 0xF0, 0x01,  // line 21 
                      0xFF, 0xFF, 0xF0, 0x01,  // line 22 
                      0xFF, 0xFF, 0xF0, 0x03,  // line 23 
                      0xFF, 0xFF, 0xE0, 0x03,  // line 24 
 
                      0xFF, 0xFF, 0xE0, 0x07,  // line 25 
                      0xFF, 0xFF, 0xC0, 0x0F,  // line 26 
                      0xFF, 0xFF, 0xC0, 0x0F,  // line 27 
                      0xFF, 0xFF, 0x80, 0x1F,  // line 28 
 
                      0xFF, 0xFF, 0x00, 0x7F,  // line 29 
                      0xFF, 0xFC, 0x00, 0xFF,  // line 30 
                      0xFF, 0xF8, 0x03, 0xFF,  // line 31 
                      0xFF, 0xFC, 0x3F, 0xFF}; // line 32 
 
// Yang-shaped icon XOR mask 
 
BYTE XORmaskIcon[] = {0x00, 0x00, 0x00, 0x00,  // line 1 
                      0x00, 0x00, 0x00, 0x00,  // line 2 
                      0x00, 0x00, 0x00, 0x00,  // line 3 
                      0x00, 0x00, 0x00, 0x00,  // line 4 
 
                      0x00, 0x00, 0x00, 0x00,  // line 5 
                      0x00, 0x00, 0x00, 0x00,  // line 6 
                      0x00, 0x00, 0x00, 0x00,  // line 7 
                      0x00, 0x00, 0x38, 0x00,  // line 8 
 
                      0x00, 0x00, 0x7C, 0x00,  // line 9 
                      0x00, 0x00, 0x7C, 0x00,  // line 10 
                      0x00, 0x00, 0x7C, 0x00,  // line 11  
                      0x00, 0x00, 0x38, 0x00,  // line 12 
 
                      0x00, 0x00, 0x00, 0x00,  // line 13 
                      0x00, 0x00, 0x00, 0x00,  // line 14 
                      0x00, 0x00, 0x00, 0x00,  // line 15 
                      0x00, 0x00, 0x00, 0x00,  // line 16 
 
                      0x00, 0x00, 0x00, 0x00,  // line 17 
                      0x00, 0x00, 0x00, 0x00,  // line 18 
                      0x00, 0x00, 0x00, 0x00,  // line 19 
                      0x00, 0x00, 0x00, 0x00,  // line 20 
 
                      0x00, 0x00, 0x00, 0x00,  // line 21 
                      0x00, 0x00, 0x00, 0x00,  // line 22 
                      0x00, 0x00, 0x00, 0x00,  // line 23 
                      0x00, 0x00, 0x00, 0x00,  // line 24 
 
                      0x00, 0x00, 0x00, 0x00,  // line 25 
                      0x00, 0x00, 0x00, 0x00,  // line 26 
                      0x00, 0x00, 0x00, 0x00,  // line 27 
                      0x00, 0x00, 0x00, 0x00,  // line 28 
 
                      0x00, 0x00, 0x00, 0x00,  // line 29 
                      0x00, 0x00, 0x00, 0x00,  // line 30 
                      0x00, 0x00, 0x00, 0x00,  // line 31 
                      0x00, 0x00, 0x00, 0x00}; // line 32 
 
hIcon1 = CreateIcon(hinst, // handle to app. instance 
             32,           // icon width 
             32,           // icon height 
             1,            // number of XOR planes 
             1,            // number of bits per pixel 
             ANDmaskIcon,  // AND mask 
             XORmaskIcon); // XOR mask 
 
hCurs1 = CreateCursor(hinst, // handle to app. instance
             19,             // horizontal position of hot spot 
             2,              // vertical position of hot spot 
             32,             // cursor width 
             32,             // cursor height 
             ANDmaskCursor,  // AND mask 
             XORmaskCursor); // XOR mask 
 
// Fill in the window class structure. 
 
WNDCLASS  wc; 
 
wc.hIcon = hIcon1;                        // class icon 
wc.hCursor = LoadCursor(NULL, IDC_ARROW); // class cursor 
 
//
// Register the window class and perform 
// other application initialization. 
//
 
// Set a timer for the mousetrap. 
 
GetCursorPos(&amp;ptOld); 
 
SetTimer(hwnd, IDT_CURSOR, 10000, (TIMERPROC) NULL); 
 
LONG APIENTRY MainWndProc( 
    HWND hwnd,          // window handle 
    UINT message,       // type of message 
    UINT wParam,        // additional information 
    LONG lParam)        // additional information 
{ 
 
    HDC hdc;            // handle to device context 
    POINT pt;           // current cursor location 
    RECT rc;            // minimized window location 
 
    switch (message) 
    { 
        //
        // Process other messages. 
        // 
        case WM_TIMER: 
        // If the window is minimized, compare the 
        // current cursor position with the one 10 
        // seconds before. If the cursor position has 
        // not changed, move the cursor to the icon. 
 
            if (IsIconic(hwnd)) 
            { 
                GetCursorPos(&amp;pt); 
 
                if ((pt.x == ptOld.x) &amp;&amp; (pt.y == ptOld.y)) 
                { 
                    GetWindowRect(hwnd, &amp;rc); 
                    SetCursorPos(rc.left + 20, rc.top + 4); 
 
                    // Note that the additional constants 
                    // (20 and 4) are application-specific 
                    // values to align the yin-shaped cursor 
                    // and the yang-shaped icon. 
 
                } 
                else 
                { 
                    ptOld.x = pt.x; 
                    ptOld.y = pt.y; 
                } 
            } 
 
            return 0; 
 
        case WM_SETCURSOR: 
        // If the window is minimized, draw hCurs1. 
        // If the window is not minimized, draw the 
        // default cursor (class cursor). 
 
            if (IsIconic(hwnd)) 
            { 
                SetCursor(hCurs1); 
                break; 
            } 
 
        case WM_DESTROY: 
        // Destroy timer. 
 
            KillTimer(hwnd, IDT_CURSOR); 
 
            PostQuitMessage(0); 
            break; 
    } 
} 
```



## Using the Keyboard to Move the Cursor

Because the system does not require a mouse, an application should be able to simulate mouse actions with the keyboard. The following example shows how to achieve this by using the [**GetCursorPos**](/windows/win32/Winuser/nf-winuser-getcursorpos?branch=master) and [**SetCursorPos**](/windows/win32/Winuser/nf-winuser-setcursorpos?branch=master) functions and by processing input from the arrow keys.


```
HCURSOR hCurs1, hCurs2;    // cursor handles 
 
POINT pt;                  // cursor location  
RECT rc;                   // client area coordinates 
static int repeat = 1;     // repeat key counter 
 
// 
// Other declarations and initialization. 
// 
 
switch (message) 
{ 
// 
// Process other messages. 
// 
 
    case WM_KEYDOWN: 
 
        if (wParam != VK_LEFT &amp;&amp; wParam != VK_RIGHT &amp;&amp; 
        wParam != VK_UP &amp;&amp; wParam != VK_DOWN) 
        { 
            break; 
        } 
 
        GetCursorPos(&amp;pt); 
 
        // Convert screen coordinates to client coordinates. 
 
        ScreenToClient(hwnd, &amp;pt); 
 
        switch (wParam) 
        { 
        // Move the cursor to reflect which 
        // arrow keys are pressed. 
 
            case VK_LEFT:               // left arrow 
                pt.x -= repeat; 
                break; 
 
            case VK_RIGHT:              // right arrow 
                pt.x += repeat; 
                break; 
 
            case VK_UP:                 // up arrow 
                pt.y -= repeat; 
                break; 
 
            case VK_DOWN:               // down arrow 
                pt.y += repeat; 
                break; 
 
            default: 
                return 0; 
        } 
 
        repeat++;           // Increment repeat count. 
 
        // Keep the cursor in the client area. 
 
        GetClientRect(hwnd, &amp;rc); 
 
        if (pt.x >= rc.right) 
        { 
            pt.x = rc.right - 1; 
        } 
        else 
        { 
            if (pt.x < rc.left) 
            { 
                pt.x = rc.left; 
            } 
        } 
 
        if (pt.y >= rc.bottom) 
            pt.y = rc.bottom - 1; 
        else 
            if (pt.y < rc.top) 
                pt.y = rc.top; 
 
        // Convert client coordinates to screen coordinates. 
 
        ClientToScreen(hwnd, &amp;pt); 
        SetCursorPos(pt.x, pt.y); 
        return 0; 

 
    case WM_KEYUP: 
 
        repeat = 1;            // Clear repeat count. 
        return 0; 
 
} 
```



 

 




