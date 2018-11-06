---
title: IAgentBalloon GetBackColor
description: IAgentBalloon GetBackColor
ms.assetid: 278ed645-0e6c-4a5d-bd85-3e3b7a1e3333
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetBackColor

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetBackColor(
   long * plBGColor  // address of variable for background color displayed
);                   // in word balloon
```

Retrieves the value for the background color displayed in a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plBGColor"></span><span id="plbgcolor"></span><span id="PLBGCOLOR"></span>*plBGColor*
</dt> <dd>

The address of a variable that receives the color setting for the balloon background.

</dd> </dl>

The background color used in a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can change the background color of the word balloons for all characters through the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::GetForeColor**](iagentballoon--getforecolor.md)


 

 




