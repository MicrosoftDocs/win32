---
title: IAgentCommandWindow GetSize
description: IAgentCommandWindow GetSize
ms.assetid: 24ad3b48-6557-4790-b9c4-2cf7df92fa7d
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandWindow::GetSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSize(
   long * plWidth,  // address of variable for Voice Commands Window width
   long * plHeight  // address of variable for Voice Commands Window height
);
```

Retrieves the current size of the Voice Commands Window.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plWidth"></span><span id="plwidth"></span><span id="PLWIDTH"></span>*plWidth*
</dt> <dd>

Address of a variable that receives the width of the Voice Commands Window in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="plHeight"></span><span id="plheight"></span><span id="PLHEIGHT"></span>*plHeight*
</dt> <dd>

Address of a variable that receives the height of the Voice Commands Window in pixels, relative to the screen origin (upper left).

</dd> </dl>

## See Also

[**IAgentCommandWindow::GetPosition**](iagentcommandwindow--getposition.md)


 

 




