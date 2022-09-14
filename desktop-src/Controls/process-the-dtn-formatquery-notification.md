---
title: How to Process the DTN_FORMATQUERY Notification
description: This topic demonstrates how to process a Format Query notification that is sent by the date and time picker (DTP) control.
ms.assetid: 74E29438-2F50-4ADD-B0C4-DB3450BF08D7
ms.topic: article
ms.date: 05/31/2018
---

# How to Process the DTN\_FORMATQUERY Notification

This topic demonstrates how to process a Format Query notification that is sent by the date and time picker (DTP) control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


A DTP control sends a [DTN\_FORMATQUERY](dtn-formatquery.md) notification code to request information about the maximum possible size of a callback field within the control. Your application must handle this message to ensure that all fields are displayed properly.

The following C++ code example is an application-defined function that processes the [DTN\_FORMATQUERY](dtn-formatquery.md) notification code by calculating the width of the widest possible string for a given callback field.

**Security Warning:** Using **lstrcmp** incorrectly can compromise the security of your application. For example, before calling **lstrcmp** in the following code example you should make sure the two strings are null-terminated. You should review [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.



```C++
//  DoFormatQuery processes DTN_FORMATQUERY messages to ensure that the
//  DTP control displays callback fields properly.
//

void WINAPI DoFormatQuery(
 HWND hwndDP, 
 LPNMDATETIMEFORMATQUERY lpDTFQuery)
{
    HDC hdc;
    HFONT hFont, hOrigFont;

    //  Prepare the device context for GetTextExtentPoint32 call.
    hdc = GetDC(hwndDP);

    hFont = (HFONT) SendMessage(hwndDP, WM_GETFONT, 0L, 0L); 

    if(!hFont)
        hFont = (HFONT)GetStockObject(DEFAULT_GUI_FONT);

    hOrigFont = (HFONT) SelectObject(hdc, hFont);

    // Check to see if this is the callback segment desired. If so,
    // use the longest text segment to determine the maximum 
    // width of the callback field, and then place the information into 
    // the NMDATETIMEFORMATQUERY structure.
    if(!lstrcmp(L"XX",lpDTFQuery->pszFormat))
        GetTextExtentPoint32 (hdc,
                          L"366",  // widest date string
                          3,
                          &lpDTFQuery->szMax);

    // Reset the font in the device context; then release the context.
    SelectObject(hdc,hOrigFont);
    ReleaseDC(hwndDP, hdc);
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

 

 




