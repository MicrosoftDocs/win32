---
title: How to Create a ComboBoxEx Control
description: This topic demonstrates how to create a ComboBoxEx control.
ms.assetid: E3D577AF-3290-431E-AA6C-1E9A9ED6448C
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a ComboBoxEx Control

This topic demonstrates how to create a ComboBoxEx control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


To create a ComboBoxEx control, call the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, using [**WC\_COMBOBOXEX**](common-control-window-classes.md) as the window class. You must first register the window class by calling the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function, while specifying the ICC\_USEREX\_CLASSES bit in the accompanying [**INITCOMMONCONTROLSEX**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) structure.

## Complete example

The following application-defined function creates a ComboBoxEx control with the [**CBS\_DROPDOWN**](combo-box-styles.md) style in the main window.


```C++
// CreateComboEx - Registers the ComboBoxEx window class and creates
// a ComboBoxEx control in the client area of the main window.
//
// g_hwndMain - A handle to the main window.
// g_hinst    - A handle to the program instance.
HWND WINAPI CreateComboEx(void)
{
    HWND hwnd;
    INITCOMMONCONTROLSEX icex;

    icex.dwSize = sizeof(INITCOMMONCONTROLSEX);
    icex.dwICC = ICC_USEREX_CLASSES;

    InitCommonControlsEx(&icex);

    hwnd = CreateWindowEx(0, WC_COMBOBOXEX, NULL,
                    WS_BORDER | WS_VISIBLE |
                    WS_CHILD | CBS_DROPDOWN,
                    // No size yet--resize after setting image list.
                    0,      // Vertical position of Combobox
                    0,      // Horizontal position of Combobox
                    0,      // Sets the width of Combobox
                    100,    // Sets the height of Combobox
                    g_hwndMain,
                    NULL,
                    g_hinst,
                    NULL);

    return (hwnd);
}
```



## Related topics

<dl> <dt>

[About ComboBoxEx Controls](comboboxex-controls.md)
</dt> <dt>

[ComboBoxEx Control Reference](bumper-comboboxex-comboboxex-control-reference.md)
</dt> <dt>

[Using ComboBoxEx Controls](/windows/desktop/Controls/using-comboboxex)
</dt> <dt>

[ComboBoxEx](comboboxex-control-reference.md)
</dt> </dl>

 

 