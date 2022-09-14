---
title: How to Process the DTN_DATETIMECHANGE Notification
description: This topic demonstrates how to process notification of changes, made by the user, to the date and time picker (DTP) control.
ms.assetid: AE029962-E9D3-47BC-A24F-312B54137F18
ms.topic: article
ms.date: 05/31/2018
---

# How to Process the DTN\_DATETIMECHANGE Notification

This topic demonstrates how to process notification of changes, made by the user, to the date and time picker (DTP) control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


A DTP control sends the [DTN\_DATETIMECHANGE](dtn-datetimechange.md) notification code whenever a change occurs. For example, this notification will be generated when the user changes one of the fields in the control or, in the case where the control is set to the [**DTS\_SHOWNONE**](date-and-time-picker-control-styles.md) style, when the user changes the state of the control's check box.

Your application must include code to process DTN\_DATETIMECHANGE messages that are sent by the DTP control.

The following C++ code example is an application-defined function designed to indicate the state of a DTP control that is set to the **DTS\_SHOWNONE** style.



```C++
void WINAPI DoDateTimeChange(LPNMDATETIMECHANGE lpChange)
{
    // If the user has unchecked the DTP's check box, change the
    // text in a static control to show the appropriate message.
    //
    // g_hwndDlg - a program-global address of a dialog box.

    if(lpChange->dwFlags == GDT_NONE)
        SetDlgItemText(g_hwndDlg, IDC_STATUS, L"Disabled");
    else
        SetDlgItemText(g_hwndDlg, IDC_STATUS, L"Active");
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

 

 




