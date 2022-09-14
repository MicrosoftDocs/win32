---
title: Accelerator Tables
description: Accelerator Tables
ms.assetid: 4F2CFD7C-90D3-4C3F-9A42-05B915914EF6
ms.topic: article
ms.date: 05/31/2018
---

# Accelerator Tables

Applications often define keyboard shortcuts, such as CTRL+O for the File Open command. You could implement keyboard shortcuts by handling individual [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) messages, but accelerator tables provide a better solution that:

-   Requires less coding.
-   Consolidates all of your shortcuts into one data file.
-   Supports localization into other languages.
-   Enables shortcuts and menu commands to use the same application logic.

An *accelerator table* is a data resource that maps keyboard combinations, such as CTRL+O, to application commands. Before we see how to use an accelerator table, we'll need a quick introduction to resources. A *resource* is a data blob that is built into an application binary (EXE or DLL). Resources store data that are needed by the application, such as menus, cursors, icons, images, text strings, or any custom application data. The application loads the resource data from the binary at run time. To include resources in a binary, do the following:

1.  Create a resource definition (.rc) file. This file defines the types of resources and their identifiers. The resource definition file may include references to other files. For example, an icon resource is declared in the .rc file, but the icon image is stored in a separate file.
2.  Use the Microsoft Windows Resource Compiler (RC) to compile the resource definition file into a compiled resource (.res) file. The RC compiler is provided with Visual Studio and also the Windows SDK.
3.  Link the compiled resource file to the binary file.

These steps are roughly equivalent to the compile/link process for code files. Visual Studio provides a set of resource editors that make it easy to create and modify resources. (These tools are not available in the Express editions of Visual Studio.) But an .rc file is simply a text file, and the syntax is documented on MSDN, so it is possible to create an .rc file using any text editor. For more information, see [About Resource Files](/windows/desktop/menurc/about-resource-files).

## Defining an Accelerator Table

An accelerator table is a table of keyboard shortcuts. Each shortcut is defined by:

-   A numeric identifier. This number identifies the application command that will be invoked by the shortcut.
-   The ASCII character or virtual-key code of the shortcut.
-   Optional modifier keys: ALT, SHIFT, or CTRL.

The accelerator table itself has a numeric identifier, which identifies the table in the list of application resources. Let's create an accelerator table for a simple drawing program. This program will have two modes, draw mode and selection mode. In draw mode, the user can draw shapes. In selection mode, the user can select shapes. For this program, we would like to define the following keyboard shortcuts.



| Shortcut | Command                   |
|----------|---------------------------|
| CTRL+M   | Toggle between modes.     |
| F1       | Switch to draw mode.      |
| F2       | Switch to selection mode. |



 

First, define numeric identifiers for the table and for the application commands. These values are arbitrary. You can assign symbolic constants for the identifiers by defining them in a header file. For example:


```C++
#define IDR_ACCEL1                      101
#define ID_TOGGLE_MODE                40002
#define ID_DRAW_MODE                  40003
#define ID_SELECT_MODE                40004
```



In this example, the value `IDR_ACCEL1` identifies the accelerator table, and the next three constants define the application commands. By convention, a header file that defines resource constants is often named resource.h. The next listing shows the resource definition file.


```C++
#include "resource.h"

IDR_ACCEL1 ACCELERATORS
{
    0x4D,   ID_TOGGLE_MODE, VIRTKEY, CONTROL    // ctrl-M
    0x70,   ID_DRAW_MODE, VIRTKEY               // F1
    0x71,   ID_SELECT_MODE, VIRTKEY             // F2
}
```



The accelerator shortcuts are defined within the curly braces. Each shortcut contains the following entries.

-   The virtual-key code or ASCII character that invokes the shortcut.
-   The application command. Notice that symbolic constants are used in the example. The resource definition file includes resource.h, where these constants are defined.
-   The keyword **VIRTKEY** means the first entry is a virtual-key code. The other option is to use ASCII characters.
-   Optional modifiers: ALT, CONTROL, or SHIFT.

If you use ASCII characters for shortcuts, then a lowercase character will be a different shortcut than an uppercase character. (For example, typing 'a' might invoke a different command than typing 'A'.) That might confuse users, so it is generally better to use virtual-key codes, rather than ASCII characters, for shortcuts.

## Loading the Accelerator Table

The resource for the accelerator table must be loaded before the program can use it. To load an accelerator table, call the [**LoadAccelerators**](/windows/desktop/api/winuser/nf-winuser-loadacceleratorsa) function.


```C++
    HACCEL hAccel = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDR_ACCEL1));
```



Call this function before you enter the message loop. The first parameter is the handle to the module. (This parameter is passed to your [**WinMain**](/windows/desktop/api/winbase/nf-winbase-winmain) function. For details, see [WinMain: The Application Entry Point](winmain--the-application-entry-point.md).) The second parameter is the resource identifier. The function returns a handle to the resource. Recall that a handle is an opaque type that refers to an object managed by the system. If the function fails, it returns **NULL**.

You can release an accelerator table by calling [**DestroyAcceleratorTable**](/windows/desktop/api/winuser/nf-winuser-destroyacceleratortable). However, the system automatically releases the table when the program exits, so you only need to call this function if you are replacing one table with another. There is an interesting example of this in the topic [Creating User Editable Accelerators](/windows/desktop/menurc/using-keyboard-accelerators).

## Translating Key Strokes into Commands

An accelerator table works by translating key strokes into [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages. The *wParam* parameter of **WM\_COMMAND** contains the numeric identifier of the command. For example, using the table shown previously, the key stroke CTRL+M is translated into a **WM\_COMMAND** message with the value `ID_TOGGLE_MODE`. To make this happen, change your message loop to the following:


```C++
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0))
    {
        if (!TranslateAccelerator(win.Window(), hAccel, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }
```



This code adds a call to the [**TranslateAccelerator**](/windows/desktop/api/winuser/nf-winuser-translateacceleratora) function inside the message loop. The **TranslateAccelerator** function examines each window message, looking for key-down messages. If the user presses one of the key combinations listed in the accelerator table, **TranslateAccelerator** sends a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the window. The function sends **WM\_COMMAND** by directly invoking the window procedure. When **TranslateAccelerator** successfully translates a key stroke, the function returns a non-zero value, which means you should skip the normal processing for the message. Otherwise, **TranslateAccelerator** returns zero. In that case, pass the window message to [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) and [**DispatchMessage**](/windows/desktop/api/winuser/nf-winuser-dispatchmessage), as normal.

Here is how the drawing program might handle the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message:


```C++
    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case ID_DRAW_MODE:
            SetMode(DrawMode);
            break;

        case ID_SELECT_MODE:
            SetMode(SelectMode);
            break;

        case ID_TOGGLE_MODE:
            if (mode == DrawMode)
            {
                SetMode(SelectMode);
            }
            else
            {
                SetMode(DrawMode);
            }
            break;
        }
        return 0;

```



This code assumes that `SetMode` is a function defined by the application to switch between the two modes. The details of how you would handle each command obviously depend on your program.

## Next

[Setting the Cursor Image](setting-the-cursor-image.md)

 

 
