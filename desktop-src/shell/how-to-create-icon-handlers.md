---
Description: Describes how to create a handler for custom icon assignments.
ms.assetid: 23ed3a21-cf62-4440-b983-fae23aa56890
title: How to Create Icon Handlers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Icon Handlers

A [file type](fa-file-types.md) often has a custom icon associated with it, to make its members easily recognizable in Windows Explorer. The simplest way to assign a custom icon to a file type is to register the icon's file. However, an icon registered in this way will be the same for all members of the file type. You can have much more flexibility in assigning icons to the members of the file type by implementing an *icon handler*.

An icon handler is a type of Shell extension handler that allows you to dynamically assign icons to the members of a file type. Every time a file of the type is displayed, the Shell queries the handler for the appropriate icon. For instance, an icon handler can assign different icons to different members of the file type, or vary the icon based on the current state of the file.

The general procedures for implementing and registering a Shell extension handler are discussed in [Creating Shell Extension Handlers](handlers.md). This document focuses on those aspects of implementation that are specific to icon handlers.

-   [Implementing Icon Handlers](#step-1-implementing-icon-handlers)
-   [Implementing the IExtractIcon Interface](#step-2-implementing-the-iextracticon-interface)
-   [Registering Icon Handlers](#step-3-registering-icon-handlers)
-   [Related topics](#related-topics)

## Instructions

### Step 1: Implementing Icon Handlers

Like all Shell extension handlers, icon handlers are in-process Component Object Model (COM) objects implemented as DLLs. They must export two interfaces in addition to [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332): [**IPersistFile**](https://msdn.microsoft.com/windows/desktop/7d34507f-8a16-43b4-8225-010798abc546) and [**IExtractIcon**](/windows/desktop/api/Shlobj_core/).

The Shell initializes the handler through its [**IPersistFile**](https://msdn.microsoft.com/windows/desktop/7d34507f-8a16-43b4-8225-010798abc546) interface. It uses this interface to request the handler's class identifier (CLSID) and provides it with the file's name. The rest of the operation takes place through the [**IExtractIcon**](/windows/desktop/api/Shlobj_core/) interface. For a general discussion of how to implement Shell extension handlers, including the **IPersistFile** interface, see [Creating Shell Extension Handlers](handlers.md). The remainder of this document discusses how to implement the **IExtractIcon** interface.

### Step 2: Implementing the IExtractIcon Interface

After the interface is initialized, the Shell uses the handler's [**IExtractIcon**](/windows/desktop/api/Shlobj_core/) interface to request the appropriate icon. The interface has two methods: [**IExtractIcon::GetIconLocation**](/windows/desktop/api/Shlobj_core/) and [**IExtractIcon::Extract**](/windows/desktop/api/Shlobj_core/).

Icons are identified by their location in the file system. The [**IExtractIcon::GetIconLocation**](/windows/desktop/api/Shlobj_core/) method is called to request this information. Set the *szIconFile* parameter to the file name. If there is more than one icon in the file, set *piIndex* to the icon's index. Assign appropriate values to the two flag variables. If you do not want to specify a file name, or if you do not want the Shell to extract the icon, set the **GIL\_NOTFILENAME** flag in the *pwFlags* parameter. You do not need to assign a value to *szIconFile*, but the handler must provide icon handles when the Shell calls [**IExtractIcon::Extract**](/windows/desktop/api/Shlobj_core/).

If you return a file name, the Shell normally attempts to load the icon from its cache. To prevent the loading of a cached icon, set the **GIL\_DONTCACHE** flag in the *pwFlags* parameter. If a cached icon is not loaded, the Shell then calls [**IExtractIcon::Extract**](/windows/desktop/api/Shlobj_core/) to request the icon handle.

If a file and index were specified by [**IExtractIcon::GetIconLocation**](/windows/desktop/api/Shlobj_core/), they are passed to [**IExtractIcon::Extract**](/windows/desktop/api/Shlobj_core/) in the *pszFile* and *nIconIndex* parameters, respectively. If a file name is provided, your handler can return S\_FALSE to have the Shell extract the icon. Otherwise, your handler must extract or otherwise produce large and small icons, and assign their HICON handles to the *phiconLarge* and *phiconSmall* parameters. The Shell adds the icons to its cache to expedite subsequent calls to the handler.

### Step 3: Registering Icon Handlers

When you [statically register an icon](icon.md) for a [file type](fa-file-types.md), you create a **DefaultIcon** subkey under the ProgID for the file type. Its default value is set to the file that contains the icon. To register an icon handler, you must still have the **DefaultIcon** subkey, but its default value must be set to "%1". Add an **IconHandler** subkey to the **Shellex** subkey of the ProgID subkey, and set its default value to the string form of the handler's CLSID GUID. For a general discussion of how to register Shell extension handlers, see [Creating Shell Extension Handlers](handlers.md).

The following example modifies the registry entry from [Customizing Icons](icon.md) so that the .myp file type now uses a shortcut menu handler instead of a statically defined icon.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   MyProgram.1
      (Default) = MyProgram Application
      DefaultIcon
         (Default) = %1
      Shellex
         IconHandler
            (Default) = {The handler's CLSID GUID}
```

## Related topics

<dl> <dt>

[Creating Shell Extension Handlers](handlers.md)
</dt> <dt>

[**IPersistFile**](https://msdn.microsoft.com/windows/desktop/7d34507f-8a16-43b4-8225-010798abc546)
</dt> <dt>

[**IExtractIcon**](/windows/desktop/api/Shlobj_core/)
</dt> </dl>

 

 



