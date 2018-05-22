---
Description: 'The following code lists the modules that have been loaded by the SymLoadModule64 or SymInitialize function.'
ms.assetid: '8c7fdfaa-d4d3-42d6-ad19-23e8ffda7bf4'
title: Enumerating Symbol Modules
---

# Enumerating Symbol Modules

The following code lists the modules that have been loaded by the [**SymLoadModule64**](symloadmodule64.md) or [**SymInitialize**](syminitialize.md) function. The [**SymEnumerateModules64**](symenumeratemodules64.md) function requires a callback function, which will be called once for each module loaded. In this example, EnumModules is an implementation of the callback function. The example assumes you have initialized the symbol handler using the code in [Initializing the Symbol Handler](initializing-the-symbol-handler.md).


```C++
BOOL CALLBACK EnumModules(
    PCTSTR  ModuleName, 
    DWORD64 BaseOfDll,  
    PVOID   UserContext )
{
    UNREFERENCED_PARAMETER(UserContext);
    
    _tprintf(TEXT("%08X %s\n"), BaseOfDll, ModuleName);
    return TRUE;
}


if (SymEnumerateModules64(hProcess, EnumModules, NULL))
{
    // SymEnumerateModules64 returned success
}
else
{
    // SymEnumerateModules64 failed
    error = GetLastError();
    _tprintf(TEXT("SymEnumerateModules64 returned error : %d\n"), error);
}
```



 

 



