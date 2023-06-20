---
description: "Learn about the CMediaType.CMediaType constructor (Mtype.h) method. This method uses the 'mtype' and 'phr' parameters."
ms.assetid: b7d5264a-2a5f-4111-96bb-1ea2b13405be
title: CMediaType.CMediaType constructor (Mtype.h) - mtype and phr parameters
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CMediaType.CMediaType constructor (Mtype.h) - mtype and phr parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CMediaType(
  [ref] const AM_MEDIA_TYPE &mtype,
              HRESULT       *phr = NULL
);
```



## Parameters

<dl> <dt>

*mtype* \[ref\]
</dt> <dd>

Reference to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. The constructor copies the media type to the new object, including the format block, if any.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an HRESULT value. This parameter can be a **NULL** pointer. Otherwise, the caller must set the value to S\_OK before calling the constructor. If the constructor fails, it sets the value to a failure code.

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

 

 




