---
Description: 'This topic lists the main programming elements used with shortcut (context) menus, and shortcut menu handlers. Shortcut menu handlers, which also known as context menu handlers or verb handlers, are a type of file type handler.'
ms.assetid: 'efd96a52-6455-40bc-9c21-65f89728e771'
title: Shortcut Menu Reference
---

# Shortcut Menu Reference

This topic lists the main programming elements used with shortcut (context) menus, and shortcut menu handlers. Shortcut menu handlers, which also known as context menu handlers or verb handlers, are a type of file type handler.

## About Shortcut Menu Implemetation

It is strongly encouraged that you implement a shortcut menu using one of the static verb methods. Please review the following instructions:

-   To use a static verb method to implement a shortcut menu, see the "Customizing a Shortcut Menu using Static Verbs" section of [Creating Shortcut Menu Handlers](context-menu-handlers.md).
-   To get dynamic behavior for static verbs in Windows 7 and later, see "Getting Dynamic Behavior for Static Verbs" in [Creating Shortcut Menu Handlers](context-menu-handlers.md).
-   For details on static verb implementation, and which dynamic verbs to avoid, see [Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md).
-   If you must extend the shortcut menu for a file type by registering a dynamic verb for the file type, then follow the instructions provided in [Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md).

### Interfaces



| Topic                                        | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IContextMenu**](icontextmenu.md)         | Exposes methods that either create or merge a shortcut menu associated with a Shell object.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**IContextMenu2**](icontextmenu2.md)       | Exposes methods that either create or merge a shortcut (context) menu associated with a Shell object. Extends [**IContextMenu**](icontextmenu.md) by adding a method that allows client objects to handle messages associated with owner-drawn menu items.<br/>                                                                                                                                                                                                                                                    |
| [**IContextMenu3**](icontextmenu3.md)       | Exposes methods that either create or merge a shortcut menu associated with a Shell object. Allows client objects to handle messages associated with owner-drawn menu items and extends [**IContextMenu2**](icontextmenu2.md) by accepting a return value from that message handling.<br/>                                                                                                                                                                                                                         |
| [**IContextMenuCB**](icontextmenucb.md)     | Exposes a method that enables the callback of a context menu. For example, to add a shield icon to a **menuItem** that requires elevation.<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| [**IContextMenuSite**](icontextmenusite.md) | Implemented by the default folder view created using [**SHCreateShellFolderView**](shcreateshellfolderview.md). An implementation of [**IContextMenuSite**](icontextmenusite.md) supports [**IContextMenu::QueryContextMenu**](icontextmenu-querycontextmenu.md), [**IContextMenu::InvokeCommand**](icontextmenu-invokecommand.md), and [**TrackPopupMenu**](menurc.trackpopupmenu) and any message forwarding necessary for that function. **IContextMenuSite** typically updates the status bar as well.<br/> |



 

### Functions



| Topic                                                            | Contents                                                                                                                                |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**CDefFolderMenu\_Create2**](cdeffoldermenu-create2.md)        | Creates a context menu for a selected group of file folder objects.<br/>                                                          |
| [**LPFNDFMCALLBACK**](lpfndfmcallback.md)                       | Defines the prototype for the callback function that receives messages from the Shell's default context menu implementation.<br/> |
| [**SHCreateDefaultContextMenu**](shcreatedefaultcontextmenu.md) | Creates an object that represents the Shell's default context menu implementation.<br/>                                           |



 

### Structures



| Topic                                                  | Contents                                                                                                                                                                                                   |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CMINVOKECOMMANDINFO**](cminvokecommandinfo.md)     | Contains information needed by [**IContextMenu::InvokeCommand**](icontextmenu-invokecommand.md) to invoke a shortcut menu command.<br/>                                                             |
| [**CMINVOKECOMMANDINFOEX**](cminvokecommandinfoex.md) | Contains extended information about a shortcut menu command. This structure is an extended version of [**CMINVOKECOMMANDINFO**](cminvokecommandinfo.md) that allows the use of Unicode values.<br/> |
| [**DEFCONTEXTMENU**](defcontextmenu.md)               | Contains context menu information used by [**SHCreateDefaultContextMenu**](shcreatedefaultcontextmenu.md).<br/>                                                                                     |



 

## Related topics

<dl> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md)
</dt> <dt>

[Verbs and File Associations](fa-verbs.md)
</dt> <dt>

[Best Practices for Shortcut Menu Handlers and Multiple Selection Verbs](verbs-best-practices.md)
</dt> <dt>

[Creating Shortcut Menu Handlers](context-menu-handlers.md)
</dt> <dt>

[Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
</dt> </dl>

 

 




