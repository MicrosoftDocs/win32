---
title: How to Process Notification Messages
description: A property sheet sends WM\_NOTIFY messages to retrieve information from the pages and to notify the pages of user actions.
ms.assetid: 82768E43-97BA-451A-9373-D5B8FD06ABED
ms.topic: article
ms.date: 05/31/2018
---

# How to Process Notification Messages

A property sheet sends [**WM\_NOTIFY**](wm-notify.md) messages to retrieve information from the pages and to notify the pages of user actions.

The *lParam* parameter of the message is the address of an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure, which contains the handle to the property sheet dialog box, the handle to the page dialog box, and a notification code. The page must respond to some notification messages by setting the DWL\_MSGRESULT value of the page to either **TRUE** or **FALSE**.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Process Notification Messages

The following example is a code fragment from the dialog box procedure for a page. It shows how to process the [PSN\_HELP](psn-help.md) notification code.


```C++
case WM_NOTIFY:

    switch (((NMHDR FAR *) lParam)->code) 
    {
    case PSN_HELP:
        {
         
        char szBuf[FILE_LEN]; // Buffer for name of Help file

        // Display Help for the font properties page.
        LoadString(g_hinst, IDS_HELPFILE, &szBuf, sizeof(szBuf)/sizeof(szBuf[0]));
        WinHelp(((NMHDR FAR *)lParam)->hwndFrom, &szBuf, HELP_CONTEXT, IDH_FONT_PROPERTIES);                
        
        break;
        
         }
         
        // Process other property sheet notifications here.
    }
    
```



## Related topics

<dl> <dt>

[Using Property Sheets](using-property-sheets.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




