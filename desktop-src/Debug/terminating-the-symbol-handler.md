---
Description: The following code cleans up all memory associated with symbol handling for the specified process, using SymCleanup.
ms.assetid: 270a1984-9e66-4dd2-accb-d715287f1ec0
title: Terminating the Symbol Handler
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Terminating the Symbol Handler

The following code cleans up all memory associated with symbol handling for the specified process, using [**SymCleanup**](/windows/win32/Dbghelp/nf-dbghelp-symcleanup?branch=master).


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



 

 



