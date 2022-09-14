---
title: IAgentCommand SetCaption
description: IAgentCommand SetCaption
ms.assetid: f4fdd37a-28b4-4e00-885c-58addedec659
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::SetCaption

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetCaption(
   BSTR bszCaption  // Caption setting for Command
);
```

Sets the [**Caption**](caption-property.md) text displayed for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszCaption"></span><span id="bszcaption"></span><span id="BSZCAPTION"></span>*bszCaption*
</dt> <dd>

A BSTR that specifies the text for the [**Caption**](caption-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

Setting the [**Caption**](caption-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) defines how it will appear on the character's pop-up menu when its [**Visible**](visible-property.md) property is set to **True** and your application is not the input-active client. To specify an access key (unlined mnemonic) for your **Caption**, include an ampersand (&) character before that character. To make it selectable, its [**Enabled**](enabled-property.md) property must be set to **True**.

## See Also

[**IAgentCommand::GetCaption**](iagentcommand--getcaption.md), [**IAgentCommand::SetEnabled**](iagentcommand--setenabled.md), [**IAgentCommand::SetVisible**](iagentcommand--setvisible.md), [**IAgentCommand::SetVoice**](iagentcommand--setvoice.md), [**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md)


 

 