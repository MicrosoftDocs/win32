---
Description: This topic lists the main programming elements used with shortcut (context) menus, and shortcut menu handlers. Shortcut menu handlers, which also known as context menu handlers or verb handlers, are a type of file type handler.
ms.assetid: efd96a52-6455-40bc-9c21-65f89728e771
title: Shortcut Menu Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**IContextMenu**](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master)         | Exposes methods that either create or merge a shortcut menu associated with a Shell object.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**IContextMenu2**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu2?branch=master)       | Exposes methods that either create or merge a shortcut (context) menu associated with a Shell object. Extends [**IContextMenu**](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master) by adding a method that allows client objects to handle messages associated with owner-drawn menu items.<br/>                                                                                                                                                                                                                                                    |
| [**IContextMenu3**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu3?branch=master)       | Exposes methods that either create or merge a shortcut menu associated with a Shell object. Allows client objects to handle messages associated with owner-drawn menu items and extends [**IContextMenu2**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu2?branch=master) by accepting a return value from that message handling.<br/>                                                                                                                                                                                                                         |
| [**IContextMenuCB**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenucb?branch=master)     | Exposes a method that enables the callback of a context menu. For example, to add a shield icon to a **menuItem** that requires elevation.<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| [**IContextMenuSite**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenusite?branch=master) | Implemented by the default folder view created using [**SHCreateShellFolderView**](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderview?branch=master). An implementation of [**IContextMenuSite**](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenusite?branch=master) supports [**IContextMenu::QueryContextMenu**](/windows/win32/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu?branch=master), [**IContextMenu::InvokeCommand**](/windows/win32/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand?branch=master), and [**TrackPopupMenu**](menurc.trackpopupmenu) and any message forwarding necessary for that function. **IContextMenuSite** typically updates the status bar as well.<br/> |



 

### Functions



| Topic                                                            | Contents                                                                                                                                |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**CDefFolderMenu\_Create2**](/windows/win32/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2?branch=master)        | Creates a context menu for a selected group of file folder objects.<br/>                                                          |
| [**LPFNDFMCALLBACK**](lpfndfmcallback.md)                       | Defines the prototype for the callback function that receives messages from the Shell's default context menu implementation.<br/> |
| [**SHCreateDefaultContextMenu**](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master) | Creates an object that represents the Shell's default context menu implementation.<br/>                                           |



 

### Structures



| Topic                                                  | Contents                                                                                                                                                                                                   |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CMINVOKECOMMANDINFO**](/windows/win32/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfo?branch=master)     | Contains information needed by [**IContextMenu::InvokeCommand**](/windows/win32/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand?branch=master) to invoke a shortcut menu command.<br/>                                                             |
| [**CMINVOKECOMMANDINFOEX**](/windows/win32/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfoex?branch=master) | Contains extended information about a shortcut menu command. This structure is an extended version of [**CMINVOKECOMMANDINFO**](/windows/win32/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfo?branch=master) that allows the use of Unicode values.<br/> |
| [**DEFCONTEXTMENU**](/windows/win32/shlobj_core/ns-shlobj_core-defcontextmenu?branch=master)               | Contains context menu information used by [**SHCreateDefaultContextMenu**](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master).<br/>                                                                                     |



 

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

 

 




