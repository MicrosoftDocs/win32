---
description: The following code cleans up all memory associated with symbol handling for the specified process, using SymCleanup.
ms.assetid: 270a1984-9e66-4dd2-accb-d715287f1ec0
title: Terminating the Symbol Handler
ms.topic: concept-article
ms.date: 07/14/2025
---

# Terminating the Symbol Handler

The following code cleans up all memory associated with symbol handling for the specified process, using [**SymCleanup**](/windows/desktop/api/Dbghelp/nf-dbghelp-symcleanup).


```C++
if (SymCleanup(hProcess))
{
    // SymCleanup returned success
}
else
{
    // SymCleanup failed
    DWORD error = GetLastError();
    printf("SymCleanup returned error : %d\n", error);
}
```



 

 



