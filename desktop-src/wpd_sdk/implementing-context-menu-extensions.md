---
description: Implementing Context Menu Extensions
ms.assetid: b8bea667-b9ea-476d-942f-281cb2e9636c
title: Implementing Context Menu Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Context Menu Extensions

The WPD Namespace Extension supports extensible context (or shortcut) menus. These are the menus that appear when a user right-clicks on an object such as a file or a folder. Some WPD applications will take advantage of these extensible menus to support operations on device-side content (or objects that reside on the device).

Extensible context menus are supported by the interfaces described in the following table. For more information about any of these interfaces, see the Windows SDK.



| Interface           | Description                                                                                                                |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| IContextMenu        | The Windows Vista Shell calls the methods in this interface to create or merge the new context menu with the given object. |
| IDataObject         | Used to pass the context menu's PIDL array to the context menu handler.                                                    |
| IPropertySetStorage | This interface is used to retrieve WPD properties for the given object.                                                    |
| IPropertyStorage    | This interface is also used to retrieve WPD properties for the given object.                                               |
| IShellExtInit       | Initializes the Windows Vista Shell extensions for the context menu.                                                       |
| IStream             | To be supplied.                                                                                                            |



 

Context menus for WPD are implemented like any other context menu in Windows Vista. If you've already implemented a context menu handler, you can modify your existing code so that it supports device-side content. If you have never created a context menu handler, see the Creating Context Menu Handlers topic in the Windows SDK.

The two points at which a WPD context menu handler differs from any other handler is in the handler registration and the support of device-side content.

 

 



