---
title: Memory Allocation in COM
description: Memory Allocation in COM
ms.assetid: b3c318d2-1273-430e-8aca-5bd5c95c138e
ms.topic: article
ms.date: 05/31/2018
---

# Memory Allocation in COM

Sometimes a method allocates a memory buffer on the heap and returns the address of the buffer to the caller. COM defines a pair of functions for allocating and freeing memory on the heap.

-   The [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) function allocates a block of memory.
-   The [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) function frees a block of memory that was allocated with [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc).

We saw an example of this pattern in the [Open dialog box example](example--the-open-dialog-box.md):


```C++
PWSTR pszFilePath;
hr = pItem->GetDisplayName(SIGDN_FILESYSPATH, &pszFilePath);
if (SUCCEEDED(hr))
{
    // ...
    CoTaskMemFree(pszFilePath);
}
```



The [**GetDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-getdisplayname) method allocates memory for a string. Internally, the method calls [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) to allocate the string. When the method returns, *pszFilePath* points to the memory location of the new buffer. The caller is responsible for calling [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to free the memory.

Why does COM define its own memory allocation functions? One reason is to provide an abstraction layer over the heap allocator. Otherwise, some methods might call **malloc** while others called **new**. Then your program would need to call **free** in some cases and **delete** in others, and keeping track of it all would quickly become impossible. The COM allocation functions create a uniform approach.

Another consideration is the fact that COM is a *binary* standard, so it is not tied to a particular programming language. Therefore, COM cannot rely on any language-specific form of memory allocation.

## Next

[COM Coding Practices](com-coding-practices.md)

 

 
