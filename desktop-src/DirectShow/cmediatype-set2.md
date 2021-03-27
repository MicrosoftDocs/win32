---
description: The Set method sets the media type from another media type.
ms.assetid: b3cf65c2-48db-4ee0-9a74-c1652f017eed
title: CMediaType.Set method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.Set
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.Set method (Mtype.h)

The `Set` method sets the media type from another media type.

## Syntax


```C++
HRESULT Set(
  [ref] const AM_MEDIA_TYPE &mtype
);
```



## Parameters

<dl> <dt>

*mtype* \[ref\]
</dt> <dd>

Reference to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure.

</dd> </dl>

## Return value

Returns S\_OK or E\_OUTOFMEMORY.

## Remarks

This method copies the entire media type from *mtype*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




