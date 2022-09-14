---
description: Retrieves the class identifier for this filter.
ms.assetid: f0559437-5d0d-4522-a3dc-947e3494b576
title: CPersistStream.GetClassID method (Pstream.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.GetClassID
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPersistStream.GetClassID method

Retrieves the class identifier for this filter.

## Syntax


```C++
HRESULT GetClassID(
   CLSID *pClsID
);
```



## Parameters

<dl> <dt>

*pClsID* 
</dt> <dd>

Pointer to a CLSID structure. Copy your class ID to here.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




