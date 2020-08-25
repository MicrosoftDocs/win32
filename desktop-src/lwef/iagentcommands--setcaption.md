---
title: IAgentCommands SetCaption
description: IAgentCommands SetCaption
ms.assetid: 042f7366-0071-40a5-a47c-81c02cdbe3a9
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::SetCaption

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetCaption(
   BSTR bszCaption  // Caption setting for Commands collection
);
```

Sets the [**Caption**](caption-property.md) text displayed for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszCaption"></span><span id="bszcaption"></span><span id="BSZCAPTION"></span>*bszCaption*
</dt> <dd>

A BSTR that specifies the value for the [**Caption**](caption-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

</dd> </dl>

Setting the [**Caption**](caption-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection defines how it will appear on the character's pop-up menu when its [**Visible**](visible-property.md) property is set to **True** and your application is not the input-active client. To specify an access key (unlined mnemonic) for your **Caption**, include an ampersand (&) character before that character.

If you define commands for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection that has its [**Caption**](caption-property.md) set, you typically also define a **Caption** for its **Commands** collection.

## See Also

[**IAgentCommands::GetCaption**](iagentcommands--getcaption.md), [**IAgentCommands::SetVisible**](iagentcommands--setvisible.md), [**IAgentCommands::SetVoice**](iagentcommands--setvoice.md)


 

 