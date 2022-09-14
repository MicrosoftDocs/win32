---
title: How to Use Pager Controls
description: This section describes how to implement the pager control in your application.
ms.assetid: 5703FE4B-987E-49DA-9741-F8B45AD26467
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Pager Controls

This section describes how to implement the pager control in your application.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Initialize a Pager Control

To use the pager control, you must call the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function with the ICC\_PAGESCROLLER\_CLASS flag set in the **dwICC** member of the [**INITCOMMONCONTROLSEX**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) structure.

### Create a Pager Control

Use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) API to create a pager control. The class name for the control is [**WC\_PAGESCROLLER**](common-control-window-classes.md), which is defined in Commctrl.h. The [**PGS\_HORZ**](pager-control-styles.md) style is used to create a horizontal pager, and the [**PGS\_VERT**](pager-control-styles.md) style is used to create a vertical pager. Because this is a child control, the [**WS\_CHILD**](/windows/desktop/winmsg/window-styles) style should also be used.

After the pager control is created, you will most likely want to assign a contained window to it. If the contained window is a child window, you should make the child window a child of the pager control so that the size and position will be calculated correctly. You then assign the window to the pager control with the [**PGM\_SETCHILD**](pgm-setchild.md) message. Be aware that this message does not actually change the parent window of the contained window; it simply assigns the contained window. If the contained window is one of the common controls, it must have the [**CCS\_NORESIZE**](common-control-styles.md) style to prevent the control from attempting to resize itself to the pager control's size.

### Process Pager Control Notifications

At a minimum, it is necessary to process the [PGN\_CALCSIZE](pgn-calcsize.md) notification. If you do not process this notification and enter a value for the width or height, the scroll arrows in the pager control will not be displayed. This is because the pager control uses the width or height supplied in the PGN\_CALCSIZE notification to determine the "ideal" size of the contained window.

The following example demonstrates how to process the [PGN\_CALCSIZE](pgn-calcsize.md) notification case. In this example, the contained window is a toolbar control that contains an unknown number of buttons at an unknown size. The example shows how to use the [**TB\_GETMAXSIZE**](tb-getmaxsize.md) message to determine the size of all of the items in the toolbar. The example then places the width of all of the items into the **iWidth** member of the [**NMPGCALCSIZE**](/windows/desktop/api/Commctrl/ns-commctrl-nmpgcalcsize) structure that is passed to the notification.


```C++
case PGN_SCROLL:{

    LPNMPGSCROLL pScroll = (LPNMPGSCROLL)lParam;
 
    switch(pScroll->iDir){
     
        case PGF_SCROLLLEFT:
        case PGF_SCROLLRIGHT:
        case PGF_SCROLLUP:
        case PGF_SCROLLDOWN:
     
            pScroll->iScroll = 20;
        
            break;
        }
    }
  
return 0;
```



## Related topics

<dl> <dt>

[Using Pager Controls](using-pager-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 