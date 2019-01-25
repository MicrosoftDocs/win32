---
title: How to Create SysLink Controls
description: You implement the SysLink control's hyperlinks through markup in the control's initialization string, or by sending it a LM\_SETITEM message.
ms.assetid: CEE02A87-D85A-4F4D-931D-2B1371320814
ms.topic: article
ms.date: 05/31/2018
---

# How to Create SysLink Controls

You implement the SysLink control's hyperlinks through markup in the control's initialization string, or by sending it a [**LM\_SETITEM**](lm-setitem.md) message.

> [!Note]  
> Before creating SysLink controls, you must call the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function, specifying the ICC\_LINK\_CLASS.

 

To create a SysLink, call the [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) or [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function, specifying the [**WC\_LINK**](common-control-window-classes.md) window class. The *lpWindowName* parameter that is common to these functions specifies a pointer to a zero-terminated string that contains the marked-up text to display. For window styles particular to SysLink controls, see [SysLink Control Styles](syslink-control-styles.md).

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a SysLink Control

The following example code creates a SysLink control that displays two hyperlinks. The first hyperlink is an Internet URL, and the second is application-defined.


```C++
HWND CreateSysLink(HWND hDlg, HINSTANCE hInst, RECT rect)
{
    return CreateWindowEx(0, WC_LINK, 
        L"For more information, <A HREF=\"https://www.microsoft.com\">click here</A> " \
        L"or <A ID=\"idInfo\">here</A>.", 
        WS_VISIBLE | WS_CHILD | WS_TABSTOP, 
        rect.left, rect.top, rect.right, rect.bottom, 
        hDlg, NULL, hInst, NULL);
}
```



## Remarks

It is assumed that [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) has already been called.

Specifying the [**WS\_TABSTOP**](https://msdn.microsoft.com/library/windows/desktop/ms632600#ws-tabstop) style ensures that the user will be able to select a link by tabbing to it and pressing the Enter key.

Version 6 of ComCtl32.dll supports Unicode only. Therefore, you cannot create ANSI versions of SysLink controls—only Unicode.

## Related topics

<dl> <dt>

[Using SysLink Controls](https://msdn.microsoft.com/library/windows/desktop/hh270419)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://go.microsoft.com/fwlink/p/?linkid=214295)
</dt> </dl>

 

 




