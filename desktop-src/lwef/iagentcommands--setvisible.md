---
title: IAgentCommands SetVisible
description: IAgentCommands SetVisible
ms.assetid: 4b99989a-29bb-4e0e-8155-cf734cc667fd
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::SetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVisible(
   long bVisible  // the Visible setting for Commands collection
);
```

Sets the value of the [**Visible**](visible-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

A Boolean value that determines the [**Visible**](visible-property.md) property of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. **True** sets the **Commands** collection's [**Caption**](caption-property.md) to be visible when the character's pop-up menu is displayed; *False* does not display it.

</dd> </dl>

A [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection must have its [**Caption**](caption-property.md) property set and its [**Visible**](visible-property.md) property set to **True** to appear on the character's pop-up menu. The **Visible** property must also be set to **True** for commands in the collection to appear when your client application is input-active.

## See Also

[**IAgentCommands::GetVisible**](iagentcommands--getvisible.md), [**IAgentCommand::SetCaption**](iagentcommand--setcaption.md)


 

 