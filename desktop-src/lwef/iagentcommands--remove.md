---
title: IAgentCommands Remove
description: IAgentCommands Remove
ms.assetid: 1f41aa2d-e50b-48a8-87fc-fda4730b035a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::Remove

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Remove(
   long dwID  // Command ID
);
```

Removes the specified [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) from a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwID"></span><span id="dwid"></span><span id="DWID"></span>*dwID*
</dt> <dd>

The ID of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) to remove from the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> </dl>

Removing a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) from a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection also removes it from the pop-up menu and the **Voice Commands Window** when your application is input-active.

## See Also

[**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md), [**IAgentCommands::RemoveAll**](iagentcommands--removeall.md)


 

 




