---
title: Menus
description: This section discusses menus.
ms.assetid: fd0b26f1-93cd-421b-9097-8502ab7681e9
keywords:
- resources,menus
- menus,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Menus

This section describes menus and explains how to use them.

### In This Section



| Name                                 | Description                                                  |
|--------------------------------------|--------------------------------------------------------------|
| [About Menus](about-menus.md)       | Discusses menus.<br/>                                  |
| [Using Menus](using-menus.md)       | Provides code examples of tasks related to menus.<br/> |
| [Menu Reference](menu-reference.md) | Contains the API reference.<br/>                       |



 

### Menu Functions



| Name                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppendMenu**](/windows/win32/Winuser/nf-winuser-appendmenua?branch=master)                                 | Appends a new item to the end of the specified menu bar, drop-down menu, submenu, or shortcut menu. You can use this function to specify the content, appearance, and behavior of the menu item. <br/>                                                                                                                                                                                                  |
| [**CheckMenuItem**](/windows/win32/Winuser/nf-winuser-checkmenuitem?branch=master)                           | Sets the state of the specified menu item's check-mark attribute to either selected or clear.<br/>                                                                                                                                                                                                                                                                                                      |
| [**CheckMenuRadioItem**](/windows/win32/Winuser/nf-winuser-checkmenuradioitem?branch=master)                 | Checks a specified menu item and makes it a radio item. At the same time, the function clears all other menu items in the associated group and clears the radio-item type flag for those items.<br/>                                                                                                                                                                                                    |
| [**CreateMenu**](/windows/win32/Winuser/nf-winuser-createmenu?branch=master)                                 | Creates a menu. The menu is initially empty, but it can be filled with menu items by using the [**InsertMenuItem**](/windows/win32/Winuser/nf-winuser-insertmenuitema?branch=master), [**AppendMenu**](/windows/win32/Winuser/nf-winuser-appendmenua?branch=master), and [**InsertMenu**](/windows/win32/Winuser/nf-winuser-insertmenua?branch=master) functions. <br/>                                                                                                                                                                        |
| [**CreatePopupMenu**](/windows/win32/Winuser/nf-winuser-createpopupmenu?branch=master)                       | Creates a drop-down menu, submenu, or shortcut menu. The menu is initially empty. You can insert or append menu items by using the [**InsertMenuItem**](/windows/win32/Winuser/nf-winuser-insertmenuitema?branch=master) function. You can also use the [**InsertMenu**](/windows/win32/Winuser/nf-winuser-insertmenua?branch=master) function to insert menu items and the [**AppendMenu**](/windows/win32/Winuser/nf-winuser-appendmenua?branch=master) function to append menu items.<br/>                                                  |
| [**DeleteMenu**](/windows/win32/Winuser/nf-winuser-deletemenu?branch=master)                                 | Deletes an item from the specified menu. If the menu item opens a menu or submenu, this function destroys the handle to the menu or submenu and frees the memory used by the menu or submenu. <br/>                                                                                                                                                                                                     |
| [**DestroyMenu**](/windows/win32/Winuser/nf-winuser-destroymenu?branch=master)                               | Destroys the specified menu and frees any memory that the menu occupies. <br/>                                                                                                                                                                                                                                                                                                                          |
| [**DrawMenuBar**](/windows/win32/Winuser/nf-winuser-drawmenubar?branch=master)                               | Redraws the menu bar of the specified window. If the menu bar changes after the system has created the window, this function must be called to draw the changed menu bar. <br/>                                                                                                                                                                                                                         |
| [**EnableMenuItem**](/windows/win32/Winuser/nf-winuser-enablemenuitem?branch=master)                         | Enables, disables, or grays the specified menu item. <br/>                                                                                                                                                                                                                                                                                                                                              |
| [**EndMenu**](/windows/win32/Winuser/nf-winuser-endmenu?branch=master)                                       | Ends the calling thread's active menu.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**GetMenu**](/windows/win32/Winuser/nf-winuser-getmenu?branch=master)                                       | Retrieves a handle to the menu assigned to the specified window. <br/>                                                                                                                                                                                                                                                                                                                                  |
| [**GetMenuBarInfo**](/windows/win32/Winuser/nf-winuser-getmenubarinfo?branch=master)                         | Retrieves information about the specified menu bar.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**GetMenuCheckMarkDimensions**](/windows/win32/Winuser/nf-winuser-getmenucheckmarkdimensions?branch=master) | Retrieves the dimensions of the default check-mark bitmap. The system displays this bitmap next to selected menu items. Before calling the [**SetMenuItemBitmaps**](/windows/win32/Winuser/nf-winuser-setmenuitembitmaps?branch=master) function to replace the default check-mark bitmap for a menu item, an application must determine the correct bitmap size by calling [**GetMenuCheckMarkDimensions**](/windows/win32/Winuser/nf-winuser-getmenucheckmarkdimensions?branch=master). <br/> |
| [**GetMenuDefaultItem**](/windows/win32/Winuser/nf-winuser-getmenudefaultitem?branch=master)                 | Determines the default menu item on the specified menu.<br/>                                                                                                                                                                                                                                                                                                                                            |
| [**GetMenuInfo**](/windows/win32/Winuser/nf-winuser-getmenuinfo?branch=master)                               | Retrieves information about a specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**GetMenuItemCount**](/windows/win32/Winuser/nf-winuser-getmenuitemcount?branch=master)                     | Retrieves the number of items in the specified menu. <br/>                                                                                                                                                                                                                                                                                                                                              |
| [**GetMenuItemID**](/windows/win32/Winuser/nf-winuser-getmenuitemid?branch=master)                           | Retrieves the menu item identifier of a menu item located at the specified position in a menu. <br/>                                                                                                                                                                                                                                                                                                    |
| [**GetMenuItemInfo**](/windows/win32/Winuser/nf-winuser-getmenuiteminfoa?branch=master)                       | Retrieves information about a menu item.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| [**GetMenuItemRect**](/windows/win32/Winuser/nf-winuser-getmenuitemrect?branch=master)                       | Retrieves the bounding rectangle for the specified menu item.<br/>                                                                                                                                                                                                                                                                                                                                      |
| [**GetMenuState**](/windows/win32/Winuser/nf-winuser-getmenustate?branch=master)                             | Retrieves the menu flags associated with the specified menu item. If the menu item opens a submenu, this function also returns the number of items in the submenu. <br/>                                                                                                                                                                                                                                |
| [**GetMenuString**](/windows/win32/Winuser/nf-winuser-getmenustringa?branch=master)                           | Copies the text string of the specified menu item into the specified buffer. <br/>                                                                                                                                                                                                                                                                                                                      |
| [**GetSubMenu**](/windows/win32/Winuser/nf-winuser-getsubmenu?branch=master)                                 | Retrieves a handle to the drop-down menu or submenu activated by the specified menu item. <br/>                                                                                                                                                                                                                                                                                                         |
| [**GetSystemMenu**](/windows/win32/Winuser/nf-winuser-getsystemmenu?branch=master)                           | Enables the application to access the window menu (also known as the system menu or the control menu) for copying and modifying. <br/>                                                                                                                                                                                                                                                                  |
| [**HiliteMenuItem**](/windows/win32/Winuser/nf-winuser-hilitemenuitem?branch=master)                         | Highlights or removes the highlighting from an item in a menu bar. <br/>                                                                                                                                                                                                                                                                                                                                |
| [**InsertMenuItem**](/windows/win32/Winuser/nf-winuser-insertmenuitema?branch=master)                         | Inserts a new menu item at the specified position in a menu.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**IsMenu**](/windows/win32/Winuser/nf-winuser-ismenu?branch=master)                                         | Determines whether a handle is a menu handle. <br/>                                                                                                                                                                                                                                                                                                                                                     |
| [**LoadMenu**](/windows/win32/Winuser/nf-winuser-loadmenua?branch=master)                                     | Loads the specified menu resource from the executable (.exe) file associated with an application instance. <br/>                                                                                                                                                                                                                                                                                        |
| [**LoadMenuIndirect**](/windows/win32/Winuser/nf-winuser-loadmenuindirecta?branch=master)                     | Loads the specified menu template in memory. <br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**MenuItemFromPoint**](/windows/win32/Winuser/nf-winuser-menuitemfrompoint?branch=master)                   | Determines which menu item, if any, is at the specified location.<br/>                                                                                                                                                                                                                                                                                                                                  |
| [**ModifyMenu**](/windows/win32/Winuser/nf-winuser-modifymenua?branch=master)                                 | Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item. <br/>                                                                                                                                                                                                                                                                           |
| [**RemoveMenu**](/windows/win32/Winuser/nf-winuser-removemenu?branch=master)                                 | Deletes a menu item or detaches a submenu from the specified menu. If the menu item opens a drop-down menu or submenu, [**RemoveMenu**](/windows/win32/Winuser/nf-winuser-removemenu?branch=master) does not destroy the menu or its handle, allowing the menu to be reused. Before this function is called, the [**GetSubMenu**](/windows/win32/Winuser/nf-winuser-getsubmenu?branch=master) function should retrieve a handle to the drop-down menu or submenu. <br/>                         |
| [**SetMenu**](/windows/win32/Winuser/nf-winuser-setmenu?branch=master)                                       | Assigns a new menu to the specified window. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**SetMenuDefaultItem**](/windows/win32/Winuser/nf-winuser-setmenudefaultitem?branch=master)                 | Sets the default menu item for the specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**SetMenuInfo**](/windows/win32/Winuser/nf-winuser-setmenuinfo?branch=master)                               | Sets information for a specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**SetMenuItemBitmaps**](/windows/win32/Winuser/nf-winuser-setmenuitembitmaps?branch=master)                 | Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item. <br/>                                                                                                                                                                                                                                   |
| [**SetMenuItemInfo**](/windows/win32/Winuser/nf-winuser-setmenuiteminfoa?branch=master)                       | Changes information about a menu item.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**TrackPopupMenu**](/windows/win32/Winuser/nf-winuser-trackpopupmenu?branch=master)                         | Displays a shortcut menu at the specified location and tracks the selection of items on the menu. The shortcut menu can appear anywhere on the screen.<br/>                                                                                                                                                                                                                                             |
| [**TrackPopupMenuEx**](/windows/win32/Winuser/nf-winuser-trackpopupmenuex?branch=master)                     | Displays a shortcut menu at the specified location and tracks the selection of items on the shortcut menu. The shortcut menu can appear anywhere on the screen.<br/>                                                                                                                                                                                                                                    |



 

