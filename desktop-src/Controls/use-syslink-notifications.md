---
title: How to Use SysLink Notifications
description: There are two notification messages associated with the SysLink control \ 8212;one for the mouse (NM\_CLICK (syslink)), and one for the keyboard (NM\_RETURN).
ms.assetid: 77E80EB2-180B-4EDD-9FB5-9930E8886CA6
ms.topic: article
ms.date: 05/31/2018
---

# How to Use SysLink Notifications

There are two notification messages associated with the SysLink control—one for the mouse ([NM\_CLICK (syslink)](nm-click-syslink.md)), and one for the keyboard ([NM\_RETURN](nm-return.md)).

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use SysLink Notifications

The following example code shows how to process the SysLink notifications that are generated when the user clicks either of the two links in the [previous example](create-syslink-controls.md). When the user clicks the Internet URL, the associated webpage opens in the default browser. When the user clicks the application-defined hyperlink, a message box is displayed.


```C++
// g_hLink is the handle of the SysLink control.
case WM_NOTIFY:

    switch (((LPNMHDR)lParam)->code)
    {
    
    case NM_CLICK:          // Fall through to the next case.
    
    case NM_RETURN:
        {
            PNMLINK pNMLink = (PNMLINK)lParam;
            LITEM   item    = pNMLink->item;
            
            if ((((LPNMHDR)lParam)->hwndFrom == g_hLink) && (item.iLink == 0))
              {
                ShellExecute(NULL, L"open", item.szUrl, NULL, NULL, SW_SHOW);
              }
            
            else if (wcscmp(item.szID, L"idInfo") == 0)
              {
                MessageBox(hDlg, L"This isn't much help.", L"Example", MB_OK);
              }
            
            break;
        }
    }
    
    break;
```



## Related topics

<dl> <dt>

[Using SysLink Controls](using-syslink-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://go.microsoft.com/fwlink/p/?linkid=214295)
</dt> </dl>

 

 




