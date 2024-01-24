---
description: The SetFormat method initializes the format block.
ms.assetid: 71f1c3d4-9c45-4124-8560-378c8f66e710
title: CMediaType.SetFormat method (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CMediaType.SetFormat method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




