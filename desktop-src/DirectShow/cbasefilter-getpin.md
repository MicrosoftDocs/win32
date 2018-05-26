---
Description: The GetPin method retrieves a pin. The CEnumPins class calls this method to enumerate pins on the filter.
ms.assetid: e3ec3f11-1e7d-40b6-810e-3759f0511cb2
title: CBaseFilter.GetPin method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseFilter.GetPin method

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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