The following function is obsolete.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>InsertMenu</strong>](/windows/win32/Winuser/nf-winuser-insertmenua?branch=master)</td>
<td>Inserts a new menu item into a menu, moving other items down the menu.
<blockquote>
[!Note]<br />
The [<strong>InsertMenu</strong>](/windows/win32/Winuser/nf-winuser-insertmenua?branch=master) function has been superseded by the [<strong>InsertMenuItem</strong>](/windows/win32/Winuser/nf-winuser-insertmenuitema?branch=master) function. You can still use <strong>InsertMenu</strong>, however, if you do not need any of the extended features of <strong>InsertMenuItem</strong>.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

### Menu Notifications



| Name                                                  | Description                                                                                                                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_COMMAND**](wm-command.md)                     | Sent when the user selects a command item from a menu, when a control sends a notification message to its parent window, or when an accelerator keystroke is translated. <br/> |
| [**WM\_CONTEXTMENU**](wm-contextmenu.md)             | Informs a window that the user clicked the right mouse button (*right-clicked*) in the window.<br/>                                                                            |
| [**WM\_ENTERMENULOOP**](wm-entermenuloop.md)         | Informs an application's main window procedure that a menu modal loop has been entered. <br/>                                                                                  |
| [**WM\_EXITMENULOOP**](wm-exitmenuloop.md)           | Informs an application's main window procedure that a menu modal loop has been exited. <br/>                                                                                   |
| [**WM\_GETTITLEBARINFOEX**](wm-gettitlebarinfoex.md) | Sent to request extended title bar information. A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.<br/>                                  |
| [**WM\_MENUCOMMAND**](wm-menucommand.md)             | Sent when the user makes a selection from a menu. <br/>                                                                                                                        |
| [**WM\_MENUDRAG**](wm-menudrag.md)                   | Sent to the owner of a drag-and-drop menu when the user drags a menu item. <br/>                                                                                               |
| [**WM\_MENUGETOBJECT**](wm-menugetobject.md)         | Sent to the owner of a drag-and-drop menu when the mouse cursor enters a menu item or moves from the center of the item to the top or bottom of the item. <br/>                |
| [**WM\_MENURBUTTONUP**](wm-menurbuttonup.md)         | Sent when the user releases the right mouse button while the cursor is on a menu item. <br/>                                                                                   |
| [**WM\_NEXTMENU**](wm-nextmenu.md)                   | Sent to an application when the right or left arrow key is used to switch between the menu bar and the system menu. <br/>                                                      |
| [**WM\_UNINITMENUPOPUP**](wm-uninitmenupopup.md)     | Sent when a drop-down menu or submenu has been destroyed. <br/>                                                                                                                |



 

