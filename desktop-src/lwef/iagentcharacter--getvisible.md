---
title: IAgentCharacter GetVisible
description: IAgentCharacter GetVisible
ms.assetid: 6e8e3a68-a7bb-4afb-a753-836fe82a0b24
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of variable for character Visible setting
);
```

Determines whether the character's animation frame is currently visible.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

Address of a variable that receives **True** if the character's frame is visible and **False** if hidden.

</dd> </dl>

You can use this method to determine whether the character's frame is currently visible. To make a character visible, use the [**Show**](/windows/desktop/lwef/iagentcharacter--show) method. To hide a character, use the [**Hide**](/windows/desktop/lwef/iagentcharacter--hide) method.

 

 