---
title: Getting Started with Windows Touch Gestures
description: This section describes the basic steps for using multitouch gestures.
ms.assetid: 0ffe222a-a0ac-498b-a4ca-85cfb1caba93
keywords:
- Windows Touch,gestures
- Windows Touch,messages
- gestures,about
- gestures,messages
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with Windows Touch Gestures

This section describes the basic steps for using multitouch gestures.

The following steps are typically performed when using Windows Touch gestures:

1.  Set up a window for receiving gestures.
2.  Handle the gesture messages.
3.  Interpret the gesture messages.

## Setting up a Window to Receive Gestures

By default, you receive [**WM\_GESTURE**](wm-gesture.md) messages.

> [!Note]  
> If you call [**RegisterTouchWindow**](/windows/desktop/api/winuser/nf-winuser-registertouchwindow), you will stop receiving [**WM\_GESTURE**](wm-gesture.md) messages. If you are not receiving **WM\_GESTURE** messages, make sure that you haven't called **RegisterTouchWindow**.

 

The following code shows a simple InitInstance implementation.


```C++
#include <windows.h>


BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   HWND hWnd;

   hInst = hInstance; // Store instance handle in our global variable

   hWnd = CreateWindow(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL, NULL, hInstance, NULL);

   if (!hWnd)
   {
      return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}
```



## Handling Gesture Messages

Similar to handling Windows Touch input messages, you can handle gesture messages in many ways. If you are using Win32, you can check for the [**WM\_GESTURE**](wm-gesture.md) message in WndProc. If you are creating another type of application, you can add the **WM\_GESTURE** message to the message map and then implement a custom handler.

The following code shows how gesture messages could be handled.


```C++
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;
    PAINTSTRUCT ps;
    HDC hdc;

    switch (message)
    {    
    case WM_GESTURE:
            // Insert handler code here to interpret the gesture.            
            return DecodeGesture(hWnd, message, wParam, lParam);            
```



## Interpreting the Gesture Messages

The [**GetGestureInfo**](/windows/desktop/api/winuser/nf-winuser-getgestureinfo) function is used to interpret a gesture message into a structure describing the gesture. The structure, [**GESTUREINFO**](/windows/win32/api/winuser/ns-winuser-gestureinfo), has information about the gesture such as the location where the gesture was performed and the type of gesture. The following code shows how you can retrieve and interpret a gesture message.


```C++
  LRESULT DecodeGesture(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam){
    // Create a structure to populate and retrieve the extra message info.
    GESTUREINFO gi;  
    
    ZeroMemory(&gi, sizeof(GESTUREINFO));
    
    gi.cbSize = sizeof(GESTUREINFO);

    BOOL bResult  = GetGestureInfo((HGESTUREINFO)lParam, &gi);
    BOOL bHandled = FALSE;

    if (bResult){
        // now interpret the gesture
        switch (gi.dwID){
           case GID_ZOOM:
               // Code for zooming goes here     
               bHandled = TRUE;
               break;
           case GID_PAN:
               // Code for panning goes here
               bHandled = TRUE;
               break;
           case GID_ROTATE:
               // Code for rotation goes here
               bHandled = TRUE;
               break;
           case GID_TWOFINGERTAP:
               // Code for two-finger tap goes here
               bHandled = TRUE;
               break;
           case GID_PRESSANDTAP:
               // Code for roll over goes here
               bHandled = TRUE;
               break;
           default:
               // A gesture was not recognized
               break;
        }
    }else{
        DWORD dwErr = GetLastError();
        if (dwErr > 0){
            //MessageBoxW(hWnd, L"Error!", L"Could not retrieve a GESTUREINFO structure.", MB_OK);
        }
    }
    if (bHandled){
        return 0;
    }else{
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
  }
```



## Related topics

<dl> <dt>

[Windows Touch Gestures](guide-multi-touch-gestures.md)
</dt> </dl>

 

 




