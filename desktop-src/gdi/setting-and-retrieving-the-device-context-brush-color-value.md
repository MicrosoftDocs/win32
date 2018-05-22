---
Description: 'The following example shows how an application can retrieve the current DC brush color by using the SetDCBrushColor and the GetDCBrushColor functions.'
ms.assetid: 'a1ef6c25-0d00-4175-8679-001ba165bd6d'
title: Setting and Retrieving the Device Context Brush Color Value
---

# Setting and Retrieving the Device Context Brush Color Value

The following example shows how an application can retrieve the current DC brush color by using the [**SetDCBrushColor**](setdcbrushcolor.md) and the [**GetDCBrushColor**](getdcbrushcolor.md) functions.


```C++
SelectObject(hdc,GetStockObject(DC_BRUSH));
SetDCBrushColor(hdc, RGB(00,0xff;00);
PatBlt(0,0,200,200,PATCOPY)
SetDCBrushColor(hdc,RGB(00,00,0xff);
PatBlt(0,0,200,200,PATCOPY);
```



 

 



