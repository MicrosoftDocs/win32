---
description: The IsPartiallySpecified method determines if the media type is partially defined. A media type is partial if the major type, subtype, or format type is GUID\_NULL.
ms.assetid: 26dd7a2b-b2f8-485f-a9af-31c3a9eb1def
title: CMediaType.IsPartiallySpecified method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.IsPartiallySpecified
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.IsPartiallySpecified method

The `IsPartiallySpecified` method determines if the media type is partially defined. A media type is *partial* if the major type, subtype, or format type is GUID\_NULL.

## Syntax


```C++
BOOL IsPartiallySpecified() const;
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the media type is partially specified. Otherwise, returns **FALSE**.

## Remarks

The [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) method can accept partial media types.

The implementation does not actually test the subtype. If there is a specified format type, the media type is not considered partial, even if the subtype is GUID\_NULL.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




