---
title: Menu Notifications
description: Menu Notifications
ms.assetid: 8ff5671e-a666-483c-9ac1-f8be6eb58ffa
ms.topic: article
ms.date: 05/31/2018
---

# Menu Notifications

## In This Section

-   [**WM\_COMMAND**](wm-command.md)
-   [**WM\_CONTEXTMENU**](wm-contextmenu.md)
-   [**WM\_ENTERMENULOOP**](wm-entermenuloop.md)
-   [**WM\_EXITMENULOOP**](wm-exitmenuloop.md)
-   [**WM\_GETTITLEBARINFOEX**](wm-gettitlebarinfoex.md)
-   [**WM\_MENUCOMMAND**](wm-menucommand.md)
-   [**WM\_MENUDRAG**](wm-menudrag.md)
-   [**WM\_MENUGETOBJECT**](wm-menugetobject.md)
-   [**WM\_MENURBUTTONUP**](wm-menurbuttonup.md)
-   [**WM\_NEXTMENU**](wm-nextmenu.md)
-   [**WM\_UNINITMENUPOPUP**](wm-uninitmenupopup.md)


## Example

```c
BOOL AboutDlg (
    HWND hDlg, 
    UINT message, 
    WPARAM wParam, 
    LPARAM lParam)
{
    BOOL bRet = FALSE;
    
    switch (message) 
    {
        case WM_INITDIALOG:
            bRet = TRUE;
            break;

        case WM_COMMAND:
            if (wParam == IDOK ||
                wParam == IDCANCEL) 
            {
                EndDialog(hDlg, TRUE);
                bRet = TRUE;
            }
            break;
    }

    return bRet;
}
```
Example taken from [Windows classic samples](https://github.com/microsoft/Windows-classic-samples) on GitHub.

 




