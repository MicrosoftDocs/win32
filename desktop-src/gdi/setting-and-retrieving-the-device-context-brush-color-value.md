---
description: The following example shows how an application can retrieve the current DC brush color by using the SetDCBrushColor and the GetDCBrushColor functions.
ms.assetid: a1ef6c25-0d00-4175-8679-001ba165bd6d
title: Setting and Retrieving the Device Context Brush Color Value
ms.topic: article
ms.date: 05/31/2018
---

# Setting and Retrieving the Device Context Brush Color Value

The following example shows how an application can retrieve the current DC brush color by using the [**SetDCBrushColor**](/windows/desktop/api/Wingdi/nf-wingdi-setdcbrushcolor) and the [**GetDCBrushColor**](/windows/desktop/api/WinGdi/nf-wingdi-getdcbrushcolor) functions.


```C++
SelectObject(hdc,GetStockObject(DC_BRUSH));
SetDCBrushColor(hdc, RGB(00,0xff;00);
PatBlt(0,0,200,200,PATCOPY)
SetDCBrushColor(hdc,RGB(00,00,0xff);
PatBlt(0,0,200,200,PATCOPY);
```



 

 



