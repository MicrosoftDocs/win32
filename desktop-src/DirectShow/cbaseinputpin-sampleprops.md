---
Description: The SampleProps method retrieves the properties of the most recent sample, in an AM\_SAMPLE2\_PROPERTIES structure.
ms.assetid: d4c98c35-f8b2-4111-bae9-4e0f58a0cc8a
title: CBaseInputPin.SampleProps method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseInputPin.SampleProps method

The `SampleProps` method retrieves the properties of the most recent sample, in an [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/strmif/ns-strmif-tagam_sample2_properties?branch=master) structure.

## Syntax


```C++
AM_SAMPLE2_PROPERTIES* SampleProps();
```



## Parameters

This method has no parameters.

## Return value

Returns the address of the [**CBaseInputPin::m\_SampleProps**](cbaseinputpin-m-sampleprops.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




