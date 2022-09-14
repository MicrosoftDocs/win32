---
title: IAgentCommands GetCount
description: IAgentCommands GetCount
ms.assetid: 17140eda-17b0-49c2-8d50-5a38a553191a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::GetCount

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetCount(
   long * pdwCount  // address of count of commands
);                    
```

Retrieves the number of [**Command**](/windows/desktop/lwef/the-command-object) objects in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwCount"></span><span id="pdwcount"></span><span id="PDWCOUNT"></span>*pdwCount*
</dt> <dd>

Address of a variable that receives the number of [**Commands**](/windows/desktop/lwef/the-command-object) in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

</dd> </dl>

*pdwCount* includes only the number of [**Commands**](/windows/desktop/lwef/the-command-object) you define in your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. Server or other client entries are not included.

 

 