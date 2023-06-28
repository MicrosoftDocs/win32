---
description: The GetPin method retrieves a pin. The CEnumPins class calls this method to enumerate pins on the filter.
ms.assetid: e3ec3f11-1e7d-40b6-810e-3759f0511cb2
title: CBaseFilter.GetPin method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.GetPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseFilter.GetPin method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetPin** method retrieves a pin. The [**CEnumPins**](cenumpins.md) class calls this method to enumerate pins on the filter.

## Syntax


```C++
virtual CBasePin* GetPin(
   int n
) = 0;
```



## Parameters

<dl> <dt>

*n* 
</dt> <dd>

The zero-based index of the pin.

</dd> </dl>

## Return value

Returns a pointer to the [**CBasePin**](cbasepin.md) object that implements the pin.

## Remarks

You must implement this pure virtual method in your derived class. Return a pointer to the *n*th pin on this filter, indexed from zero. You can choose an arbitrary indexing order, as long as the ordering is fixed. If the filter adds or deletes pins, or the ordering changes for some other reason at run time, call the [**CBaseFilter::IncrementPinVersion**](cbasefilter-incrementpinversion.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




