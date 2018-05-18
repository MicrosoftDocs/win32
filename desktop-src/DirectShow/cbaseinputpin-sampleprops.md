---
Description: 'The SampleProps method retrieves the properties of the most recent sample, in an AM\_SAMPLE2\_PROPERTIES structure.'
ms.assetid: 'd4c98c35-f8b2-4111-bae9-4e0f58a0cc8a'
title: 'CBaseInputPin.SampleProps method'
---

# CBaseInputPin.SampleProps method

The `SampleProps` method retrieves the properties of the most recent sample, in an [**AM\_SAMPLE2\_PROPERTIES**](am-sample2-properties.md) structure.

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

 

 




