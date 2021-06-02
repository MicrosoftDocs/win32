---
description: The GetCurrentPosition method retrieves the current position, relative to the total duration of the stream. Not implemented.
ms.assetid: 386f41e4-a673-4c67-a28f-e155810fbb5a
title: CSourceSeeking.GetCurrentPosition method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.GetCurrentPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.GetCurrentPosition method

The `GetCurrentPosition` method retrieves the current position, relative to the total duration of the stream. Not implemented.

## Syntax


```C++
HRESULT GetCurrentPosition(
   LONGLONG *pCurrent
);
```



## Parameters

<dl> <dt>

*pCurrent* 
</dt> <dd>

Pointer to a variable that receives the current position, in units of the current time format.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

Source filters typically do not support this method. Instead, renderer filters report the current position through the [**CRendererPosPassThru**](crendererpospassthru.md) class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




