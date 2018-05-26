---
title: Debugging Memory Allocations
description: Debugging Memory Allocations
ms.assetid: 522adb1f-0e3e-4dfb-8836-f539a79a3d9e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Debugging Memory Allocations

COM provides the [**IMallocSpy**](/windows/win32/ObjIdl/nn-objidl-imallocspy?branch=master) interface for developers to use to debug their memory allocations. For each method in [**IMalloc**](/windows/win32/objidlbase/nn-objidl-imalloc?branch=master), there are two methods in **IMallocSpy**, a "pre" method and a "post" method. After a developer implements it and publishes it to the system, the system calls the **IMallocSpy** "pre" method just before the corresponding **IMalloc** method, effectively allowing the debug code to "spy" on the allocation operation, and calls the "post" method to release the spy.

For example, when COM detects that the next call is a call to [**IMalloc::Alloc**](/windows/win32/ObjIdl/nf-objidl-imalloc-alloc?branch=master), it calls [**IMallocSpy::PreAlloc**](/windows/win32/ObjIdl/nf-objidl-imallocspy-prealloc?branch=master), executing whatever debug operations the developer wants during the **Alloc** execution, and then, when the **Alloc** call returns, calls [**IMallocSpy::PostAlloc**](/windows/win32/ObjIdl/nf-objidl-imallocspy-postalloc?branch=master) to release the spy and return control to the code.

## Related topics

<dl> <dt>

[Managing Memory Allocation](managing-memory-allocation.md)
</dt> </dl>

 

 




