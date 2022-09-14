---
description: CEnumPins.CEnumPins constructor - Constructor method.
ms.assetid: f696e433-b051-4de0-80e5-f9cd31fd0f23
title: CEnumPins.CEnumPins constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumPins.CEnumPins
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CEnumPins.CEnumPins constructor

Constructor method.

## Syntax


```C++
CEnumPins(
   CBaseFilter *pFilter,
   CEnumPins   *pEnumPins
);
```



## Parameters

<dl> <dt>

*pFilter* 
</dt> <dd>

Pointer to the filter on which to enumerate the pins.

</dd> <dt>

*pEnumPins* 
</dt> <dd>

Pointer to the [**IEnumPins**](/windows/desktop/api/Strmif/nn-strmif-ienumpins) interface of an enumerator to clone, or **NULL**.

</dd> </dl>

## Remarks

If *pEnumPins* is **NULL**, this method initializes the enumerator to the beginning of the enumeration sequence. Otherwise, it duplicates the internal state of the enumerator specified by *pEnumPins*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CEnumPins Class**](cenumpins.md)
</dt> </dl>

 

 




