---
description: This section explains how to perform tasks associated with the Multiple Document Interface.
ms.assetid: 024744d3-362f-4162-8d0a-d4dac61de808
title: Using the Multiple Document Interface
ms.topic: article
ms.date: 05/31/2018
---

# Using the Multiple Document Interface

This section explains how to perform the following tasks:

-   [Registering Child and Frame Window Classes](#registering-child-and-frame-window-classes)
-   [Creating Frame and Child Windows](#creating-frame-and-child-windows)
-   [Writing the Main Message Loop](#writing-the-main-message-loop)
-   [Writing the Frame Window Procedure](#writing-the-frame-window-procedure)
-   [Writing the Child Window Procedure](#writing-the-child-window-procedure)
-   [Creating a Child Window](#creating-a-child-window)

To illustrate these tasks, this section includes examples from Multipad, a typical multiple-document interface (MDI) application.

## Registering Child and Frame Window Classes

A typical MDI application must register two window classes: one for its frame window and one for its child windows. If an application supports more than one type of document (for example, a spreadsheet and a chart), it must register a window class for each type.

The class structure for the frame window is similar to the class structure for the main window in non–MDI applications. The class structure for the MDI child windows differs slightly from the structure for child windows in non–MDI applications as follows:

-   The class structure should have an icon, because the user can minimize an MDI child window as if it were a normal application window.
-   The menu name should be **NULL**, because an MDI child window cannot have its own menu.
-   The class structure should reserve extra space in the window structure. With this space, the application can associate data, such as a filename, with a particular child window.

The following example shows how Multipad registers its frame and child window classes.


```
BOOL WINAPI InitializeApplication() 
{ 
    WNDCLASS wc; 
 
    // Register the frame window class. 
 
    wc.style         = 0; 
    wc.lpfnWndProc   = (WNDPROC) MPFrameWndProc; 
    wc.cbClsExtra    = 0; 
    wc.cbWndExtra    = 0; 
    wc.hInstance     = hInst; 
    wc.hIcon         = LoadIcon(hInst, IDMULTIPAD); 
    wc.hCursor       = LoadCursor((HANDLE) NULL, IDC_ARROW); 
    wc.hbrBackground = (HBRUSH) (COLOR_APPWORKSPACE + 1); 
    wc.lpszMenuName  = IDMULTIPAD; 
    wc.lpszClassName = szFrame; 
 
    if (!RegisterClass (&wc) ) 
        return FALSE; 
 
    // Register the MDI child window class. 
 
    wc.lpfnWndProc   = (WNDPROC) MPMDIChildWndProc; 
    wc.hIcon         = LoadIcon(hInst, IDNOTE); 
    wc.lpszMenuName  = (LPCTSTR) NULL; 
    wc.cbWndExtra    = CBWNDEXTRA; 
    wc.lpszClassName = szChild; 
 
    if (!RegisterClass(&wc)) 
        return FALSE; 
 
    return TRUE; 
} 
```



## Creating Frame and Child Windows

After registering its window classes, an MDI application can create its windows. First, it creates its frame window by using the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. After creating its frame window, the application creates its client window, again by using **CreateWindow** or **CreateWindowEx**. The application should specify MDICLIENT as the client window's class name; **MDICLIENT** is a preregistered window class defined by the system. The *lpvParam* parameter of **CreateWindow** or **CreateWindowEx** should point to a [**CLIENTCREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-clientcreatestruct) structure. This structure contains the members described in the following table:



| Member           | Description                                                                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **hWindowMenu**  | Handle to the window menu used for controlling MDI child windows. As child windows are created, the application adds their titles to the window menu as menu items. The user can then activate a child window by clicking its title on the window menu.                                                               |
| **idFirstChild** | Specifies the identifier of the first MDI child window. The first MDI child window created is assigned this identifier. Additional windows are created with incremented window identifiers. When a child window is destroyed, the system immediately reassigns the window identifiers to keep their range contiguous. |



 

When a child window's title is added to the window menu, the system assigns an identifier to the child window. When the user clicks a child window's title, the frame window receives a [**WM\_COMMAND**](../menurc/wm-command.md) message with the identifier in the *wParam* parameter. You should specify a value for the **idFirstChild** member that does not conflict with menu-item identifiers in the frame window's menu.

Multipad's frame window procedure creates the MDI client window while processing the [**WM\_CREATE**](wm-create.md) message. The following example shows how the client window is created.


```
case WM_CREATE: 
    { 
        CLIENTCREATESTRUCT ccs; 
 
        // Retrieve the handle to the window menu and assign the 
        // first child window identifier. 
 
        ccs.hWindowMenu = GetSubMenu(GetMenu(hwnd), WINDOWMENU); 
        ccs.idFirstChild = IDM_WINDOWCHILD; 
 
        // Create the MDI client window. 
 
        hwndMDIClient = CreateWindow( "MDICLIENT", (LPCTSTR) NULL, 
            WS_CHILD | WS_CLIPCHILDREN | WS_VSCROLL | WS_HSCROLL, 
            0, 0, 0, 0, hwnd, (HMENU) 0xCAC, hInst, (LPSTR) &ccs); 
 
        ShowWindow(hwndMDIClient, SW_SHOW); 
    } 
    break; 
```



Titles of child windows are added to the bottom of the window menu. If the application adds strings to the window menu by using the [**AppendMenu**](/windows/win32/api/winuser/nf-winuser-appendmenua) function, these strings can be overwritten by the titles of the child windows when the window menu is repainted (whenever a child window is created or destroyed). An MDI application that adds strings to its window menu should use the [**InsertMenu**](/windows/win32/api/winuser/nf-winuser-insertmenua) function and verify that the titles of child windows have not overwritten these new strings.

Use the **WS\_CLIPCHILDREN** style to create the MDI client window to prevent the window from painting over its child windows.

## Writing the Main Message Loop

The main message loop of an MDI application is similar to that of a non-MDI application handling accelerator keys. The difference is that the MDI message loop calls the [**TranslateMDISysAccel**](/windows/win32/api/winuser/nf-winuser-translatemdisysaccel) function before checking for application-defined accelerator keys or before dispatching the message.

The following example shows the message loop of a typical MDI application. Note that [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) can return -1 if there is an error.


```
MSG msg;
BOOL bRet;

while ((bRet = GetMessage(&msg, (HWND) NULL, 0, 0)) != 0)
{
    if (bRet == -1)
    {
        // handle the error and possibly exit
    }
    else 
    { 
        if (!TranslateMDISysAccel(hwndMDIClient, &msg) && 
                !TranslateAccelerator(hwndFrame, hAccel, &msg))
        { 
            TranslateMessage(&msg); 
            DispatchMessage(&msg); 
        } 
    } 
}
```



The [**TranslateMDISysAccel**](/windows/win32/api/winuser/nf-winuser-translatemdisysaccel) function translates [**WM\_KEYDOWN**](../inputdev/wm-keydown.md) messages into [**WM\_SYSCOMMAND**](../menurc/wm-syscommand.md) messages and sends them to the active MDI child window. If the message is not an MDI accelerator message, the function returns **FALSE**, in which case the application uses the [**TranslateAccelerator**](/windows/win32/api/winuser/nf-winuser-translateacceleratora) function to determine whether any of the application-defined accelerator keys were pressed. If not, the loop dispatches the message to the appropriate window procedure.

## Writing the Frame Window Procedure

The window procedure for an MDI frame window is similar to that of a non–MDI application's main window. The difference is that a frame window procedure passes all messages it does not handle to the [**DefFrameProc**](/windows/win32/api/winuser/nf-winuser-defframeproca) function rather than to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. In addition, the frame window procedure must also pass some messages that it does handle, including those listed in the following table.



| Message                                  | Response                                                                                                                                                                                                                                                            |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_COMMAND**](../menurc/wm-command.md)     | Activates the MDI child window that the user chooses. This message is sent when the user chooses an MDI child window from the window menu of the MDI frame window. The window identifier accompanying this message identifies the MDI child window to be activated. |
| [**WM\_MENUCHAR**](../menurc/wm-menuchar.md)   | Opens the window menu of the active MDI child window when the user presses the ALT+ – (minus) key combination.                                                                                                                                                      |
| [**WM\_SETFOCUS**](../inputdev/wm-setfocus.md) | Passes the keyboard focus to the MDI client window, which in turn passes it to the active MDI child window.                                                                                                                                                         |
| [**WM\_SIZE**](wm-size.md)              | Resizes the MDI client window to fit in the new frame window's client area. If the frame window procedure sizes the MDI client window to a different size, it should not pass the message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.                   |



 

The frame window procedure in Multipad is called MPFrameWndProc. The handling of other messages by MPFrameWndProc is similar to that of non–MDI applications. [**WM\_COMMAND**](../menurc/wm-command.md) messages in Multipad are handled by the locally defined CommandHandler function. For command messages Multipad does not handle, CommandHandler calls the [**DefFrameProc**](/windows/win32/api/winuser/nf-winuser-defframeproca) function. If Multipad does not use **DefFrameProc** by default, the user can't activate a child window from the window menu, because the **WM\_COMMAND** message sent by clicking the window's menu item would be lost.

## Writing the Child Window Procedure

Like the frame window procedure, an MDI child window procedure uses a special function for processing messages by default. All messages that the child window procedure does not handle must be passed to the [**DefMDIChildProc**](/windows/win32/api/winuser/nf-winuser-defmdichildproca) function rather than to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. In addition, some window-management messages must be passed to **DefMDIChildProc**, even if the application handles the message, in order for MDI to function correctly. Following are the messages the application must pass to **DefMDIChildProc**.



| Message                                       | Response                                                                                                                                                                                                                                                  |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CHILDACTIVATE**](wm-childactivate.md) | Performs activation processing when MDI child windows are sized, moved, or displayed. This message must be passed.                                                                                                                                        |
| [**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md) | Calculates the size of a maximized MDI child window, based on the current size of the MDI client window.                                                                                                                                                  |
| [**WM\_MENUCHAR**](../menurc/wm-menuchar.md)        | Passes the message to the MDI frame window.                                                                                                                                                                                                               |
| [**WM\_MOVE**](wm-move.md)                   | Recalculates MDI client scroll bars, if they are present.                                                                                                                                                                                                 |
| [**WM\_SETFOCUS**](../inputdev/wm-setfocus.md)      | Activates the child window, if it is not the active MDI child window.                                                                                                                                                                                     |
| [**WM\_SIZE**](wm-size.md)                   | Performs operations necessary for changing the size of a window, especially for maximizing or restoring an MDI child window. Failing to pass this message to the [**DefMDIChildProc**](/windows/win32/api/winuser/nf-winuser-defmdichildproca) function produces highly undesirable results. |
| [**WM\_SYSCOMMAND**](../menurc/wm-syscommand.md)    | Handles window (formerly known as system) menu commands: **SC\_NEXTWINDOW**, **SC\_PREVWINDOW**, **SC\_MOVE**, **SC\_SIZE**, and **SC\_MAXIMIZE**.                                                                                                        |



 

## Creating a Child Window

To create an MDI child window, an application can either call the [**CreateMDIWindow**](/windows/win32/api/winuser/nf-winuser-createmdiwindowa) function or send an [**WM\_MDICREATE**](wm-mdicreate.md) message to the MDI client window. (The application can use the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function with the **WS\_EX\_MDICHILD** style to create MDI child windows.) A single-threaded MDI application can use either method to create a child window. A thread in a multithreaded MDI application must use the **CreateMDIWindow** or **CreateWindowEx** function to create a child window in a different thread.

The *lParam* parameter of a [**WM\_MDICREATE**](wm-mdicreate.md) message is a far pointer to an [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure. The structure includes four dimension members: **x** and **y**, which indicate the horizontal and vertical positions of the window, and **cx** and **cy**, which indicate the horizontal and vertical extents of the window. Any of these members may be assigned explicitly by the application, or they may be set to **CW\_USEDEFAULT**, in which case the system selects a position, size, or both, according to a cascading algorithm. In any case, all four members must be initialized. Multipad uses **CW\_USEDEFAULT** for all dimensions.

The last member of the [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure is the **style** member, which may contain style bits for the window. To create an MDI child window that can have any combination of window styles, specify the **MDIS\_ALLCHILDSTYLES** window style. When this style is not specified, an MDI child window has the **WS\_MINIMIZE**, **WS\_MAXIMIZE**, **WS\_HSCROLL**, and **WS\_VSCROLL** styles as default settings.

Multipad creates its MDI child windows by using its locally defined AddFile function (located in the source file MPFILE.C). The AddFile function sets the title of the child window by assigning the **szTitle** member of the window's [**MDICREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-mdicreatestructa) structure to either the name of the file being edited or to "Untitled." The **szClass** member is set to the name of the MDI child window class registered in Multipad's InitializeApplication function. The **hOwner** member is set to the application's instance handle.

The following example shows the AddFile function in Multipad.


```
HWND APIENTRY AddFile(pName) 
TCHAR * pName; 
{ 
    HWND hwnd; 
    TCHAR sz[160]; 
    MDICREATESTRUCT mcs; 
 
    if (!pName) 
    { 
 
        // If the pName parameter is NULL, load the "Untitled" 
        // string from the STRINGTABLE resource and set the szTitle 
        // member of MDICREATESTRUCT. 
 
        LoadString(hInst, IDS_UNTITLED, sz, sizeof(sz)/sizeof(TCHAR)); 
        mcs.szTitle = (LPCTSTR) sz; 
    } 
    else 
 
        // Title the window with the full path and filename, 
        // obtained by calling the OpenFile function with the 
        // OF_PARSE flag, which is called before AddFile(). 
 
        mcs.szTitle = of.szPathName; 
 
    mcs.szClass = szChild; 
    mcs.hOwner  = hInst; 
 
    // Use the default size for the child window. 
 
    mcs.x = mcs.cx = CW_USEDEFAULT; 
    mcs.y = mcs.cy = CW_USEDEFAULT; 
 
    // Give the child window the default style. The styleDefault 
    // variable is defined in MULTIPAD.C. 
 
    mcs.style = styleDefault; 
 
    // Tell the MDI client window to create the child window. 
 
    hwnd = (HWND) SendMessage (hwndMDIClient, WM_MDICREATE, 0, 
        (LONG) (LPMDICREATESTRUCT) &mcs); 
 
    // If the file is found, read its contents into the child 
    // window's client area. 
 
    if (pName) 
    { 
        if (!LoadFile(hwnd, pName)) 
        { 
 
            // Cannot load the file; close the window. 
 
            SendMessage(hwndMDIClient, WM_MDIDESTROY, 
                (DWORD) hwnd, 0L); 
        } 
    } 
    return hwnd; 
} 
```



The pointer passed in the *lParam* parameter of the [**WM\_MDICREATE**](wm-mdicreate.md) message is passed to the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) function and appears as the first member in the [**CREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-createstructa) structure, passed in the [**WM\_CREATE**](wm-create.md) message. In Multipad, the child window initializes itself during **WM\_CREATE** message processing by initializing document variables in its extra data and by creating the edit control's child window.

 

 
