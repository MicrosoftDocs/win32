---
description: The following code demonstrates how to retrieve an undecorated symbol name from a symbol name using UnDecorateSymbolName.
ms.assetid: fcb0591a-dac3-45eb-b4c0-4a35c42450e5
title: Retrieving Undecorated Symbol Names
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Undecorated Symbol Names

The following code demonstrates how to retrieve an undecorated symbol name from a symbol name using [**UnDecorateSymbolName**](/windows/desktop/api/Dbghelp/nf-dbghelp-undecoratesymbolname). The decorated name is stored in `szName`. The example assumes you have initialized the symbol handler using the code in [Initializing the Symbol Handler](initializing-the-symbol-handler.md).


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



 

 



