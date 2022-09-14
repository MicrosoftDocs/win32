---
title: Finding and Loading Resources
description: This topic discusses how to load a resource into memory.
ms.assetid: 9e56cfdd-b365-4433-a507-a30220b4a92d
ms.topic: article
ms.date: 05/31/2018
---

# Finding and Loading Resources

Before using a resource, an application must load it into memory. The [**FindResource**](/windows/desktop/api/Winbase/nf-winbase-findresourcea) and [**FindResourceEx**](/windows/desktop/api/Winbase/nf-winbase-findresourceexa) functions find a resource in a module and return a handle to the binary resource data. **FindResource** locates a resource by type and name. **FindResourceEx** locates the resource by type, name, and language. Information about **FindResource** in this topic also applies to **FindResourceEx**.

The [**LoadResource**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadresource) function uses the resource handle returned by [**FindResource**](/windows/desktop/api/Winbase/nf-winbase-findresourcea) to load the resource into memory. After an application loads a resource by using **LoadResource**, the system will unload the associated memory only when all references to its module are freed through [**FreeLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-freelibrary). Applications which need to repeatedly access the same or many resources within a particular module may incur performance penalties due to the memory mapping taking place in repeated [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and **FreeLibrary** calls. Applications should store a single module handle until resources are no longer needed, and then call **FreeLibrary**. After a module is unloaded from memory, resource handles become invalid.

An application can use [**FindResource**](/windows/desktop/api/Winbase/nf-winbase-findresourcea) and [**LoadResource**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadresource) to find and load any type of resource, but these functions should be used only in one of these situations:

-   When the application cannot access the resource by using an existing resource-specific function.
-   When the application must access the resource as binary data for subsequent function calls.

Whenever possible, an application should instead use one of the following resource-specific functions to find and load resources in one call:



| Function                                     | Action                                   | To remove resource                                                                                               |
|----------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage)      | Loads and formats a message-table entry. | No action needed.                                                                                                |
| [**LoadAccelerators**](/windows/desktop/api/Winuser/nf-winuser-loadacceleratorsa) | Loads an accelerator table.              | [**DestroyAcceleratorTable**](/windows/desktop/api/Winuser/nf-winuser-destroyacceleratortable)                                                       |
| [**LoadBitmap**](/windows/desktop/api/winuser/nf-winuser-loadbitmapa)             | Loads a bitmap resource.                 | [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject)                                                                             |
| [**LoadCursor**](/windows/desktop/api/Winuser/nf-winuser-loadcursora)             | Loads a cursor resource.                 | [**DestroyCursor**](/windows/desktop/api/Winuser/nf-winuser-destroycursor)                                                                           |
| [**LoadIcon**](/windows/desktop/api/Winuser/nf-winuser-loadicona)                 | Loads an icon resource.                  | [**DestroyIcon**](/windows/desktop/api/Winuser/nf-winuser-destroyicon)                                                                               |
| [**LoadImage**](/windows/desktop/api/Winuser/nf-winuser-loadimagea)               | Loads an icon, cursor, or bitmap.        | [**DestroyIcon**](/windows/desktop/api/Winuser/nf-winuser-destroyicon), [**DestroyCursor**](/windows/desktop/api/Winuser/nf-winuser-destroycursor), [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject) |
| [**LoadMenu**](/windows/desktop/api/Winuser/nf-winuser-loadmenua)                 | Loads a menu resource.                   | [**DestroyMenu**](/windows/desktop/api/Winuser/nf-winuser-destroymenu)                                                                               |
| [**LoadString**](/windows/desktop/api/Winuser/nf-winuser-loadstringa)             | Loads a string-table entry.              | No action needed.                                                                                                |



 

Note the release functions in the table above. Before terminating, an application should release the memory occupied by accelerator tables, bitmaps, cursors, icons, and menus by using the appropriate functions.

Memory associated with resources loaded through [**FindResource**](/windows/desktop/api/Winbase/nf-winbase-findresourcea) and [**LoadResource**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadresource) will be released once the module has been unloaded by a call to [**FreeLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-freelibrary). Any resources which remain unloaded at application termination will be automatically released by the system.

 

 