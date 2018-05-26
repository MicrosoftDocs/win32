---
title: How to Create Rebar Controls
description: An application creates a rebar control by calling the CreateWindowEx function, specifying REBARCLASSNAME as the window class.
ms.assetid: F17CC2A4-BDC6-48A6-9AF5-19FCF65CC39A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Create Rebar Controls

An application creates a rebar control by calling the [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function, specifying [**REBARCLASSNAME**](common-control-window-classes.md#rebarclassname) as the window class. The application must first register the window class by calling the [**InitCommonControlsEx**](/windows/win32/Commctrl/nf-commctrl-initcommoncontrolsex?branch=master) function, specifying the ICC\_COOL\_CLASSES bit in the accompanying [**INITCOMMONCONTROLSEX**](/windows/win32/Commctrl/ns-commctrl-taginitcommoncontrolsex?branch=master) structure.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Rebar Control

The following example creates a rebar control with two bands—one that contains a combo box, and another one that contains a toolbar. (See the illustration in [About Rebar Controls](rebar-controls.md).) These controls are created separately, and are passed to the example function as parameters.


```C++
#define NUMBUTTONS 3

HWND CreateRebar(HWND hwndOwner, HWND hwndToolbar, HWND hwndCombo)
{
    // Check parameters.
    if ((hwndToolbar == NULL) || (hwndCombo == NULL))
    {
        return NULL;
    }

    // Initialize common controls.
    INITCOMMONCONTROLSEX icex;
    icex.dwSize = sizeof(INITCOMMONCONTROLSEX);
    icex.dwICC   = ICC_COOL_CLASSES | ICC_BAR_CLASSES;
    InitCommonControlsEx(&amp;icex);

    // Create the rebar.
    HWND hwndRebar = CreateWindowEx(WS_EX_TOOLWINDOW,
        REBARCLASSNAME,
        NULL,
        WS_CHILD | WS_VISIBLE | WS_CLIPSIBLINGS |
        WS_CLIPCHILDREN | RBS_VARHEIGHT |
        CCS_NODIVIDER | RBS_BANDBORDERS,
        0,0,0,0,
        hwndOwner,
        NULL,
        g_hInst, // global instance handle
        NULL);

    if(!hwndRebar)
    {
        return NULL;
    }

    // Initialize band info used by both bands.
    REBARBANDINFO rbBand = { sizeof(REBARBANDINFO) };
    rbBand.fMask  = 
          RBBIM_STYLE       // fStyle is valid.
        | RBBIM_TEXT        // lpText is valid.
        | RBBIM_CHILD       // hwndChild is valid.
        | RBBIM_CHILDSIZE   // child size members are valid.
        | RBBIM_SIZE;       // cx is valid
    rbBand.fStyle = RBBS_CHILDEDGE | RBBS_GRIPPERALWAYS;  

    // Get the height of the toolbar.
    DWORD dwBtnSize = (DWORD)SendMessage(hwndToolbar, TB_GETBUTTONSIZE, 0,0);

    // Set values unique to the band with the toolbar.
    rbBand.lpText = TEXT("");
    rbBand.hwndChild = hwndToolbar;
    rbBand.cyChild = LOWORD(dwBtnSize);
    rbBand.cxMinChild = NUMBUTTONS * HIWORD(dwBtnSize);
    rbBand.cyMinChild = LOWORD(dwBtnSize);
    // The default width is the width of the buttons.
    rbBand.cx = 0;

    // Add the band that has the toolbar.
    SendMessage(hwndRebar, RB_INSERTBAND, (WPARAM)-1, (LPARAM)&amp;rbBand);

    // Set values unique to the band with the combo box.
    RECT rc;
    GetWindowRect(hwndCombo, &amp;rc);
    rbBand.lpText = TEXT("Font");
    rbBand.hwndChild = hwndCombo;
    rbBand.cxMinChild = 0;
    rbBand.cyMinChild = rc.bottom - rc.top;
    // The default width should be set to some value wider than the text. The combo 
    // box itself will expand to fill the band.
    rbBand.cx = 100;

    // Add the band that has the combo box.
    SendMessage(hwndRebar, RB_INSERTBAND, (WPARAM)-1, (LPARAM)&amp;rbBand);
    
    return (hwndRebar);
}
```



## Related topics

<dl> <dt>

[Using Rebar Controls](using-rebar-controls.md)
</dt> <dt>

[About Rebar Controls](rebar-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](http://go.microsoft.com/fwlink/p/?linkid=214295)
</dt> </dl>

 

 




