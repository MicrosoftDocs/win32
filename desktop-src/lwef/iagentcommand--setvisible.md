---
title: IAgentCommand SetVisible
description: IAgentCommand SetVisible
ms.assetid: 58a383f4-6c98-4037-b469-ae68f06c852d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::SetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVisible(
   long bVisible  // Visible setting for Command
);
```

Sets the value of the [**Visible**](visible-property.md) property for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

A Boolean value that determines the [**Visible**](visible-property.md) property of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441). **True** shows the **Command**; **False** hides it.

</dd> </dl>

A [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) must have its [**Visible**](visible-property.md) property set to **True** and its [**Caption**](caption-property.md) property set to appear in the character's pop-up menu.

## See Also

[**IAgentCommand::GetVisible**](iagentcommand--getvisible.md), [**IAgentCommand::SetCaption**](iagentcommand--setcaption.md), [**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md)


 

 




