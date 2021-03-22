---
description: The = operator assigns a new reference time.
ms.assetid: 556c2e8a-4726-42ab-949d-9a028ebb1b95
title: CRefTime.operator= method (Reftime.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime.operator=
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRefTime.operator= method (Reftime.h)

The = operator assigns a new reference time.

## Syntax


```C++
CRefTime& operator=(
   const LONGLONG ll
);
```



## Parameters

<dl> <dt>

*ll* 
</dt> <dd>

New reference time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




