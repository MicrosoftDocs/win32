---
description: The StreamTime method retrieves the current stream time.
ms.assetid: 2e1ff6f1-9815-4ee6-97e8-a5ab5f472b27
title: CBaseMediaFilter.StreamTime method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseMediaFilter.StreamTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseMediaFilter.StreamTime method

The `StreamTime` method retrieves the current stream time.

## Syntax


```C++
virtual HRESULT StreamTime(
  [ref] CRefTime &rtStream
);
```



## Parameters

<dl> <dt>

*rtStream* \[ref\]
</dt> <dd>

Reference to a [**CRefTime**](creftime.md) object that receives the current stream time.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                      | Description                                 |
|--------------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Success.<br/>                         |
| <dl> <dt>**VFW\_E\_NO\_CLOCK**</dt> </dl> | No reference clock is available.<br/> |



 

## Remarks

Stream time is defined as the current reference time (as given by the reference clock) minus the start time (specified by [**CBaseMediaFilter::m\_tStart**](cbasemediafilter-m-tstart.md)). A media sample's time stamp specifies the stream time when it should be rendered. If a sample with a time stamp less than the current stream time has not yet been rendered, it is late.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




