---
title: IAgentCommands GetVisible
description: IAgentCommands GetVisible
ms.assetid: 229a02c8-f0a1-4ee5-9bae-961b63792038
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of Visible setting for Commands collection
);
```

Retrieves the value of the [**Visible**](visible-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

The address of a variable that receives the value of the [**Visible**](visible-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

</dd> </dl>

## See Also

[**IAgentCommands::SetVisible**](iagentcommands--setvisible.md), [**IAgentCommands::SetCaption**](iagentcommands--setcaption.md)


 

 