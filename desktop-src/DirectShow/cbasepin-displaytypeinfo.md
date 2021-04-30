---
description: The DisplayTypeInfo method displays media type information during debugging.
ms.assetid: fd10d37b-57f5-4246-8ca3-f4bc59911445
title: CBasePin.DisplayTypeInfo method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.DisplayTypeInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.DisplayTypeInfo method

The `DisplayTypeInfo` method displays media type information during debugging.

## Syntax


```C++
void DisplayTypeInfo(
         IPin       *pPin,
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Ignored.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

In debug builds, this method calls the [**DbgLog**](dbglog.md) function to display the specified media type. In retail builds, this method does nothing.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




