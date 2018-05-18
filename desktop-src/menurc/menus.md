---
title: Menus
description: This section discusses menus.
ms.assetid: 'fd0b26f1-93cd-421b-9097-8502ab7681e9'
keywords: ["resources,menus", "menus,about"]
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
| [**AppendMenu**](appendmenu.md)                                 | Appends a new item to the end of the specified menu bar, drop-down menu, submenu, or shortcut menu. You can use this function to specify the content, appearance, and behavior of the menu item. <br/>                                                                                                                                                                                                  |
| [**CheckMenuItem**](checkmenuitem.md)                           | Sets the state of the specified menu item's check-mark attribute to either selected or clear.<br/>                                                                                                                                                                                                                                                                                                      |
| [**CheckMenuRadioItem**](checkmenuradioitem.md)                 | Checks a specified menu item and makes it a radio item. At the same time, the function clears all other menu items in the associated group and clears the radio-item type flag for those items.<br/>                                                                                                                                                                                                    |
| [**CreateMenu**](createmenu.md)                                 | Creates a menu. The menu is initially empty, but it can be filled with menu items by using the [**InsertMenuItem**](insertmenuitem.md), [**AppendMenu**](appendmenu.md), and [**InsertMenu**](insertmenu.md) functions. <br/>                                                                                                                                                                        |
| [**CreatePopupMenu**](createpopupmenu.md)                       | Creates a drop-down menu, submenu, or shortcut menu. The menu is initially empty. You can insert or append menu items by using the [**InsertMenuItem**](insertmenuitem.md) function. You can also use the [**InsertMenu**](insertmenu.md) function to insert menu items and the [**AppendMenu**](appendmenu.md) function to append menu items.<br/>                                                  |
| [**DeleteMenu**](deletemenu.md)                                 | Deletes an item from the specified menu. If the menu item opens a menu or submenu, this function destroys the handle to the menu or submenu and frees the memory used by the menu or submenu. <br/>                                                                                                                                                                                                     |
| [**DestroyMenu**](destroymenu.md)                               | Destroys the specified menu and frees any memory that the menu occupies. <br/>                                                                                                                                                                                                                                                                                                                          |
| [**DrawMenuBar**](drawmenubar.md)                               | Redraws the menu bar of the specified window. If the menu bar changes after the system has created the window, this function must be called to draw the changed menu bar. <br/>                                                                                                                                                                                                                         |
| [**EnableMenuItem**](enablemenuitem.md)                         | Enables, disables, or grays the specified menu item. <br/>                                                                                                                                                                                                                                                                                                                                              |
| [**EndMenu**](endmenu.md)                                       | Ends the calling thread's active menu.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**GetMenu**](getmenu.md)                                       | Retrieves a handle to the menu assigned to the specified window. <br/>                                                                                                                                                                                                                                                                                                                                  |
| [**GetMenuBarInfo**](getmenubarinfo.md)                         | Retrieves information about the specified menu bar.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**GetMenuCheckMarkDimensions**](getmenucheckmarkdimensions.md) | Retrieves the dimensions of the default check-mark bitmap. The system displays this bitmap next to selected menu items. Before calling the [**SetMenuItemBitmaps**](setmenuitembitmaps.md) function to replace the default check-mark bitmap for a menu item, an application must determine the correct bitmap size by calling [**GetMenuCheckMarkDimensions**](getmenucheckmarkdimensions.md). <br/> |
| [**GetMenuDefaultItem**](getmenudefaultitem.md)                 | Determines the default menu item on the specified menu.<br/>                                                                                                                                                                                                                                                                                                                                            |
| [**GetMenuInfo**](getmenuinfo.md)                               | Retrieves information about a specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**GetMenuItemCount**](getmenuitemcount.md)                     | Retrieves the number of items in the specified menu. <br/>                                                                                                                                                                                                                                                                                                                                              |
| [**GetMenuItemID**](getmenuitemid.md)                           | Retrieves the menu item identifier of a menu item located at the specified position in a menu. <br/>                                                                                                                                                                                                                                                                                                    |
| [**GetMenuItemInfo**](getmenuiteminfo.md)                       | Retrieves information about a menu item.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| [**GetMenuItemRect**](getmenuitemrect.md)                       | Retrieves the bounding rectangle for the specified menu item.<br/>                                                                                                                                                                                                                                                                                                                                      |
| [**GetMenuState**](getmenustate.md)                             | Retrieves the menu flags associated with the specified menu item. If the menu item opens a submenu, this function also returns the number of items in the submenu. <br/>                                                                                                                                                                                                                                |
| [**GetMenuString**](getmenustring.md)                           | Copies the text string of the specified menu item into the specified buffer. <br/>                                                                                                                                                                                                                                                                                                                      |
| [**GetSubMenu**](getsubmenu.md)                                 | Retrieves a handle to the drop-down menu or submenu activated by the specified menu item. <br/>                                                                                                                                                                                                                                                                                                         |
| [**GetSystemMenu**](getsystemmenu.md)                           | Enables the application to access the window menu (also known as the system menu or the control menu) for copying and modifying. <br/>                                                                                                                                                                                                                                                                  |
| [**HiliteMenuItem**](hilitemenuitem.md)                         | Highlights or removes the highlighting from an item in a menu bar. <br/>                                                                                                                                                                                                                                                                                                                                |
| [**InsertMenuItem**](insertmenuitem.md)                         | Inserts a new menu item at the specified position in a menu.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**IsMenu**](ismenu.md)                                         | Determines whether a handle is a menu handle. <br/>                                                                                                                                                                                                                                                                                                                                                     |
| [**LoadMenu**](loadmenu.md)                                     | Loads the specified menu resource from the executable (.exe) file associated with an application instance. <br/>                                                                                                                                                                                                                                                                                        |
| [**LoadMenuIndirect**](loadmenuindirect.md)                     | Loads the specified menu template in memory. <br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**MenuItemFromPoint**](menuitemfrompoint.md)                   | Determines which menu item, if any, is at the specified location.<br/>                                                                                                                                                                                                                                                                                                                                  |
| [**ModifyMenu**](modifymenu.md)                                 | Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item. <br/>                                                                                                                                                                                                                                                                           |
| [**RemoveMenu**](removemenu.md)                                 | Deletes a menu item or detaches a submenu from the specified menu. If the menu item opens a drop-down menu or submenu, [**RemoveMenu**](removemenu.md) does not destroy the menu or its handle, allowing the menu to be reused. Before this function is called, the [**GetSubMenu**](getsubmenu.md) function should retrieve a handle to the drop-down menu or submenu. <br/>                         |
| [**SetMenu**](setmenu.md)                                       | Assigns a new menu to the specified window. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**SetMenuDefaultItem**](setmenudefaultitem.md)                 | Sets the default menu item for the specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| [**SetMenuInfo**](setmenuinfo.md)                               | Sets information for a specified menu.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**SetMenuItemBitmaps**](setmenuitembitmaps.md)                 | Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item. <br/>                                                                                                                                                                                                                                   |
| [**SetMenuItemInfo**](setmenuiteminfo.md)                       | Changes information about a menu item.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**TrackPopupMenu**](trackpopupmenu.md)                         | Displays a shortcut menu at the specified location and tracks the selection of items on the menu. The shortcut menu can appear anywhere on the screen.<br/>                                                                                                                                                                                                                                             |
| [**TrackPopupMenuEx**](trackpopupmenuex.md)                     | Displays a shortcut menu at the specified location and tracks the selection of items on the shortcut menu. The shortcut menu can appear anywhere on the screen.<br/>                                                                                                                                                                                                                                    |



 

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
<td>[<strong>InsertMenu</strong>](insertmenu.md)</td>
<td>Inserts a new menu item into a menu, moving other items down the menu.
<blockquote>
[!Note]<br />
The [<strong>InsertMenu</strong>](insertmenu.md) function has been superseded by the [<strong>InsertMenuItem</strong>](insertmenuitem.md) function. You can still use <strong>InsertMenu</strong>, however, if you do not need any of the extended features of <strong>InsertMenuItem</strong>.
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
| [**MDINEXTMENU**](mdinextmenu.md)                         | Contains information about the menu to be activated. <br/>                                                                                                |
| [**MENUBARINFO**](menubarinfo.md)                         | Contains menu bar information.<br/>                                                                                                                       |
| [**MENUEX\_TEMPLATE\_HEADER**](menuex-template-header.md) | Defines the header for an extended menu template. This structure definition is for explanation only; it is not present in any standard header file. <br/> |
| [**MENUEX\_TEMPLATE\_ITEM**](menuex-template-item.md)     | Defines a menu item in an extended menu template. This structure definition is for explanation only; it is not present in any standard header file.<br/>  |
| [**MENUGETOBJECTINFO**](menugetobjectinfo.md)             | Contains information about the menu that the mouse cursor is on.<br/>                                                                                     |
| [**MENUINFO**](menuinfo.md)                               | Contains information about a menu.<br/>                                                                                                                   |
| [**MENUITEMINFO**](menuiteminfo.md)                       | Contains information about a menu item. <br/>                                                                                                             |
| [**MENUITEMTEMPLATE**](menuitemtemplate.md)               | Defines a menu item in a menu template. <br/>                                                                                                             |
| [**MENUITEMTEMPLATEHEADER**](menuitemtemplateheader.md)   | Defines the header for a menu template. A complete menu template consists of a header and one or more menu item lists. <br/>                              |
| [**TPMPARAMS**](tpmparams.md)                             | Contains extended parameters for the [**TrackPopupMenuEx**](trackpopupmenuex.md) function.<br/>                                                          |



 

 

 





