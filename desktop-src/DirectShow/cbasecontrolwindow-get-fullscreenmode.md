---
description: The get\_FullScreenMode method retrieves the current full-screen mode.
ms.assetid: 351af361-5cfd-4e82-bd8a-92f629bd270d
title: CBaseControlWindow.get_FullScreenMode method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_FullScreenMode
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_FullScreenMode method

The `get_FullScreenMode` method retrieves the current full-screen mode.

## Syntax


```C++
HRESULT get_FullScreenMode(
   long *FullScreenMode
);
```



## Parameters

<dl> <dt>

*FullScreenMode* 
</dt> <dd>

Pointer to the current full-screen mode.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function returns E\_NOTIMPL by default. This informs the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) plug-in distributor that this renderer does not implement a full-screen renderer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




