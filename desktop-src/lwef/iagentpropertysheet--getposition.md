---
title: IAgentPropertySheet GetPosition
description: IAgentPropertySheet GetPosition
ms.assetid: 5d3de366-e48a-4643-81c5-ac4808671763
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::GetPosition

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetPosition(
   long * plLeft,  // address of variable for left edge of property sheet
   long * plTop    // address of variable for top edge of property sheet
);
```

Retrieves the Microsoft Agent's property sheet window position.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plLeft"></span><span id="plleft"></span><span id="PLLEFT"></span>*plLeft*
</dt> <dd>

Address of a variable that receives the screen coordinate of the left edge of the property sheet in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="plTop"></span><span id="pltop"></span><span id="PLTOP"></span>*plTop*
</dt> <dd>

Address of a variable that receives the screen coordinate of the top edge of the property sheet in pixels, relative to the screen origin (upper left).

</dd> </dl>

## See Also

[**IAgentPropertySheet::GetSize**](iagentpropertysheet--getsize.md)


 

 




