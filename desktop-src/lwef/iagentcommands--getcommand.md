---
title: IAgentCommands GetCommand
description: IAgentCommands GetCommand
ms.assetid: 0f4a9152-d5dc-4045-b469-8a03f0369e34
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::GetCommand

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetCommand(
   long dwCommandID,         // Command ID
   IUnknown ** ppunkCommand  // address of IUnknown interface
);                    
```

Retrieves a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object from the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwCommandID"></span><span id="dwcommandid"></span><span id="DWCOMMANDID"></span>*dwCommandID*
</dt> <dd>

The ID of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object in the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> <dt>

<span id="IUnknown"></span><span id="iunknown"></span><span id="IUNKNOWN"></span>*IUnknown*
</dt> <dd>

The address of the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface for the [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object.

</dd> </dl>

## See Also

[**IAgentCommand**](iagentcommand.md)


 

 




