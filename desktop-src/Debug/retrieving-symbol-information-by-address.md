---
description: The following code demonstrates how to call the SymFromAddr function.
ms.assetid: 63dfadea-b0c4-4050-add8-d1f3aef7a495
title: Retrieving Symbol Information by Address
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Symbol Information by Address

The following code demonstrates how to call the [**SymFromAddr**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromaddr) function. This function fills in a [**SYMBOL\_INFO**](/windows/desktop/api/DbgHelp/ns-dbghelp-symbol_info) structure. Because the name is variable in length, you must supply a buffer that is large enough to hold the name stored at the end of the **SYMBOL\_INFO** structure. Also, the **MaxNameLen** member must be set to the number of bytes reserved for the name. In this example, *dwAddress* is the address to be mapped to a symbol. The **SymFromAddr** function will store an offset to the beginning of the symbol to the address in *dwDisplacement*. The example assumes you have initialized the symbol handler using the code in [Initializing the Symbol Handler](initializing-the-symbol-handler.md).


```C++
DWORD64  dwDisplacement = 0;
DWORD64  dwAddress = SOME_ADDRESS;

char buffer[sizeof(SYMBOL_INFO) + MAX_SYM_NAME * sizeof(TCHAR)];
PSYMBOL_INFO pSymbol = (PSYMBOL_INFO)buffer;

pSymbol->SizeOfStruct = sizeof(SYMBOL_INFO);
pSymbol->MaxNameLen = MAX_SYM_NAME;

if (SymFromAddr(hProcess, dwAddress, &dwDisplacement, pSymbol))
{
    // SymFromAddr returned success
}
else
{
    // SymFromAddr failed
    DWORD error = GetLastError();
    printf("SymFromAddr returned error : %d\n", error);
}
```



To retrieve the source code line number for a specified address, an application can use [**SymGetLineFromAddr64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetlinefromaddr). This function requires a pointer to an [**IMAGEHLP\_LINE64**](/windows/desktop/api/DbgHelp/ns-dbghelp-imagehlp_line) structure to receive the source file name and line number corresponding to a specified code address. Note that the symbol handler can retrieve line number information only when **SYMOPT\_LOAD\_LINES** is set using the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function. This option must be set before loading the module. The dwAddress parameter contains the code address for which the source file name and line number will be located.


```C++
DWORD64  dwAddress;
DWORD  dwDisplacement;
IMAGEHLP_LINE64 line;

SymSetOptions(SYMOPT_LOAD_LINES);

line.SizeOfStruct = sizeof(IMAGEHLP_LINE64);
dwAddress = 0x1000000; // Address you want to check on.

if (SymGetLineFromAddr64(hProcess, dwAddress, &dwDisplacement, &line))
{
    // SymGetLineFromAddr64 returned success
}
else
{
    // SymGetLineFromAddr64 failed
    DWORD error = GetLastError();
    _tprintf(TEXT("SymGetLineFromAddr64 returned error : %d\n"), error);
}
```



 

 



