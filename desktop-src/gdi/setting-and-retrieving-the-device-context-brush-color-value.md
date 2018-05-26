---
Description: The following example shows how an application can retrieve the current DC brush color by using the SetDCBrushColor and the GetDCBrushColor functions.
ms.assetid: a1ef6c25-0d00-4175-8679-001ba165bd6d
title: Setting and Retrieving the Device Context Brush Color Value
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting and Retrieving the Device Context Brush Color Value

The following example shows how an application can retrieve the current DC brush color by using the [**SetDCBrushColor**](/windows/win32/Wingdi/nf-wingdi-setdcbrushcolor?branch=master) and the [**GetDCBrushColor**](/windows/win32/WinGdi/nf-wingdi-getdcbrushcolor?branch=master) functions.


```C++
SelectObject(hdc,GetStockObject(DC_BRUSH));
SetDCBrushColor(hdc, RGB(00,0xff;00);
PatBlt(0,0,200,200,PATCOPY)
SetDCBrushColor(hdc,RGB(00,00,0xff);
PatBlt(0,0,200,200,PATCOPY);
```



 

 



