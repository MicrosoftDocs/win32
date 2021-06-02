---
description: How to implement and register a drop handler.
title: How to Create Drop Handlers
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Drop Handlers

By default, files are not drop targets. You can make the members of a [file type](fa-file-types.md) into drop targets by implementing and registering a *drop handler*.

If a drop handler is registered for a file type, it is called whenever an object is dragged over or dropped on a member of the file type. The Shell manages the operation by calling the appropriate methods on the handler's [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface.

The general procedures for implementing and registering a Shell extension handler are discussed in [Creating Shell Extension Handlers](handlers.md). This document focuses on those aspects of implementation that are specific to drop handlers.

## Instructions

### Step 1: Implementing Drop Handlers

Like all Shell extension handlers, drop handlers are in-process Component Object Model (COM) objects implemented as DLLs. They export two interfaces in addition to [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown): [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) and [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget).

The Shell initializes the handler through its [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) interface. It uses this interface to request the handler's class identifier (CLSID) and provides it with the file's name. For a general discussion of how to implement Shell extension handlers, including the **IPersistFile** interface, see [Creating Shell Extension Handlers](handlers.md).

Once the drop handler is initialized, the Shell calls the appropriate method on the handler's [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface.

### Step 2: Registering Drop Handlers

Drop handlers are registered under this file type's subkey.

```
HKEY_CLASSES_ROOT
   ProgID
      shellex
         DropHandler
```

Create a subkey of **DropHandler** named for the handler, and set the subkey's default value to the string form of the handler's CLSID GUID. For a general discussion of how to register Shell extension handlers, see [Creating Shell Extension Handlers](handlers.md).

The following example illustrates registry entries that enable a drop handler for an example .myp file type.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   CLSID
      {00000000-1111-2222-3333-444444444444}
         InProcServer32
            (Default) = C:\MyDir\MyCommand.dll
            ThreadingModel = Apartment
   MyProgram.1
      (Default) = MyProgram Application
      shellex
         DropHandler
            (Default) = {00000000-1111-2222-3333-444444444444}
```

## Related topics

<dl> <dt>

[Creating Shell Extension Handlers](handlers.md)
</dt> <dt>

[**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget)
</dt> <dt>

[**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile)
</dt> </dl>

 

 
