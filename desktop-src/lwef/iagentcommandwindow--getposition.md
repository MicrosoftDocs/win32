---
title: IAgentCommandWindow GetPosition
description: IAgentCommandWindow GetPosition
ms.assetid: d85a7a2c-f0ea-4612-aa73-2e44c49e4e18
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandWindow::GetPosition

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetPosition(
   long * plLeft,  // address of variable for left edge of Voice Commands Window
   long * plTop    // address of variable for top edge of Voice Commands Window
);
```

Retrieves the Voice Commands Window's position.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plLeft"></span><span id="plleft"></span><span id="PLLEFT"></span>*plLeft*
</dt> <dd>

Address of a variable that receives the screen coordinate of the left edge of the Voice Commands Window in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="plTop"></span><span id="pltop"></span><span id="PLTOP"></span>*plTop*
</dt> <dd>

Address of a variable that receives the screen coordinate of the top edge of the Voice Commands Window in pixels, relative to the screen origin (upper left).

</dd> </dl>

## See Also

[**IAgentCommandWindow::GetSize**](iagentcommandwindow--getsize.md)


 

 




