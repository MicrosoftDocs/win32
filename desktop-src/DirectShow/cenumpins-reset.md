---
Description: The Reset method resets the enumeration sequence to the beginning. This method implements the IEnumPins::Reset method.
ms.assetid: b2e86304-bb14-495b-a922-8868b3898d85
title: CEnumPins.Reset method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumPins.Reset
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CEnumPins.Reset method

The `Reset` method resets the enumeration sequence to the beginning. This method implements the [**IEnumPins::Reset**](/windows/desktop/api/Strmif/nf-strmif-ienumpins-reset) method.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CEnumPins Class**](cenumpins.md)
</dt> </dl>

 

 




