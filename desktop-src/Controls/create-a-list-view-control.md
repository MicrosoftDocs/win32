---
title: How to Create a List-View Control
description: This topic demonstrates how to create a list-view control. To create a list-view control, you use the CreateWindow or CreateWindowEx function and specify the WC\_LISTVIEW window class.
ms.assetid: FEAA0ACA-A086-46DF-9DD2-A3E32F2CCDA3
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a List-View Control

This topic demonstrates how to create a list-view control. To create a list-view control, you use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function and specify the [**WC\_LISTVIEW**](common-control-window-classes.md) window class.

A list-view control can also be created as part of a dialog box template. You must specify [**WC\_LISTVIEW**](common-control-window-classes.md) as the class name. To use a list-view control as part of a dialog box template, you must call [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols) or [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) before you create an instance of the dialog box.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


First register the window class by calling the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function and specifying the [**ICC\_LISTVIEW\_CLASSES**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) bit in the accompanying **INITCOMMONCONTROLSEX** structure. This ensures that the common controls DLL is loaded. Next, use the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function and specify the [**WC\_LISTVIEW**](common-control-window-classes.md) window class.

> [!Note]  
> By default, a list-view control uses the icon title font. However, you can use a [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont) message to specify the font to be used for the text. You should send this message before inserting any items. The control uses the dimensions of the font that is specified by the **WM\_SETFONT** message to determine spacing and layout. You can also customize the font for each item. For more information, see [Custom Draw](custom-draw.md).

 

The following C++ code example creates a list-view control in report view.


```C++
// CreateListView: Creates a list-view control in report view.
// Returns the handle to the new control
// TO DO:  The calling procedure should determine whether the handle is NULL, in case 
// of an error in creation.
//
// HINST hInst: The global handle to the applicadtion instance.
// HWND  hWndParent: The handle to the control's parent window. 
//
HWND CreateListView (HWND hwndParent) 
{
    INITCOMMONCONTROLSEX icex;           // Structure for control initialization.
    icex.dwICC = ICC_LISTVIEW_CLASSES;
    InitCommonControlsEx(&icex);

    RECT rcClient;                       // The parent window's client area.

    GetClientRect (hwndParent, &rcClient); 

    // Create the list-view window in report view with label editing enabled.
    HWND hWndListView = CreateWindow(WC_LISTVIEW, 
                                     L"",
                                     WS_CHILD | LVS_REPORT | LVS_EDITLABELS,
                                     0, 0,
                                     rcClient.right - rcClient.left,
                                     rcClient.bottom - rcClient.top,
                                     hwndParent,
                                     (HMENU)IDM_CODE_SAMPLES,
                                     g_hInst,
                                     NULL); 

    return (hWndListView);
}

```




Typically, list-view applications enable the user to change from one view to another.

The following C++ code example changes the list-view's window style, which in turn changes the view.


```C++
// SetView: Sets a list-view's window style to change the view.
// hWndListView: A handle to the list-view control. 
// dwView:       A value specifying the new view style.
//
VOID SetView(HWND hWndListView, DWORD dwView) 
{ 
    // Retrieve the current window style. 
    DWORD dwStyle = GetWindowLong(hWndListView, GWL_STYLE); 
    
    // Set the window style only if the view bits changed.
    if ((dwStyle & LVS_TYPEMASK) != dwView) 
    {
        SetWindowLong(hWndListView,
                      GWL_STYLE,
                      (dwStyle & ~LVS_TYPEMASK) | dwView);
    }               // Logical OR'ing of dwView with the result of 
}                   // a bitwise AND between dwStyle and 
                    // the Unary complenent of LVS_TYPEMASK.

```



## Related topics

<dl> <dt>

[List-View Control Reference](bumper-list-view-list-view-control-reference.md)
</dt> <dt>

[About List-View Controls](list-view-controls-overview.md)
</dt> <dt>

[Using List-View Controls](using-list-view-controls.md)
</dt> </dl>

 

 