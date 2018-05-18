---
title: Finding and Loading Resources
description: This topic discusses how to load a resource into memory.
ms.assetid: '9e56cfdd-b365-4433-a507-a30220b4a92d'
---

# Finding and Loading Resources

Before using a resource, an application must load it into memory. The [**FindResource**](findresource.md) and [**FindResourceEx**](findresourceex.md) functions find a resource in a module and return a handle to the binary resource data. **FindResource** locates a resource by type and name. **FindResourceEx** locates the resource by type, name, and language. Information about **FindResource** in this topic also applies to **FindResourceEx**.

The [**LoadResource**](loadresource.md) function uses the resource handle returned by [**FindResource**](findresource.md) to load the resource into memory. After an application loads a resource by using **LoadResource**, the system will unload the associated memory only when all references to its module are freed through [**FreeLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms683152). Applications which need to repeatedly access the same or many resources within a particular module may incur performance penalties due to the memory mapping taking place in repeated [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and **FreeLibrary** calls. Applications should store a single module handle until resources are no longer needed, and then call **FreeLibrary**. After a module is unloaded from memory, resource handles become invalid.

An application can use [**FindResource**](findresource.md) and [**LoadResource**](loadresource.md) to find and load any type of resource, but these functions should be used only in one of these situations:

-   When the application cannot access the resource by using an existing resource-specific function.
-   When the application must access the resource as binary data for subsequent function calls.

Whenever possible, an application should instead use one of the following resource-specific functions to find and load resources in one call:



| Function                                     | Action                                   | To remove resource                                                                                               |
|----------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351)      | Loads and formats a message-table entry. | No action needed.                                                                                                |
| [**LoadAccelerators**](loadaccelerators.md) | Loads an accelerator table.              | [**DestroyAcceleratorTable**](destroyacceleratortable.md)                                                       |
| [**LoadBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd145033)             | Loads a bitmap resource.                 | [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)                                                                             |
| [**LoadCursor**](loadcursor.md)             | Loads a cursor resource.                 | [**DestroyCursor**](destroycursor.md)                                                                           |
| [**LoadIcon**](loadicon.md)                 | Loads an icon resource.                  | [**DestroyIcon**](destroyicon.md)                                                                               |
| [**LoadImage**](loadimage.md)               | Loads an icon, cursor, or bitmap.        | [**DestroyIcon**](destroyicon.md), [**DestroyCursor**](destroycursor.md), [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539) |
| [**LoadMenu**](loadmenu.md)                 | Loads a menu resource.                   | [**DestroyMenu**](destroymenu.md)                                                                               |
| [**LoadString**](loadstring.md)             | Loads a string-table entry.              | No action needed.                                                                                                |



 

Note the release functions in the table above. Before terminating, an application should release the memory occupied by accelerator tables, bitmaps, cursors, icons, and menus by using the appropriate functions.

Memory associated with resources loaded through [**FindResource**](findresource.md) and [**LoadResource**](loadresource.md) will be released once the module has been unloaded by a call to [**FreeLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms683152). Any resources which remain unloaded at application termination will be automatically released by the system.

 

 




