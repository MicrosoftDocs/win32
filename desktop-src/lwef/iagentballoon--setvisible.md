---
title: IAgentBalloon SetVisible
description: IAgentBalloon SetVisible
ms.assetid: 682ebc6a-522d-4a39-bfa4-30a7c4d84d25
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::SetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVisible(
   long bVisible  // word balloon Visible setting 
);
```

Sets the [**Visible**](visible-property.md) property for the word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

Visible property setting. A value of **True** displays the word balloon; a value of **False** hides it.

</dd> </dl>

## See Also

[**IAgentBalloon::GetVisible**](iagentballoon--getvisible.md)


 

 




