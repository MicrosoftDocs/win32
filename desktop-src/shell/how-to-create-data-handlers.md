---
description: Extending the clipboard with custom data format handlers.
title: How to Create Data Handlers
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Data Handlers

When a file is copied to the clipboard or dragged and dropped, the Shell creates a data object that supports a variety of standard [clipboard formats](dragdrop.md). For files that are of a specific file type, you can extend the available clipboard formats by implementing and registering a *data handler*. When a file of the file type is transferred, the Shell delegates calls to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface to the data handler if one of the custom formats is used.

The general procedures for implementing and registering a Shell extension handler are discussed in [Creating Shell Extension Handlers](handlers.md). This document focuses on those aspects of implementation that are specific to data handlers.

-   [Implementing Data Handlers](#step-1-implementing-data-handlers)
-   [Registering Data Handlers](#step-2-registering-data-handlers)
-   [Related topics](#related-topics)

## Instructions

### Step 1: Implementing Data Handlers

Like all Shell extension handlers, data handlers are in-process Component Object Model (COM) objects implemented as DLLs. They export two interfaces in addition to [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown): [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) and [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject).

The Shell initializes the handler through its [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) interface. It uses this interface to request the handler's class identifier (CLSID) and provides it with the file's name. For a general discussion of how to implement Shell extension handlers, including the **IPersistFile** interface, see [Creating Shell Extension Handlers](handlers.md).

Once the data handler is initialized, the Shell delegates calls from the data object to the handler's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface if one of the custom formats is used.

### Step 2: Registering Data Handlers

Data handlers are registered under the file type's *ProgID* subkey as shown here: **HKEY\_CLASSES\_ROOT**\\*ProgID*\\**shellex**\\**DataHandler**

Create a subkey named for the handler under **DataHandler** and set the default value of that handler's subkey to the string form of the handler's CLSID GUID. For a general discussion of how to register Shell extension handlers, see [Creating Shell Extension Handlers](handlers.md).

The following example illustrates registry entries that enable a data handler for an example .myp file type.

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
      Shellex
         DataHandler
            (Default) = {00000000-1111-2222-3333-444444444444}
```

## Related topics

<dl> <dt>

[Creating Shell Extension Handlers](handlers.md)
</dt> <dt>

[**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile)
</dt> <dt>

[**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject)
</dt> </dl>

 

 
