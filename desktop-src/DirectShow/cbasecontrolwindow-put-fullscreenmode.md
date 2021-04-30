---
description: The put\_FullScreenMode method sets the full-screen mode of the renderer.
ms.assetid: 25e2a12e-a327-4aab-b4ab-54db0dfc950a
title: CBaseControlWindow.put_FullScreenMode method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_FullScreenMode
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_FullScreenMode method

The `put_FullScreenMode` method sets the full-screen mode of the renderer.

## Syntax


```C++
HRESULT put_FullScreenMode(
   long FullScreenMode
);
```



## Parameters

<dl> <dt>

*FullScreenMode* 
</dt> <dd>

Full-screen mode to apply.

</dd> </dl>

## Return value

Returns an **HRESULT** value. The current implementation returns E\_NOTIMPL.

## Remarks

A video renderer that implements a full-screen mode should override this member function and implement whatever modes it supports.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




