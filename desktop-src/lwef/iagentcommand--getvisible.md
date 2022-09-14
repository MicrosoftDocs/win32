---
title: IAgentCommand GetVisible
description: IAgentCommand GetVisible
ms.assetid: cac07737-6a0b-4587-ae16-2137ce0d412c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of Visible setting for Command
);
```

Retrieves the value of the [**Visible**](visible-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

The address of a variable that receives the [**Visible**](visible-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

## See Also

[**IAgentCommand::SetVisible**](iagentcommand--setvisible.md), [**IAgentCommand::SetCaption**](iagentcommand--setcaption.md), [**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md)


 

 