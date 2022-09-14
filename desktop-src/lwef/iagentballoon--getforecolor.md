---
title: IAgentBalloon GetForeColor
description: IAgentBalloon GetForeColor
ms.assetid: b06ad924-66b6-42a6-8c97-5bc4c46f6e2d
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetForeColor

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetForeColor(
   long * plFGColor // address of variable for foreground color displayed
);                  // in word balloon
```

Retrieves the value for the foreground color displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plFGColor"></span><span id="plfgcolor"></span><span id="PLFGCOLOR"></span>*plFGColor*
</dt> <dd>

The address of a variable that receives the color setting for the balloon foreground.

</dd> </dl>

The foreground color used in a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can override the foreground color of the word balloons for all characters through the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::GetBackColor**](iagentballoon--getbackcolor.md)


 

 




