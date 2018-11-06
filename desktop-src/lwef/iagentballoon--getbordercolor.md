---
title: IAgentBalloon GetBorderColor
description: IAgentBalloon GetBorderColor
ms.assetid: e6c592c3-0e14-474f-a829-6028f2de5791
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetBorderColor

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetBorderColor (
  long * plBorderColor// address of variable for border color displayed
);                    // for word balloon
```

Retrieves the value for the border color displayed for a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plBorderColor"></span><span id="plbordercolor"></span><span id="PLBORDERCOLOR"></span>*plBorderColor*
</dt> <dd>

The address of a variable that receives the color setting for the balloon border.

</dd> </dl>

The border color for a character word balloon is defined in the Microsoft Agent Character Editor. It cannot be changed by an application. However, the user can change the border color of the word balloons for all characters through the Microsoft Agent property sheet.

## See Also

[**IAgentBalloon::GetBackColor**](iagentballoon--getbackcolor.md), [**IAgentBalloon::GetForeColor**](iagentballoon--getforecolor.md)


 

 




