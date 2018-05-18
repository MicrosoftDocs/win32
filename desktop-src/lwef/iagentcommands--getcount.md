---
title: IAgentCommands GetCount
description: IAgentCommands GetCount
ms.assetid: '17140eda-17b0-49c2-8d50-5a38a553191a'
---

# IAgentCommands::GetCount

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetCount(
   long * pdwCount  // address of count of commands
);                    
```

Retrieves the number of [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) objects in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwCount"></span><span id="pdwcount"></span><span id="PDWCOUNT"></span>*pdwCount*
</dt> <dd>

Address of a variable that receives the number of [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms696441) in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> </dl>

*pdwCount* includes only the number of [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms696441) you define in your [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. Server or other client entries are not included.

 

 




