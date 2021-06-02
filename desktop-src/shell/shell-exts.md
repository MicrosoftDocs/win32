---
description: This set of topics discusses how to implement the extension handlers that allow you to modify a variety of Shell actions.
ms.assetid: '794b6369-665f-49a9-a263-7c736c5ce8ac'
title: Working with Shell Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Working with Shell Extensions

The capabilities of the Shell can be extended with registry entries and .ini files. While this approach to extending the Shell is simple, and adequate for many purposes, it is limited. For example, if you use the registry to specify a custom icon for a file type, the same icon will appear for every file of that type. Extending the Shell with the registry does not allow you to vary the icon for different members of the file type. Other aspects of the Shell, such as the **Properties** property sheet that can be displayed when a file is right-clicked, cannot be modified at all with the registry.

A more powerful and flexible approach to extending the Shell is to implement *shell extension handlers*. These handlers can be implemented for a variety of actions that the Shell can take. Before taking the action, the Shell queries the extension handler, giving it the opportunity to modify the action. A common example is a shortcut menu extension handler. If one is implemented for a file type, it will be queried every time one of the files is right-clicked. The handler can then specify additional menu items on a file-by-file basis, rather than having the same set for all files of that file type.

This set of topics discusses how to implement the extension handlers that allow you to modify a variety of Shell actions. The following handlers are associated with a particular file type and allow you to specify on a file-by-file basis.



| Handler                                               | Description                                                                                                                                                                |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Shortcut menu handler](context-menu-handlers.md)    | Called before a file's shortcut menu is displayed. It enables you to add items to the shortcut menu on a file-by-file basis.                                               |
| [Data handler](how-to-create-data-handlers.md)       | Called when a drag-and-drop operation is performed on Shell objects. It enables you to provide additional clipboard formats to the drop target.                            |
| [Drop handler](how-to-create-drop-handlers.md)       | Called when a data object is dragged over or dropped on a file. It enables you to make a file into a drop target.                                                          |
| [Icon handler](how-to-create-icon-handlers.md)       | Called before a file's icon is displayed. It enables you to replace the file's default icon with a custom icon on a file-by-file basis.                                    |
| [Property sheet handler](propsheet-handlers.md)      | Called before an object's **Properties** property sheet is displayed. It enables you to add or replace pages.                                                              |
| [**Thumbnail Image handler**](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider) | Provides an image to represent the item.                                                                                                                                   |
| [**Infotip handler**](/windows/win32/api/shlobj_core/nn-shlobj_core-iqueryinfo)                 | Provides pop-up text when the user hovers the mouse pointer over the object.                                                                                               |
| [**Metadata handler**](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage)       | Provides read and write access to metadata (properties) stored in a file. This can be used to extend the Details view, infotips, the property page, and grouping features. |



 

Others are not associated with a particular file type but are called before some Shell operations.



| Handler                                                            | Description                                                                                                                                  |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Column handler](../lwef/column-handlers.md)                             | Called by Windows Explorer before it displays the Details view of a folder. It enables you to add custom columns to the Details view.        |
| [Copy hook handler](how-to-create-copy-hook-handlers.md)          | Called when a folder or printer object is about to be moved, copied, deleted, or renamed. It enables you to approve or veto the operation.   |
| [Drag-and-drop handler](context-menu-handlers.md)                 | Called when a file is dragged with the right mouse button. It enables you to modify the shortcut menu that is displayed.                     |
| [Icon Overlay handler](how-to-implement-icon-overlay-handlers.md) | Called before a file's icon is displayed. It enables you to specify an overlay for the file's icon.                                          |
| [Search handler](../lwef/search-handlers.md)                             | Called to launch a search engine. It enables you to implement a custom search engine accessible from the **Start** menu or Windows Explorer. |



 

The details of how to implement specific extension handlers are covered in the sections listed above. For discussions of implementation issues that are common to all Shell extension handlers, see these topics:

-   [Initializing Shell Extension Handlers](int-shell-exts.md)
-   [Registering Shell Extension Handlers](reg-shell-exts.md)

 

 
