---
description: CPosPassThru.SetPositions method - The SetPositions method sets the current position and the stop position. This method implements the IMediaSeeking::SetPositions method.
ms.assetid: d4425221-e20f-4e51-8a33-a74fa21f9117
title: CPosPassThru.SetPositions method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.SetPositions
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.SetPositions method

The `SetPositions` method sets the current position and the stop position. This method implements the [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) method.

## Syntax


```C++
HRESULT SetPositions(
   LONGLONG *pCurrent,
   DWORD    dwCurrentFlags,
   LONGLONG *pStop,
   DWORD    dwStopFlags
);
```



## Parameters

<dl> <dt>

*pCurrent* 
</dt> <dd>

Pointer to a variable that specifies the current position, in units of the current time format.

</dd> <dt>

*dwCurrentFlags* 
</dt> <dd>

Bitwise combination of flags. See [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) for more information.

</dd> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that specifies the stop time, in units of the current time format.

</dd> <dt>

*dwStopFlags* 
</dt> <dd>

Bitwise combination of flags. See [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) for more information.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




