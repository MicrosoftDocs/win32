---
description: Using Shell extensions to implement a copy hook handler.
ms.assetid: 05808281-84fb-402d-9fa1-3a747b29d030
title: How to Create Copy Hook Handlers
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Copy Hook Handlers

The general procedures for implementing and registering a Shell extension handler are discussed in [Creating Shell Extension Handlers](handlers.md). This document focuses on those aspects of implementation that are specific to copy hook handlers.

- [Implementing Copy Hook Handlers](#step-1-implementing-copy-hook-handlers)
- [Registering Copy Hook Handlers](#step-2-registering-copy-hook-handlers)
- [Related topics](#related-topics)

## Instructions

### Step 1: Implementing Copy Hook Handlers

Like all Shell extension handlers, copy hook handlers are in-process Component Object Model (COM) objects implemented as DLLs. They export one interface in addition to [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown): [**ICopyHook**](/previous-versions/windows/desktop/legacy/bb776049(v=vs.85)). The Shell initializes the handler directly, so there is no need for an initialization interface such as [**IShellExtInit**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit).

The [**ICopyHook**](/previous-versions/windows/desktop/legacy/bb776049(v=vs.85)) interface has a single method, [**ICopyHook::CopyCallback**](/previous-versions/windows/desktop/legacy/bb776048(v=vs.85)). When a folder is about to be moved, the Shell calls this method. It passes in a variety of information, including:

-   The folder's name.
-   The folder's destination or new name.
-   The operation that is being attempted.
-   The attributes of the source and destination folders.
-   A window handle that can be used to display a user interface.

When your handler's [**ICopyHook::CopyCallback**](/previous-versions/windows/desktop/legacy/bb776048(v=vs.85)) method is called, it returns one of the three following values to indicate to the Shell how it should proceed.



| Value    | Description                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| IDYES    | Allows the operation.                                                                                                                            |
| IDNO     | Prevents the operation on this folder. The Shell can continue with any other operations that have been approved, such as a batch copy operation. |
| IDCANCEL | Prevents the current operation and cancels any pending operations.                                                                               |



 

### Step 2: Registering Copy Hook Handlers

Copy hook handlers for folders are registered under the **HKEY\_CLASSES\_ROOT**\\**Directory**\\**shellex**\\**CopyHookHandlers** subkey. Create a subkey of **CopyHookHandlers** named for the handler, and set the subkey's default value to the string form of the handler's class identifier (CLSID) GUID.

The following example adds the **MyCopyHandler** subkey to the Shell's list of copy hook handlers.

```
HKEY_CLASSES_ROOT
   Directory
      shellex
         CopyHookHandlers
            MyCopyHandler
               (Default) = {MyCopyHandler CLSID GUID}
```

Copy hook handlers for printer objects are registered in essentially the same way. The only difference is that you must register them under the **HKEY\_CLASSES\_ROOT**\\**Printers** subkey.

## Remarks

Normally, users and applications can copy, move, delete, or rename folders with few restrictions. By implementing a copy hook handler, you can control whether these operations take place. For instance, implementing such a handler allows you to prevent critical folders from being renamed or deleted. Copy hook handlers can also be implemented for printer objects.

Copy hook handlers are global. The Shell calls all registered handlers every time an application or user attempts to copy, move, delete, or rename a folder or printer object. The handler does not perform the operation itself. It only approves or vetoes it. If all handlers approve, the Shell does the operation. If any handler vetoes the operation, it is canceled and the remaining handlers are not called. Copy hook handlers are not informed of the success or failure of the operation, so they cannot be used to monitor file operations.

## Related topics

<dl> <dt>

[Creating Shell Extension Handlers](handlers.md)
</dt> <dt>

[**ICopyHook**](/previous-versions/windows/desktop/legacy/bb776049(v=vs.85))
</dt> </dl>

 

 
