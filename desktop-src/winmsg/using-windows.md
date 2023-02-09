---
description: The examples in this section describe how to perform tasks associated with using windows.
ms.assetid: 7695fb64-3918-4d9a-8cd8-01d20edd9c55
title: Using Windows
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows

The examples in this section describe how to perform the following tasks:

-   [Creating a Main Window](#creating-a-main-window)
-   [Creating, Enumerating, and Sizing Child Windows](#creating-enumerating-and-sizing-child-windows)
-   [Destroying a Window](#destroying-a-window)
-   [Using Layered Windows](#using-layered-windows)

## Creating a Main Window

The first window an application creates is typically the main window. You create the main window by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function, specifying the window class, window name, window styles, size, position, menu handle, instance handle, and creation data. A main window belongs to an application-defined window class, so you must register the window class and provide a window procedure for the class before creating the main window.

Most applications typically use the [**WS\_OVERLAPPEDWINDOW**](window-styles.md) style to create the main window. This style gives the window a title bar, a window menu, a sizing border, and minimize and maximize buttons. The [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function returns a handle that uniquely identifies the window.

The following example creates a main window belonging to an application-defined window class. The window name, **Main Window**, will appear in the window's title bar. By combining the [**WS\_VSCROLL**](window-styles.md) and **WS\_HSCROLL** styles with the **WS\_OVERLAPPEDWINDOW** style, the application creates a main window with horizontal and vertical scroll bars in addition to the components provided by the **WS\_OVERLAPPEDWINDOW** style. The four occurrences of the **CW\_USEDEFAULT** constant set the initial size and position of the window to the system-defined default values. By specifying **NULL** instead of a menu handle, the window will have the menu defined for the window class.


```
HINSTANCE hinst; 
HWND hwndMain; 
 
// Create the main window. 
 
hwndMain = CreateWindowEx( 
    0,                      // no extended styles           
    "MainWClass",           // class name                   
    "Main Window",          // window name                  
    WS_OVERLAPPEDWINDOW |   // overlapped window            
             WS_HSCROLL |   // horizontal scroll bar        
             WS_VSCROLL,    // vertical scroll bar          
    CW_USEDEFAULT,          // default horizontal position  
    CW_USEDEFAULT,          // default vertical position    
    CW_USEDEFAULT,          // default width                
    CW_USEDEFAULT,          // default height               
    (HWND) NULL,            // no parent or owner window    
    (HMENU) NULL,           // class menu used              
    hinst,                  // instance handle              
    NULL);                  // no window creation data      
 
if (!hwndMain) 
    return FALSE; 
 
// Show the window using the flag specified by the program 
// that started the application, and send the application 
// a WM_PAINT message. 
 
ShowWindow(hwndMain, SW_SHOWDEFAULT); 
UpdateWindow(hwndMain); 
```



Notice that the preceding example calls the [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) function after creating the main window. This is done because the system does not automatically display the main window after creating it. By passing the **SW\_SHOWDEFAULT** flag to **ShowWindow**, the application allows the program that started the application to set the initial show state of the main window. The [**UpdateWindow**](/windows/win32/api/winuser/nf-winuser-updatewindow) function sends the window its first [**WM\_PAINT**](../gdi/wm-paint.md) message.

## Creating, Enumerating, and Sizing Child Windows

You can divide a window's client area into different functional areas by using child windows. Creating a child window is like creating a main window—you use the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. To create a window of an application-defined window class, you must register the window class and provide a window procedure before creating the child window. You must give the child window the [**WS\_CHILD**](window-styles.md) style and specify a parent window for the child window when you create it.

The following example divides the client area of an application's main window into three functional areas by creating three child windows of equal size. Each child window is the same height as the main window's client area, but each is one-third its width. The main window creates the child windows in response to the [**WM\_CREATE**](wm-create.md) message, which the main window receives during its own window-creation process. Because each child window has the [**WS\_BORDER**](window-styles.md) style, each has a thin line border. Also, because the **WS\_VISIBLE** style is not specified, each child window is initially hidden. Notice also that each child window is assigned a child-window identifier.

The main window sizes and positions the child windows in response to the [**WM\_SIZE**](wm-size.md) message, which the main window receives when its size changes. In response to **WM\_SIZE**, the main window retrieves the dimensions of its client area by using the [**GetClientRect**](/windows/win32/api/winuser/nf-winuser-getclientrect) function and then passes the dimensions to the [**EnumChildWindows**](/windows/win32/api/winuser/nf-winuser-enumchildwindows) function. **EnumChildWindows** passes the handle to each child window, in turn, to the application-defined [**EnumChildProc**](/previous-versions/windows/desktop/legacy/ms633493(v=vs.85)) callback function. This function sizes and positions each child window by calling the [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow) function; the size and position are based on the dimensions of the main window's client area and the identifier of the child window. Afterward, **EnumChildProc** calls the [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) function to make the window visible.


```
#define ID_FIRSTCHILD  100 
#define ID_SECONDCHILD 101 
#define ID_THIRDCHILD  102 
 
LONG APIENTRY MainWndProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) 
{ 
    RECT rcClient; 
    int i; 
 
    switch(uMsg) 
    { 
        case WM_CREATE: // creating main window  
 
            // Create three invisible child windows. 

            for (i = 0; i < 3; i++) 
            { 
                CreateWindowEx(0, 
                               "ChildWClass", 
                               (LPCTSTR) NULL, 
                               WS_CHILD | WS_BORDER, 
                               0,0,0,0, 
                               hwnd, 
                               (HMENU) (int) (ID_FIRSTCHILD + i), 
                               hinst, 
                               NULL); 
            }
 
            return 0; 
 
        case WM_SIZE:   // main window changed size 
 
            // Get the dimensions of the main window's client 
            // area, and enumerate the child windows. Pass the 
            // dimensions to the child windows during enumeration. 
 
            GetClientRect(hwnd, &rcClient); 
            EnumChildWindows(hwnd, EnumChildProc, (LPARAM) &rcClient); 
            return 0; 

        // Process other messages. 
    } 
    return DefWindowProc(hwnd, uMsg, wParam, lParam); 
} 
 
BOOL CALLBACK EnumChildProc(HWND hwndChild, LPARAM lParam) 
{ 
    LPRECT rcParent; 
    int i, idChild; 
 
    // Retrieve the child-window identifier. Use it to set the 
    // position of the child window. 
 
    idChild = GetWindowLong(hwndChild, GWL_ID); 
 
    if (idChild == ID_FIRSTCHILD) 
        i = 0; 
    else if (idChild == ID_SECONDCHILD) 
        i = 1; 
    else 
        i = 2; 
 
    // Size and position the child window.  
 
    rcParent = (LPRECT) lParam; 
    MoveWindow(hwndChild, 
               (rcParent->right / 3) * i, 
               0, 
               rcParent->right / 3, 
               rcParent->bottom, 
               TRUE); 
 
    // Make sure the child window is visible. 
 
    ShowWindow(hwndChild, SW_SHOW); 
 
    return TRUE;
}
```



## Destroying a Window

You can use the [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function to destroy a window. Typically, an application sends the [**WM\_CLOSE**](wm-close.md) message before destroying a window, giving the window the opportunity to prompt the user for confirmation before the window is destroyed. A window that includes a window menu automatically receives the **WM\_CLOSE** message when the user clicks **Close** from the window menu. If the user confirms that the window should be destroyed, the application calls **DestroyWindow**. The system sends the [**WM\_DESTROY**](wm-destroy.md) message to the window after removing it from the screen. In response to **WM\_DESTROY**, the window saves its data and frees any resources it allocated. A main window concludes its processing of **WM\_DESTROY** by calling the [**PostQuitMessage**](/windows/win32/api/winuser/nf-winuser-postquitmessage) function to quit the application.

The following example shows how to prompt for user confirmation before destroying a window. In response to [**WM\_CLOSE**](wm-close.md), the example displays a dialog box that contains **Yes**, **No**, and **Cancel** buttons. If the user clicks **Yes**, [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) is called; otherwise, the window is not destroyed. Because the window being destroyed is a main window, the example calls [**PostQuitMessage**](/windows/win32/api/winuser/nf-winuser-postquitmessage) in response to [**WM\_DESTROY**](wm-destroy.md).


```
case WM_CLOSE: 
 
    // Create the message box. If the user clicks 
    // the Yes button, destroy the main window. 
 
    if (MessageBox(hwnd, szConfirm, szAppName, MB_YESNOCANCEL) == IDYES) 
        DestroyWindow(hwndMain); 
    else 
        return 0; 
 
case WM_DESTROY: 
 
    // Post the WM_QUIT message to 
    // quit the application terminate. 
 
    PostQuitMessage(0); 
    return 0;
```



## Using Layered Windows

To have a dialog box come up as a translucent window, first create the dialog as usual. Then, on [**WM\_INITDIALOG**](../dlgbox/wm-initdialog.md), set the layered bit of the window's extended style and call [**SetLayeredWindowAttributes**](/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes) with the desired alpha value. The code might look like this:


```
// Set WS_EX_LAYERED on this window 
SetWindowLong(hwnd, 
              GWL_EXSTYLE, 
              GetWindowLong(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED);

// Make this window 70% alpha
SetLayeredWindowAttributes(hwnd, 0, (255 * 70) / 100, LWA_ALPHA);
```



Note that the third parameter of [**SetLayeredWindowAttributes**](/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes) is a value that ranges from 0 to 255, with 0 making the window completely transparent and 255 making it completely opaque. This parameter mimics the more versatile [**BLENDFUNCTION**](/windows/win32/api/wingdi/ns-wingdi-blendfunction) of the [**AlphaBlend**](/windows/win32/api/wingdi/nf-wingdi-alphablend) function.

To make this window completely opaque again, remove the **WS\_EX\_LAYERED** bit by calling [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) and then ask the window to repaint. Removing the bit is desired to let the system know that it can free up some memory associated with layering and redirection. The code might look like this:


```
// Remove WS_EX_LAYERED from this window styles
SetWindowLong(hwnd, 
              GWL_EXSTYLE,
              GetWindowLong(hwnd, GWL_EXSTYLE) & ~WS_EX_LAYERED);

// Ask the window and its children to repaint
RedrawWindow(hwnd, 
             NULL, 
             NULL, 
             RDW_ERASE | RDW_INVALIDATE | RDW_FRAME | RDW_ALLCHILDREN);
```



In order to use layered child windows, the application has to declare itself Windows 8-aware in the manifest.

For windows 10/11, one can include this compatibility snippet in its `app.manifest` to make it Windows 10-aware :
```
...
<compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">
    <application>
      <!-- Windows 10 GUID -->
      <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}" />
    </application>
</compatibility>
...
```
More about modifying app manifest can be read here :  [Application manifests](https://learn.microsoft.com/en-us/windows/win32/sbscs/application-manifests)
 

 
