---
description: The ReallocFormatBuffer method reallocates the format block to a new size.
ms.assetid: 49bec677-09cc-4e1a-994a-13e873e61713
title: CMediaType.ReallocFormatBuffer method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.ReallocFormatBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.ReallocFormatBuffer method

The `ReallocFormatBuffer` method reallocates the format block to a new size.

## Syntax


```C++
BYTE* ReallocFormatBuffer(
   ULONG length
);
```



## Parameters

<dl> <dt>

*length* 
</dt> <dd>

New size required for the format block, in bytes. Must be greater than zero.

</dd> </dl>

## Return value

Returns a pointer to the new block if successful. Otherwise, returns either a pointer to the old format block, or **NULL**.

## Remarks

This method allocates a new format block. It copies as much of the existing format block as possible into the new format block. If the new block is smaller than the existing block, the existing format block is truncated. If the new block is larger, the contents of the additional space are undefined. They are not explicitly set to zero.

The method updates the **cbFormat** and **pbFormat** members of the **AM\_MEDIA\_TYPE** structure.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




