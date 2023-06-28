---
description: The GetBitCount function returns the number of bits per pixel used by a specified video subtype. This function is valid for uncompressed RGB subtypes only.
ms.assetid: 876b91c8-50ba-4217-b79c-7f7ec1c22b83
title: GetBitCount function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetBitCount
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# GetBitCount function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetBitCount` function returns the number of bits per pixel used by a specified video subtype. This function is valid for uncompressed RGB subtypes only.

## Syntax


```C++
WORD GetBitCount(
   const GUID *pSubtype
);
```



## Parameters

<dl> <dt>

*pSubtype* 
</dt> <dd>

Pointer to a video subtype **GUID**.

</dd> </dl>

## Return value

Returns the number of bits per pixel for this subtype, or the value **USHRT\_MAX** if the subtype is not recognized.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




