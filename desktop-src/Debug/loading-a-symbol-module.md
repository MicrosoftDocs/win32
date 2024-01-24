---
description: If an application does not call the SymInitialize function with the fInvadeProcess parameter set to TRUE, it must load symbols for a module when they are required.
ms.assetid: 01cee812-d1f2-4459-acee-bce8719a85b2
title: Loading a Symbol Module
ms.topic: article
ms.date: 05/31/2018
---

# Loading a Symbol Module

If an application does not call the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function with the *fInvadeProcess* parameter set to **TRUE**, it must load symbols for a module when they are required. To load a symbol module on demand, the application can call the [**SymLoadModuleEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symloadmoduleex) function with a full path to a module name. When the module is loaded, the symbol handler will either load the symbols immediately or defer the load, depending on the options set using the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function.

The following code loads a symbol module. Note that it assumes you have initialized the symbol handler using the code in [Initializing the Symbol Handler](initializing-the-symbol-handler.md).


```C++
TCHAR  szImageName[MAX_PATH] = TEXT("foo.dll");
DWORD64 dwBaseAddr = 0;

if (SymLoadModuleEx(hProcess,    // target process 
                    NULL,        // handle to image - not used
                    szImageName, // name of image file
                    NULL,        // name of module - not required
                    dwBaseAddr,  // base address - not required
                    0,           // size of image - not required
                    NULL,        // MODLOAD_DATA used for special cases 
                    0))          // flags - not required
{
    // SymLoadModuleEx returned success
}
else
{
    // SymLoadModuleEx failed
    DWORD error = GetLastError();
    printf("SymLoadModuleEx returned error : %d\n", error);
}
```



Note that *szImageName* can be a path to any executable module that has debugging information (.exe, .dll, .drv, .sys, .scr, .cpl, .com). Also, *dwBaseAddr* is the base address of the symbol module to be loaded. If this value is 0, the symbol handler will obtain the base address from the specified symbol module.

## Related topics

<dl> <dt>

[Unloading a Symbol Module](unloading-a-symbol-module.md)
</dt> </dl>

 

 



