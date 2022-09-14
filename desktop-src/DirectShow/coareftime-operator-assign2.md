---
description: "The operator assigns a new reference time and uses the 'rt [ref]' parameter."
ms.assetid: e3a005c0-95d5-41e0-80bb-e70399a50dca
title: COARefTime.operator= method (Ctlutil.h) - rt [ref] parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime.operator=
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COARefTime.operator= method (Ctlutil.h) - rt [ref] parameter

This operator assigns a new reference time.

## Syntax


```C++
COARefTime& operator=(
  [ref] const REFERENCE_TIME &rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a [**REFERENCE\_TIME**](reference-time.md) value that specifies the new reference time in 100-nanosecond units.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements

| Requirement                    | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Ctlutil.h (include Streams.h)                                                                                   |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




