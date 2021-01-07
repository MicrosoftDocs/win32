---
description: Implementing Property Sheet Extensions
ms.assetid: 5d1f9d91-e8a1-4cbb-b1de-4262a61e3cb7
title: Implementing Property Sheet Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Property Sheet Extensions

The WPD Namespace Extension supports extensible property sheets. These are the property dialogs that appear when a user right-clicks on an object, such as a file or a folder, and selects **Properties**. Some WPD applications will take advantage of these extensible property sheets to display properties for device-side content (or objects that reside on the device).

Extensible property sheets are supported by the interfaces described in the following table. For more information about any of these interfaces, see the Windows SDK.



| Interface           | Description                                                                  |
|---------------------|------------------------------------------------------------------------------|
| IDataObject         | Used to pass the context menu's PIDL array to the context menu handler.      |
| IPropertySetStorage | This interface is used to retrieve WPD properties for the given object.      |
| IPropertyStorage    | This interface is also used to retrieve WPD properties for the given object. |
| IShellExtInit       | Initializes the Windows Vista Shell extensions for the context menu.         |
| IShellPropSheetExt  | Supports addition of property sheet extensions.                              |



 

Property sheets for WPD are implemented like any other property sheet in Windows Vista. If you've already implemented a property sheet handler, you can modify your existing code so that it supports device-side content. If you've never created a context menu handler, see the Creating Property Sheet Handlers topic in the Windows SDK.

The two points at which a WPD property sheet handler differs from any other handler is in the handler registration and the support of device-side content.

 

 



