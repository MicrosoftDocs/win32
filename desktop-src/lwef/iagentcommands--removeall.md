---
title: IAgentCommands RemoveAll
description: IAgentCommands RemoveAll
ms.assetid: fab43363-6325-4566-b7bb-599591f67321
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::RemoveAll

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Remove();
```

Removes all [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms696441) from a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

Removing all [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms696441) from a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection also removes them from the pop-up menu and the **Voice Commands Window** when your application is input-active. **RemoveAll** does not remove server or other client's entries.

## See Also

[**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md), [**IAgentCommands::Remove**](iagentcommands--remove.md)


 

 




