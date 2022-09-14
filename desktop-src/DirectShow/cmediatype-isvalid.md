---
description: The IsValid method determines whether a major type has been assigned to this object.
ms.assetid: 22d28019-f360-4b93-972c-d1dfe83938f0
title: CMediaType.IsValid method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.IsValid
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.IsValid method

The `IsValid` method determines whether a major type has been assigned to this object.

## Syntax


```C++
BOOL IsValid() const;
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if a major type has been assigned to this object. Otherwise, returns **FALSE**.

## Remarks

By default, [**CMediaType**](cmediatype.md) objects are initialized with a major type of GUID\_NULL. Call this method to determine whether the object has been correctly initialized.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




