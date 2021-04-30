---
description: This section explains how to perform the following tasks associated with window procedures.
ms.assetid: acc68991-4689-44dc-8547-a7b6153b0f62
title: Using Window Procedures
ms.topic: article
ms.date: 05/31/2018
---

# Using Window Procedures

This section explains how to perform the following tasks associated with window procedures.

-   [Designing a Window Procedure](#designing-a-window-procedure)
-   [Associating a Window Procedure with a Window Class](#associating-a-window-procedure-with-a-window-class)
-   [Subclassing a Window](#subclassing-a-window)

## Designing a Window Procedure

The following example shows the structure of a typical window procedure. The window procedure uses the message argument in a **switch** statement with individual messages handled by separate **case** statements. Notice that each case returns a specific value for each message. For messages that it does not process, the window procedure calls the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.


```
LRESULT CALLBACK MainWndProc(
    HWND hwnd,        // handle to window
    UINT uMsg,        // message identifier
    WPARAM wParam,    // first message parameter
    LPARAM lParam)    // second message parameter
{ 
 
    switch (uMsg) 
    { 
        case WM_CREATE: 
            // Initialize the window. 
            return 0; 
 
        case WM_PAINT: 
            // Paint the window's client area. 
            return 0; 
 
        case WM_SIZE: 
            // Set the size and position of the window. 
            return 0; 
 
        case WM_DESTROY: 
            // Clean up window-specific data objects. 
            return 0; 
 
        // 
        // Process other messages. 
        // 
 
        default: 
            return DefWindowProc(hwnd, uMsg, wParam, lParam); 
    } 
    return 0; 
} 
```



The [**WM\_NCCREATE**](wm-nccreate.md) message is sent just after your window is created, but if an application responds to this message by returning **FALSE**, [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function fails. The [**WM\_CREATE**](wm-create.md) message is sent after your window is already created.

The [**WM\_DESTROY**](wm-destroy.md) message is sent when your window is about to be destroyed. The [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function takes care of destroying any child windows of the window being destroyed. The [**WM\_NCDESTROY**](wm-ncdestroy.md) message is sent just before a window is destroyed.

At the very least, a window procedure should process the [**WM\_PAINT**](../gdi/wm-paint.md) message to draw itself. Typically, it should handle mouse and keyboard messages as well. Consult the descriptions of individual messages to determine whether your window procedure should handle them.

Your application can call the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function as part of the processing of a message. In such a case, the application can modify the message parameters before passing the message to **DefWindowProc**, or it can continue with the default processing after performing its own operations.

A dialog box procedure receives a [**WM\_INITDIALOG**](../dlgbox/wm-initdialog.md) message instead of a [**WM\_CREATE**](wm-create.md) message and does not pass unprocessed messages to the [**DefDlgProc**](/windows/win32/api/winuser/nf-winuser-defdlgprocw) function. Otherwise, a dialog box procedure is exactly the same as a window procedure.

## Associating a Window Procedure with a Window Class

You associate a window procedure with a window class when registering the class. You must fill a [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure with information about the class, and the **lpfnWndProc** member must specify the address of the window procedure. To register the class, pass the address of **WNDCLASS** structure to the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa) function. After the window class has been registered, the window procedure is automatically associated with each new window created with that class.

The following example shows how to associate the window procedure in the previous example with a window class.


```
int APIENTRY WinMain( 
    HINSTANCE hinstance,  // handle to current instance 
    HINSTANCE hinstPrev,  // handle to previous instance 
    LPSTR lpCmdLine,      // address of command-line string 
    int nCmdShow)         // show-window type 
{ 
    WNDCLASS wc; 
 
    // Register the main window class. 
    wc.style = CS_HREDRAW | CS_VREDRAW; 
    wc.lpfnWndProc = (WNDPROC) MainWndProc; 
    wc.cbClsExtra = 0; 
    wc.cbWndExtra = 0; 
    wc.hInstance = hinstance; 
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION); 
    wc.hCursor = LoadCursor(NULL, IDC_ARROW); 
    wc.hbrBackground = GetStockObject(WHITE_BRUSH); 
    wc.lpszMenuName =  "MainMenu"; 
    wc.lpszClassName = "MainWindowClass"; 
 
    if (!RegisterClass(&wc)) 
       return FALSE; 
 
    // 
    // Process other messages. 
    // 
 
} 
```



## Subclassing a Window

To subclass an instance of a window, call the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function and specify the handle to the window to subclass the GWL\_WNDPROC flag and a pointer to the subclass procedure. **SetWindowLong** returns a pointer to the original window procedure; use this pointer to pass messages to the original procedure. The subclass window procedure must use the [**CallWindowProc**](/windows/win32/api/winuser/nf-winuser-callwindowproca) function to call the original window procedure.

> [!Note]  
> To write code that is compatible with both 32-bit and 64-bit versions of Windows, use the [**SetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-setwindowlongptra) function.

 

The following example shows how to subclass an instance of an edit control in a dialog box. The subclass window procedure enables the edit control to receive all keyboard input, including the ENTER and TAB keys, whenever the control has the input focus.


```
WNDPROC wpOrigEditProc; 
 
LRESULT APIENTRY EditBoxProc(
    HWND hwndDlg, 
    UINT uMsg, 
    WPARAM wParam, 
    LPARAM lParam) 
{ 
    HWND hwndEdit; 
 
    switch(uMsg) 
    { 
        case WM_INITDIALOG: 
            // Retrieve the handle to the edit control. 
            hwndEdit = GetDlgItem(hwndDlg, ID_EDIT); 
 
            // Subclass the edit control. 
            wpOrigEditProc = (WNDPROC) SetWindowLong(hwndEdit, 
                GWL_WNDPROC, (LONG) EditSubclassProc); 
            // 
            // Continue the initialization procedure. 
            // 
            return TRUE; 
 
        case WM_DESTROY: 
            // Remove the subclass from the edit control. 
            SetWindowLong(hwndEdit, GWL_WNDPROC, 
                (LONG) wpOrigEditProc); 
            // 
            // Continue the cleanup procedure. 
            // 
            break; 
    } 
    return FALSE; 
        UNREFERENCED_PARAMETER(lParam); 
} 
 
// Subclass procedure 
LRESULT APIENTRY EditSubclassProc(
    HWND hwnd, 
    UINT uMsg, 
    WPARAM wParam, 
    LPARAM lParam) 
{ 
    if (uMsg == WM_GETDLGCODE) 
        return DLGC_WANTALLKEYS; 
 
    return CallWindowProc(wpOrigEditProc, hwnd, uMsg, 
        wParam, lParam); 
} 
```



 

 
