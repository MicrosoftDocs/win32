---
description: The CountPrefixBits method calculates the number of zero bits at the start of a specified bit field.
ms.assetid: 36fc5c5f-dc64-4588-9130-1b0740d03be1
title: CImageDisplay.CountPrefixBits method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.CountPrefixBits
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.CountPrefixBits method

The `CountPrefixBits` method calculates the number of zero bits at the start of a specified bit field.

## Syntax


```C++
DWORD CountPrefixBits(
   const DWORD Field
);
```



## Parameters

<dl> <dt>

*Field* 
</dt> <dd>

Specifies a bit field as a **DWORD** value.

</dd> </dl>

## Return value

Returns the number of zero bits that occur before the first 1 bit, or 0x80000000 if all bits are zero.

## Remarks

This method is useful for working with color masks in [**VIDEOINFO**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfo) structures.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




