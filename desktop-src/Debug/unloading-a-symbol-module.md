---
description: The following code unloads a symbol module referred to by the BaseOfDll module address using SymUnloadModule64.
ms.assetid: f185ae64-1de9-4139-acd5-7c3a108e1eba
title: Unloading a Symbol Module
ms.topic: article
ms.date: 05/31/2018
---

# Unloading a Symbol Module

The following code unloads a symbol module referred to by the BaseOfDll module address using [**SymUnloadModule64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symunloadmodule).


```C++
if (SymUnloadModule64(hProcess, BaseOfDll))
{
    // SymUnloadModule64 returned success
}
else
{
    // SymUnloadModule64 failed
    DWORD error = GetLastError();
    printf("SymUnloadModule64 returned error : %d\n", error);
}
```



## Related topics

<dl> <dt>

[Loading a Symbol Module](loading-a-symbol-module.md)
</dt> </dl>

 

 



