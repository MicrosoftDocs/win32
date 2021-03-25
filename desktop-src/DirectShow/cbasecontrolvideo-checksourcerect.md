---
description: Determines if a source rectangle is valid.
ms.assetid: 3fef107b-6f4c-4fab-91d3-6ab72dcc32be
title: CBaseControlVideo.CheckSourceRect method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.CheckSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.CheckSourceRect method

Determines if a source rectangle is valid.

## Syntax


```C++
virtual HRESULT CheckSourceRect(
   RECT *pSourceRect
);
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the source rectangle to check.

</dd> </dl>

## Return value

Returns E\_INVALIDARG if not valid; otherwise, returns NOERROR (S\_OK).

## Remarks

This member function checks that the source rectangle requested does not exceed the available source video. The left and top coordinates cannot be negative, and the width and height cannot exceed the right and bottom of the video.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




