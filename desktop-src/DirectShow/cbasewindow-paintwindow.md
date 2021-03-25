---
description: The PaintWindow method causes the window to be repainted.
ms.assetid: dce3d782-00e5-4176-9365-378d59d48ebc
title: CBaseWindow.PaintWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.PaintWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.PaintWindow method

The `PaintWindow` method causes the window to be repainted.

## Syntax


```C++
void PaintWindow(
   BOOL bErase
);
```



## Parameters

<dl> <dt>

*bErase* 
</dt> <dd>

Boolean value that specifies whether the background is erased. If the value is **TRUE**, the background is erased.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method generates a WM\_PAINT message by invalidating the window's entire client area.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




