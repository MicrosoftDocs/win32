---
description: The CreateAudioMediaType function initializes a media type from a WAVEFORMATEX structure.
ms.assetid: 2571b7b4-86e9-443f-a99d-9ba48f469522
title: CreateAudioMediaType function (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- CreateAudioMediaType
api_type:
- LibDef
api_location:
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CreateAudioMediaType function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CreateAudioMediaType** function initializes a media type from a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.

## Syntax


```C++
HRESULT STDAPI CreateAudioMediaType(
   const WAVEFORMATEX  *pwfx,
         AM_MEDIA_TYPE *pmt,
         BOOL          bSetFormat
);
```



## Parameters

<dl> <dt>

*pwfx* 
</dt> <dd>

Pointer to the supplied [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure to initialize.

</dd> <dt>

*bSetFormat* 
</dt> <dd>

Flag indicating whether to initialize the format block. Specify **TRUE** to initialize it, or **FALSE** otherwise.

</dd> </dl>

## Return value

Returns E\_OUTOFMEMORY if memory could not be allocated for the format data; S\_OK otherwise.

## Remarks

If the *bSetFormat* parameter is **TRUE**, the method allocates the memory for the format block. If the *pmt* parameter already contains an allocated format block, a memory leak will occur. To avoid a memory leak, call [**FreeMediaType**](freemediatype.md) before calling this function. After the method returns, call **FreeMediaType** again to free the format block.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**Media Type Functions**](media-type-functions.md)
</dt> </dl>

 

