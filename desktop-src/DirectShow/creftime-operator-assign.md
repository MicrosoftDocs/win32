---
description: The = operator assigns a new reference time.
ms.assetid: 0b11e2ea-23dc-4c75-88c6-94215a4b14b6
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
  [ref] const CRefTime &rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a **CRefTime** object that specifies the new reference time.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




