---
title: IAgentPropertySheet GetSize
description: IAgentPropertySheet GetSize
ms.assetid: 09bac150-ad68-40b2-9c2c-760f6bc919e4
ms.topic: article
ms.date: 05/31/2018
---

# IAgentPropertySheet::GetSize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSize(
   long * plWidth,  // address of variable for property sheet width
   long * plHeight  // address of variable for property sheet height
);
```

Retrieves the size of the Microsoft Agent property sheet window.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="plWidth"></span><span id="plwidth"></span><span id="PLWIDTH"></span>*plWidth*
</dt> <dd>

Address of a variable that receives the width of the property sheet in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="plHeight"></span><span id="plheight"></span><span id="PLHEIGHT"></span>*plHeight*
</dt> <dd>

Address of a variable that receives the height of the property sheet in pixels, relative to the screen origin (upper left).

</dd> </dl>

## See Also

[**IAgentPropertySheet::GetPosition**](iagentpropertysheet--getposition.md)


 

 




