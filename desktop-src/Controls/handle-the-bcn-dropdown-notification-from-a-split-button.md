---
title: Handle BCN_DROPDOWN notifications from SplitButtons
description: This topic describes one possible way of responding to the BCN\_DROPDOWN notification in a dialog procedure.
ms.assetid: 847DD645-AE29-4F62-BC32-F235BA409E1E
ms.topic: article
ms.date: 05/31/2018
---

# How to Handle the BCN\_DROPDOWN Notification from a Split Button

This topic describes one possible way of responding to the [BCN\_DROPDOWN](bcn-dropdown.md) notification in a dialog procedure.

The C++ application retrieves the client coordinates of the button from the notification header and converts them to screen coordinates. It then creates a popup menu and displays it at the bottom of the button. To keep the example simple, keyboard shortcuts are not implemented for the menu.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Step 1: Wait for the *BCN\_DROPDOWN* notification.


```C++
case BCN_DROPDOWN:
{
    NMBCDROPDOWN* pDropDown = (NMBCDROPDOWN*)lParam;
    if (pDropDown->hdr.hwndFrom = GetDlgItem(hDlg, IDC_SPLIT))
    {
```



### Step 2: Get the screen coordinates of the button.

Use the [**ClientToScreen**](/windows/desktop/api/winuser/nf-winuser-clienttoscreen) function to convert the window coordinates of the button's lower left edge to screen coordinates.


```C++
POINT pt;
pt.x = pDropDown->rcButton.left;
pt.y = pDropDown->rcButton.bottom;
ClientToScreen(pDropDown->hdr.hwndFrom, &pt);
```



### Step 3: Create a menu and add items.

Use the [**CreatePopupMenu**](/windows/desktop/api/winuser/nf-winuser-createpopupmenu) function to create a menu. Use the [**AppendMenu**](/windows/desktop/menurc/u) function to add items to the menu. IDC\_MENUCOMMAND1 and IDC\_MENUCOMMAND2 are application-defined constants for menu commands.


```C++
HMENU hSplitMenu = CreatePopupMenu();
AppendMenu(hSplitMenu, MF_BYPOSITION, IDC_MENUCOMMAND1, L"Menu item 1");
AppendMenu(hSplitMenu, MF_BYPOSITION, IDC_MENUCOMMAND2, L"Menu item 2");
```



### Step 4: Display the menu.

The [**TrackPopupMenu**](/windows/desktop/api/winuser/nf-winuser-trackpopupmenu) function displays a shortcut menu at the specified location and tracks the selection of items on the menu.


```C++
TrackPopupMenu(hSplitMenu, TPM_LEFTALIGN | TPM_TOPALIGN, pt.x, pt.y, 0, hDlg, NULL);
```



## Complete example


```C++
case WM_NOTIFY:
    switch (((LPNMHDR)lParam)->code)
    {
        case BCN_DROPDOWN:
        {
            NMBCDROPDOWN* pDropDown = (NMBCDROPDOWN*)lParam;
            if (pDropDown->hdr.hwndFrom = GetDlgItem(hDlg, IDC_SPLIT))
            {

                // Get screen coordinates of the button.
                POINT pt;
                pt.x = pDropDown->rcButton.left;
                pt.y = pDropDown->rcButton.bottom;
                ClientToScreen(pDropDown->hdr.hwndFrom, &pt);
        
                // Create a menu and add items.
                HMENU hSplitMenu = CreatePopupMenu();
                AppendMenu(hSplitMenu, MF_BYPOSITION, IDC_MENUCOMMAND1, L"Menu item 1");
                AppendMenu(hSplitMenu, MF_BYPOSITION, IDC_MENUCOMMAND2, L"Menu item 2");
        
                // Display the menu.
                TrackPopupMenu(hSplitMenu, TPM_LEFTALIGN | TPM_TOPALIGN, pt.x, pt.y, 0, hDlg, NULL);
                return TRUE;
            }
            break;
        }
    }
    return FALSE;
}
```



## Related topics

<dl> <dt>

[BCN\_DROPDOWN Notification Code](bcn-dropdown.md)
</dt> <dt>

[About Buttons](about-buttons.md)
</dt> <dt>

[Button Control Reference](bumper-button-button-control-reference.md)
</dt> <dt>

[Using Buttons](using-buttons.md)
</dt> <dt>

[Button](buttons.md)
</dt> </dl>

 

 