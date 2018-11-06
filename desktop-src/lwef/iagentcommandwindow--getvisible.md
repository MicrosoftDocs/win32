---
title: IAgentCommandWindow GetVisible
description: IAgentCommandWindow GetVisible
ms.assetid: a69a2aaa-5a3a-46b8-b505-49609a2aa5ba
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandWindow::GetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisible(
   long * pbVisible  // address of variable for Visible setting for 
);                   // Voice Commands Window
```

Determines whether the Voice Commands Window is visible or hidden.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbVisible"></span><span id="pbvisible"></span><span id="PBVISIBLE"></span>*pbVisible*
</dt> <dd>

Address of a variable that receives **True** if the Voice Commands Window is visible, or **False** if hidden.

</dd> </dl>

## See Also

[**IAgentCommandWindow::SetVisible**](iagentcommandwindow--setvisible.md)


 

 




