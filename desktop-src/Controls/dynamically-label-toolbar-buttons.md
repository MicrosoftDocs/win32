---
title: How to Dynamically Label Toolbar Buttons
description: You can assign text to an existing button by using the TB\_SETBUTTONINFO message.
ms.assetid: 571C7FB9-2806-47AF-8933-0D3541AE6ACF
ms.topic: article
ms.date: 05/31/2018
---

# How to Dynamically Label Toolbar Buttons

You can assign text to an existing button by using the [**TB\_SETBUTTONINFO**](tb-setbuttoninfo.md) message.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Dynamically Label a Toolbar Button

The following example demonstrates how to change the text of the third button in the previous examples from **Save** to **Save As**.


```C++
LRESULT RelabelButton(HWND hWndToolbar)
{
    TBBUTTONINFO tbInfo;
    
    tbInfo.cbSize  = sizeof(TBBUTTONINFO);
    tbInfo.dwMask  = TBIF_TEXT;
    tbInfo.pszText = L"Save As";
    
    return SendMessage(hWndToolbar, TB_SETBUTTONINFO, (WPARAM)IDM_SAVE, (LPARAM)&tbInfo);
}
```



## Remarks

Changing a button's text by using [**TB\_SETBUTTONINFO**](tb-setbuttoninfo.md) does not affect the string that is assigned to that button in the internal string list.

If you add a toolbar button string to the internal text list, you cannot retrieve the index of that string by calling [TBN\_GETBUTTONINFO](tbn-getbuttoninfo.md)—you must use the [**TB\_GETBUTTON**](tb-getbutton.md) message instead.

## Related topics

<dl> <dt>

[Using Toolbar Controls](using-toolbar-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




