---
Description: You use the BeginPaint and EndPaint functions to prepare for and complete the drawing in the client area.
ms.assetid: ed995bfd-a791-4d73-9a0b-daf65a9f7709
title: Drawing in the Client Area
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing in the Client Area

You use the [**BeginPaint**](/windows/win32/Winuser/nf-winuser-beginpaint?branch=master) and [**EndPaint**](/windows/win32/Winuser/nf-winuser-endpaint?branch=master) functions to prepare for and complete the drawing in the client area. **BeginPaint** returns a handle to the display device context used for drawing in the client area; **EndPaint** ends the paint request and releases the device context.

In the following example, the window procedure writes the message "Hello, Windows!" in the client area. To make sure the string is visible when the window is first created, the [**WinMain**](_win32_winmain_cpp) function calls [**UpdateWindow**](/windows/win32/Winuser/nf-winuser-updatewindow?branch=master) immediately after creating and showing the window. This causes a [**WM\_PAINT**](wm-paint.md) message to be sent immediately to the window procedure.


```C++
LRESULT APIENTRY WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam) 
{ 
    PAINTSTRUCT ps; 
    HDC hdc; 
 
    switch (message) 
    { 
        case WM_PAINT: 
            hdc = BeginPaint(hwnd, &amp;ps); 
            TextOut(hdc, 0, 0, "Hello, Windows!", 15); 
            EndPaint(hwnd, &amp;ps); 
            return 0L; 

        // Process other messages.   
    } 
} 
 
int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) 
{ 
    HWND hwnd; 
 
    hwnd = CreateWindowEx( 
        // parameters  
        ); 
 
    ShowWindow(hwnd, SW_SHOW); 
    UpdateWindow(hwnd); 
 
    return msg.wParam; 
} 
```



 

 



