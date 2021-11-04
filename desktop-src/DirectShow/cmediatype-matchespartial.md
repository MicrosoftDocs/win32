---
description: The MatchesPartial method determines if this media type matches a partially specified media type.
ms.assetid: 62d531f3-5aa2-4af2-b951-584a49a849fc
title: CMediaType.MatchesPartial method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.MatchesPartial
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.MatchesPartial method

The `MatchesPartial` method determines if this media type matches a partially specified media type.

## Syntax


```C++
BOOL MatchesPartial(
   const CMediaType *ppartial
) const;
```



## Parameters

<dl> <dt>

*ppartial* 
</dt> <dd>

Pointer to the media type to match.

</dd> </dl>

## Return value

Returns **TRUE** if the media types match. Otherwise, returns **FALSE**.

## Remarks

The media type specified by *ppartial* can have a value of GUID\_NULL for the major type, subtype, or format type. Any members with GUID\_NULL values are not tested. (In effect, GUID\_NULL acts as a wildcard.) Members with values other than GUID\_NULL must match for the media type to match.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




