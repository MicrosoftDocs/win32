---
title: IAgentBalloon GetVisible
description: IAgentBalloon GetVisible
ms.assetid: 328af211-4ea4-482c-8487-42c8e4cd66b0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of variable for word balloon
);                   // Visible setting
```

Determines whether the word balloon is visible or hidden.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

Address of a variable that receives **True** if the word balloon is visible and **False** if hidden.

</dd> </dl>

## See Also

[**IAgentBalloon::SetVisible**](iagentballoon--setvisible.md)


 

 




