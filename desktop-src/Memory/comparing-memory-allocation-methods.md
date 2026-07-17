---
description: The following is a brief comparison of the various memory allocation methods.
ms.assetid: b6101014-02d2-4b19-aec6-8772a2793d38
title: Comparing Memory Allocation Methods
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/18/2025
---

# Comparing Memory Allocation Methods

## Choosing the right allocation method

Use the following guidance to select the appropriate memory allocation API for your scenario:

| Scenario | Recommended API | Notes |
|----------|----------------|-------|
| General-purpose C++ allocations | `new` / `std::make_unique` / `std::make_shared` | Default choice for C++ code. Uses the CRT heap internally. RAII ensures automatic cleanup. |
| General-purpose C allocations | `malloc` / `calloc` / `realloc` | Default choice for C code. Portable across platforms. |
| Allocations larger than ~1 MB or requiring page-level control | [VirtualAlloc](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) | Allocates at page granularity (typically 4 KB). Use for reserving large address ranges, guard pages, or memory with specific protection attributes (`PAGE_READWRITE`, `PAGE_EXECUTE_READ`, etc.). |
| Many small allocations with custom control (e.g., pool allocator) | [HeapAlloc](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) / [HeapCreate](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) | Create a private heap for isolation or serialization control. Use `HEAP_NO_SERIALIZE` only if the heap is exclusively single-threaded. |
| COM interop (marshaled memory) | [CoTaskMemAlloc](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc) | Required when memory crosses COM apartment boundaries. MIDL-generated stubs use CoTaskMemAlloc/CoTaskMemFree. |
| Legacy code using moveable memory | [GlobalAlloc](/windows/desktop/api/WinBase/nf-winbase-globalalloc) / [LocalAlloc](/windows/desktop/api/WinBase/nf-winbase-localalloc) | **Avoid for new code.** These add overhead over HeapAlloc and exist primarily for backward compatibility with clipboard operations and certain Win32 APIs that require them. |

> [!IMPORTANT]
> **Always pair allocation and deallocation functions correctly.** Memory allocated with `HeapAlloc` must be freed with `HeapFree` — not `free()` or `LocalFree`. Mixing allocation/deallocation families causes heap corruption that is difficult to diagnose.

> [!NOTE]
> **VirtualAlloc vs HeapAlloc**: VirtualAlloc operates at page granularity (minimum 4 KB, reservations aligned to `SYSTEM_INFO.dwAllocationGranularity`, typically 64 KB). Allocating many small objects with VirtualAlloc wastes address space. Use HeapAlloc (or `malloc`/`new`) for small, frequent allocations. Use VirtualAlloc when you need to reserve large address regions, control page protection, or implement custom allocators.

## Detailed comparison

The following is a brief comparison of the various memory allocation methods:

-   [**CoTaskMemAlloc**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc)
-   [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc)
-   [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc)
-   [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc)
-   **malloc**
-   **new**
-   [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc)

Although the [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc), [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc), and [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) functions ultimately allocate memory from the same heap, each provides a slightly different set of functionality. For example, **HeapAlloc** can be instructed to raise an exception if memory could not be allocated, a capability not available with **LocalAlloc**. **LocalAlloc** supports allocation of handles which permit the underlying memory to be moved by a reallocation without changing the handle value, a capability not available with **HeapAlloc**.

Starting with 32-bit Windows, [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc) and [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc) are implemented as wrapper functions that call [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) using a handle to the process's default heap. Therefore, **GlobalAlloc** and **LocalAlloc** have greater overhead than **HeapAlloc**.

Because the different heap allocators provide distinctive functionality by using different mechanisms, you must free memory with the correct function. For example, memory allocated with [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) must be freed with [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree) and not [**LocalFree**](/windows/desktop/api/WinBase/nf-winbase-localfree) or [**GlobalFree**](/windows/desktop/api/WinBase/nf-winbase-globalfree). Memory allocated with [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc) or [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc) must be queried, validated, and released with the corresponding global or local function.

The [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) function allows you to specify additional options for memory allocation. However, its allocations use a page granularity, so using **VirtualAlloc** can result in higher memory usage.

The **malloc** function has the disadvantage of being run-time dependent. The **new** operator has the disadvantage of being compiler dependent and language dependent.

The [**CoTaskMemAlloc**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc) function has the advantage of working well in either C, C++, or Visual Basic. It is also the only way to share memory in a COM-based application, since MIDL uses **CoTaskMemAlloc** and [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) to marshal memory.


## Examples

* [Reserving and Committing Memory](./reserving-and-committing-memory.md)

* [AWE Example](./awe-example.md)

## Related topics

<dl> <dt>

[Global and Local Functions](global-and-local-functions.md)
</dt> <dt>

[Heap Functions](heap-functions.md)
</dt> <dt>

[Virtual Memory Functions](virtual-memory-functions.md)
</dt> </dl>

 

 