---
title: IAgentCommandWindow SetVisible
description: IAgentCommandWindow SetVisible
ms.assetid: 44f3fc2d-937a-4890-8dad-e0f29da4c6b5
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandWindow::SetVisible

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVisible(
   long bVisible  // Voice Commands Window Visible setting 
);
```

Set the [**Visible**](visible-property.md) property for the Voice Commands Window.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

[**Visible**](visible-property.md) property setting. A value of **True** displays the Voice Commands Window; **False** hides it.

</dd> </dl>

The user can override this property.

## See Also

[**IAgentCommandWindow::GetVisible**](iagentcommandwindow--getvisible.md)


 

 