### Menu Structures



| Name                                                       | Description                                                                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MDINEXTMENU**](/windows/win32/Winuser/ns-winuser-tagmdinextmenu?branch=master)                         | Contains information about the menu to be activated. <br/>                                                                                                |
| [**MENUBARINFO**](/windows/win32/Winuser/ns-winuser-tagmenubarinfo?branch=master)                         | Contains menu bar information.<br/>                                                                                                                       |
| [**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md) | Defines the header for an extended menu template. This structure definition is for explanation only; it is not present in any standard header file. <br/> |
| [**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md)     | Defines a menu item in an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.<br/>  |
| [**MENUGETOBJECTINFO**](/windows/win32/Winuser/ns-winuser-tagmenugetobjectinfo?branch=master)             | Contains information about the menu that the mouse cursor is on.<br/>                                                                                     |
| [**MENUINFO**](/windows/win32/Winuser/ns-winuser-tagmenuinfo?branch=master)                               | Contains information about a menu.<br/>                                                                                                                   |
| [**MENUITEMINFO**](/windows/win32/Winuser/ns-winuser-tagmenuiteminfoa?branch=master)                       | Contains information about a menu item. <br/>                                                                                                             |
| [**MENUITEMTEMPLATE**](/windows/win32/Winuser/ns-winuser-menuitemtemplate?branch=master)               | Defines a menu item in a menu template. <br/>                                                                                                             |
| [**MENUITEMTEMPLATEHEADER**](/windows/win32/Winuser/ns-winuser-menuitemtemplateheader?branch=master)   | Defines the header for a menu template. A complete menu template consists of a header and one or more menu item lists. <br/>                              |
| [**TPMPARAMS**](/windows/win32/Winuser/ns-winuser-tagtpmparams?branch=master)                             | Contains extended parameters for the [**TrackPopupMenuEx**](/windows/win32/Winuser/nf-winuser-trackpopupmenuex?branch=master) function.<br/>                                                          |



 

 

 





