---
Description: The following code demonstrates how to retrieve an undecorated symbol name from a symbol name using UnDecorateSymbolName.
ms.assetid: fcb0591a-dac3-45eb-b4c0-4a35c42450e5
title: Retrieving Undecorated Symbol Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Undecorated Symbol Names

The following code demonstrates how to retrieve an undecorated symbol name from a symbol name using [**UnDecorateSymbolName**](/windows/win32/Dbghelp/nf-dbghelp-undecoratesymbolname?branch=master). The decorated name is stored in `szName`. The example assumes you have initialized the symbol handler using the code in [Initializing the Symbol Handler](initializing-the-symbol-handler.md).


```C++
if (UnDecorateSymbolName(szName, szUndName, sizeof(szUndName), UNDNAME_COMPLETE))
{
    // UnDecorateSymbolName returned success
    printf ("Symbol : %s\n", szUndName);
}
else
{
    // UnDecorateSymbolName failed
    DWORD error = GetLastError();
    printf("UnDecorateSymbolName returned error %d\n", error);
}
```



 

 



