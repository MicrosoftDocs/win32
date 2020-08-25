---
title: How to Create a Keyboard Interface for Standard Scroll Bars
description: Although a scroll bar control provides a built-in keyboard interface, a standard scroll bar does not.
ms.assetid: 249D0077-6E61-479A-91D5-A4BD9752B82E
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Keyboard Interface for Standard Scroll Bars

Although a scroll bar control provides a built-in keyboard interface, a standard scroll bar does not. To implement a keyboard interface for a standard scroll bar, a window procedure must process the [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) message and examine the virtual-key code specified by the *wParam* parameter. If the virtual-key code corresponds to an arrow key, the window procedure sends itself a [**WM\_HSCROLL**](wm-hscroll.md) or [**WM\_VSCROLL**](wm-vscroll.md) message with the low-order word of the *wParam* parameter set to the appropriate scroll bar request code.

For example, when the user presses the UP arrow key, the window procedure receives a [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) message with *wParam* equal to VK\_UP. In response, the window procedure sends itself a [**WM\_VSCROLL**](wm-vscroll.md) message with the low-order word of *wParam* set to the SB\_LINEUP request code.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Keyboard Interface for a Standard Scroll Bar

The following code example demonstrates how to include a keyboard interface for a standard scroll bar.


```C++
    case WM_KEYDOWN: 
    {
        WORD wScrollNotify = 0xFFFF;

        switch (wParam) 
        { 
            case VK_UP: 
                wScrollNotify = SB_LINEUP; 
                break; 
 
            case VK_PRIOR: 
                wScrollNotify = SB_PAGEUP; 
                break; 
 
            case VK_NEXT: 
                wScrollNotify = SB_PAGEDOWN; 
                break; 
 
            case VK_DOWN: 
                wScrollNotify = SB_LINEDOWN; 
                break; 
 
            case VK_HOME: 
                wScrollNotify = SB_TOP; 
                break; 
 
            case VK_END: 
                wScrollNotify = SB_BOTTOM; 
                break; 
        } 
 
        if (wScrollNotify != -1) 
            SendMessage(hwnd, WM_VSCROLL, MAKELONG(wScrollNotify, 0), 0L); 
 
        break; 
    }
```



## Related topics

<dl> <dt>

[Using Scroll Bars](using-scroll-bars.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 