---
description: The SetFormat method initializes the format block.
ms.assetid: 71f1c3d4-9c45-4124-8560-378c8f66e710
title: CMediaType.SetFormat method (Mtype.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaType.SetFormat method

The `SetFormat` method initializes the format block.

## Syntax


```C++
BOOL SetFormat(
   BYTE  *pFormat,
   ULONG length
);
```



## Parameters

<dl> <dt>

*pFormat* 
</dt> <dd>

Pointer to a block of memory that contains the format block.

</dd> <dt>

*length* 
</dt> <dd>

Length of the format block, in bytes.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** if an error occurred.

## Remarks

This method allocates memory for the format block and copies the buffer specified by *pFormat* into the new format block. If the media type already contains a format block, the old one is released. The method also sets the **cbFormat** member of the **AM\_MEDIA\_TYPE** structure.

To set the format type, call the [**CMediaType::SetFormatType**](cmediatype-setformattype.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




