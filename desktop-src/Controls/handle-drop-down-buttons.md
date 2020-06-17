---
title: How to Handle Drop-down Buttons
description: A drop-down button can present users with a list of options.
ms.assetid: 2D908D4B-AA8B-4DEF-B656-C37B673ABB4D
ms.topic: article
ms.date: 05/31/2018
---

# How to Handle Drop-down Buttons

A drop-down button can present users with a list of options. To create this style of button, specify the [**BTNS\_DROPDOWN**](toolbar-control-and-button-styles.md) style (also called [**TBSTYLE\_DROPDOWN**](toolbar-control-and-button-styles.md) for compatibility with previous versions of the common controls). To show a drop-down button with an arrow, you must also set the [**TBSTYLE\_EX\_DRAWDDARROWS**](toolbar-extended-styles.md) toolbar style by sending a [**TB\_SETEXTENDEDSTYLE**](tb-setextendedstyle.md) message.

The following illustration shows a drop-down "Open" button with the context menu open and showing a list of files. In this example, the toolbar has the [**TBSTYLE\_EX\_DRAWDDARROWS**](toolbar-extended-styles.md) style.

![screen shot of a dialog box with three toolbar items represented by icons; one has an expanded drop-down arrow and a three-item context menu](images/tb-dropdown.png)

The following illustration shows the same toolbar, this time without the [**TBSTYLE\_EX\_DRAWDDARROWS**](toolbar-extended-styles.md) style.

![screen shot of a previous dialog box, but the icon with the context menu has no dropdown arrow](images/tb-dropdown2.png)

When users click a toolbar button that uses the [**BTNS\_DROPDOWN**](toolbar-control-and-button-styles.md) style, the toolbar control sends its parent window a [TBN\_DROPDOWN](tbn-dropdown.md) notification code.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Handle a Drop-down Button

The following code example demonstrates how an application can support a drop-down button in a toolbar control.


```C++
BOOL DoNotify(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{

    #define lpnm   ((LPNMHDR)lParam)
    #define lpnmTB ((LPNMTOOLBAR)lParam)

    switch(lpnm->code)
    {
        case TBN_DROPDOWN:
        {
            // Get the coordinates of the button.
            RECT rc;
            SendMessage(lpnmTB->hdr.hwndFrom, TB_GETRECT, (WPARAM)lpnmTB->iItem, (LPARAM)&rc);

            // Convert to screen coordinates.            
            MapWindowPoints(lpnmTB->hdr.hwndFrom, HWND_DESKTOP, (LPPOINT)&rc, 2);                         
        
            // Get the menu.
            HMENU hMenuLoaded = LoadMenu(g_hinst, MAKEINTRESOURCE(IDR_POPUP)); 
         
            // Get the submenu for the first menu item.
            HMENU hPopupMenu = GetSubMenu(hMenuLoaded, 0);

            // Set up the pop-up menu.
            // In case the toolbar is too close to the bottom of the screen, 
            // set rcExclude equal to the button rectangle and the menu will appear above 
            // the button, and not below it.
         
            TPMPARAMS tpm;
         
            tpm.cbSize    = sizeof(TPMPARAMS);
            tpm.rcExclude = rc;
         
            // Show the menu and wait for input. 
            // If the user selects an item, its WM_COMMAND is sent.
         
            TrackPopupMenuEx(hPopupMenu, 
                             TPM_LEFTALIGN | TPM_LEFTBUTTON | TPM_VERTICAL, 
                             rc.left, rc.bottom, g_hwndMain, &tpm);

            DestroyMenu(hMenuLoaded);
         
        return (FALSE);
      
        }
    }
   
    return FALSE;
}
```



## Related topics

<dl> <dt>

[Using Toolbar Controls](using-toolbar-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




