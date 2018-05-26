---
Description: The IncrementTypeVersion method increments the version number on the set of preferred media types.
ms.assetid: 30cad0ae-58e7-47f6-94ee-75e24ce0a7e9
title: CBasePin.IncrementTypeVersion method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.IncrementTypeVersion method

The `IncrementTypeVersion` method increments the version number on the set of preferred media types.

## Syntax


```C++
void IncrementTypeVersion();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method increments the [**CBasePin::m\_TypeVersion**](cbasepin-m-typeversion.md) member variable. If the pin dynamically changes the list of preferred media types, call this method whenever the list changes. For more information, see [**CBasePin::GetMediaTypeVersion**](cbasepin-getmediatypeversion.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




