---
title: How to Create a Date and Time Picker Control
description: This topic demonstrates how to dynamically create a date and time picker (DTP) control.
ms.assetid: D4ACA939-3004-48D3-ADD9-FC5E53128BA2
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Date and Time Picker Control

This topic demonstrates how to dynamically create a date and time picker (DTP) control. The accompanying C++ code example creates a DTP control in a modeless dialog box. It uses the [**DTS\_SHOWNONE**](date-and-time-picker-control-styles.md) style to enable the user to simulate deactivation of the date within the control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Step 1:

Register the window class by calling the [**InitCommonControlsEx**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrolsex) function and specifying the ICC\_DATE\_CLASSES bit in the accompanying [**INITCOMMONCONTROLSEX**](/windows/win32/api/commctrl/ns-commctrl-initcommoncontrolsex) structure.


```C++
 INITCOMMONCONTROLSEX icex;

 icex.dwSize = sizeof(icex);
 icex.dwICC = ICC_DATE_CLASSES;

 InitCommonControlsEx(&icex);
```



### Step 2:

To create the DTP control, use the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function. Specify [**DATETIMEPICK\_CLASS**](common-control-window-classes.md) as the window class, and pass the handle to the parent dialog box.

The following C++ code example uses the [**CreateDialog**](/windows/desktop/api/winuser/nf-winuser-createdialoga) function to create a modeless dialog box. It then calls **CreateWindowEx** to create the DTP control.


```C++
  hwndDlg = CreateDialog  (g_hinst,
                           MAKEINTRESOURCE(IDD_DIALOG1),
                           hwndMain,
                           DlgProc);

  if(hwndDlg)
      hwndDP = CreateWindowEx(0,
                           DATETIMEPICK_CLASS,
                           TEXT("DateTime"),
                           WS_BORDER|WS_CHILD|WS_VISIBLE|DTS_SHOWNONE,
                           20,50,220,20,
                           hwndDlg,
                           NULL,
                           g_hinst,
                           NULL);
```



## Complete example


```C++
//  CreateDatePick creates a DTP control within a dialog box.
//  Returns the handle to the new DTP control if successful, or NULL 
//  otherwise.
// 
//    hwndMain - The handle to the main window.
//    g_hinst  - global handle to the program instance.

HWND WINAPI CreateDatePick(HWND hwndMain)
{
    HWND hwndDP = NULL;
    HWND hwndDlg = NULL;

    INITCOMMONCONTROLSEX icex;

    icex.dwSize = sizeof(icex);
    icex.dwICC = ICC_DATE_CLASSES;

    InitCommonControlsEx(&icex);

    hwndDlg = CreateDialog  (g_hinst,
                             MAKEINTRESOURCE(IDD_DIALOG1),
                             hwndMain,
                             DlgProc);

    if(hwndDlg)
        hwndDP = CreateWindowEx(0,
                             DATETIMEPICK_CLASS,
                             TEXT("DateTime"),
                             WS_BORDER|WS_CHILD|WS_VISIBLE|DTS_SHOWNONE,
                             20,50,220,20,
                             hwndDlg,
                             NULL,
                             g_hinst,
                             NULL);

    return (hwndDP);
}

```



## Related topics

<dl> <dt>

[Using Date and Time Picker Controls](using-date-and-time-picker.md)
</dt> <dt>

[Date and Time Picker Control Reference](bumper-date-and-time-picker-date-and-time-picker-control-reference.md)
</dt> <dt>

[Date and Time Picker](date-and-time-picker-control-reference.md)
</dt> </dl>

 

 