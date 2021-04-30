---
description: The GetVideoSize method retrieves the native video's width and height.
ms.assetid: b3461a56-705b-465a-9cfc-e86fd52a07c5
title: CBaseControlVideo.GetVideoSize method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetVideoSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.GetVideoSize method

The `GetVideoSize` method retrieves the native video's width and height.

## Syntax


```C++
HRESULT GetVideoSize(
   long *pWidth,
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pWidth* 
</dt> <dd>

Pointer to the video width.

</dd> <dt>

*pHeight* 
</dt> <dd>

Pointer to the video height.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




