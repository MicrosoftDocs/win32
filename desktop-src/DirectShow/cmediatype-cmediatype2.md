---
description: "Learn about the CMediaType.CMediaType constructor (Mtype.h) method. This method uses the 'majortype' parameter."
ms.assetid: 89356578-0509-46c1-abd4-421688017f1d
title: CMediaType.CMediaType constructor (Mtype.h) - majortype parameter
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.CMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.CMediaType constructor (Mtype.h) - majortype parameter

Constructor method.

## Syntax


```C++
CMediaType(
   const GUID *majortype
);
```



## Parameters

<dl> <dt>

*majortype* 
</dt> <dd>

Pointer to a major type **GUID**. The constructor initializes the major type GUID to this value.

</dd> </dl>

## Remarks

The constructor calls the [**CMediaType::InitMediaType**](cmediatype-initmediatype.md) method to initialize the media type.

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Mtype.h (include Streams.h)                                                                                     |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




