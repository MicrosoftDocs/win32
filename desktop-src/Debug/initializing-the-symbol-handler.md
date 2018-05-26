---
Description: The following code demonstrates how to initialize the symbol handler.
ms.assetid: e8c8f648-c3b0-4595-ac07-f508dd576d9f
title: Initializing the Symbol Handler
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Initializing the Symbol Handler

The following code demonstrates how to initialize the symbol handler. The [**SymSetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symsetoptions?branch=master) function defers symbol loading until symbol information is requested. The code loads the symbols for each module in the specified process by passing a value of **TRUE** for the *bInvade* parameter of the [**SymInitialize**](/windows/win32/Dbghelp/nf-dbghelp-syminitialize?branch=master) function. (This function calls the [**SymLoadModule64**](/windows/win32/Dbghelp/nf-dbghelp-symloadmodule?branch=master) function for each module the process has mapped into its address space.)

If the specified process is not the process that called [**SymInitialize**](/windows/win32/Dbghelp/nf-dbghelp-syminitialize?branch=master), the code passes a process identifier as the first parameter of **SymInitialize**.

Specifying **NULL** as the second parameter of [**SymInitialize**](/windows/win32/Dbghelp/nf-dbghelp-syminitialize?branch=master) indicates that the symbol handler should use the default search path to locate symbol files. For detailed information on how the symbol handler locates symbol files or how an application can specify a symbol search path, see [Symbol Paths](symbol-paths.md).


```C++
DWORD  error;
HANDLE hProcess;

SymSetOptions(SYMOPT_UNDNAME | SYMOPT_DEFERRED_LOADS);

hProcess = GetCurrentProcess();

if (!SymInitialize(hProcess, NULL, TRUE))
{
    // SymInitialize failed
    error = GetLastError();
    printf("SymInitialize returned error : %d\n", error);
    return FALSE;
}
```



 

 



