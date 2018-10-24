---
title: Memory Allocation in COM
description: .
ms.assetid: b3c318d2-1273-430e-8aca-5bd5c95c138e
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Memory Allocation in COM

Sometimes a method allocates a memory buffer on the heap and returns the address of the buffer to the caller. COM defines a pair of functions for allocating and freeing memory on the heap.

-   The [**CoTaskMemAlloc**](https://msdn.microsoft.com/library/windows/desktop/ms692727) function allocates a block of memory.
-   The [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) function frees a block of memory that was allocated with [**CoTaskMemAlloc**](https://msdn.microsoft.com/library/windows/desktop/ms692727).

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



The [**GetDisplayName**](https://msdn.microsoft.com/library/windows/desktop/bb761140) method allocates memory for a string. Internally, the method calls [**CoTaskMemAlloc**](https://msdn.microsoft.com/library/windows/desktop/ms692727) to allocate the string. When the method returns, *pszFilePath* points to the memory location of the new buffer. The caller is responsible for calling [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) to free the memory.

Why does COM define its own memory allocation functions? One reason is to provide an abstraction layer over the heap allocator. Otherwise, some methods might call **malloc** while others called **new**. Then your program would need to call **free** in some cases and **delete** in others, and keeping track of it all would quickly become impossible. The COM allocation functions create a uniform approach.

Another consideration is the fact that COM is a *binary* standard, so it is not tied to a particular programming language. Therefore, COM cannot rely on any language-specific form of memory allocation.

## Next

[COM Coding Practices](com-coding-practices.md)

 

 




