---
description: The CheckVideoInfo2Type function checks a media type that contains a VIDEOINFOHEADER2 format structure for certain common errors that can cause buffer overruns or integer overflows.
ms.assetid: 6a71ce7e-c6fc-4811-9182-67949644a0a5
title: CheckVideoInfo2Type function (Checkbmi.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CheckVideoInfo2Type
api_type: 
- HeaderDef
api_location: 
- checkbmi.h
ms.custom: UpdateFrequency5
---

# CheckVideoInfo2Type function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckVideoInfo2Type` function checks a media type that contains a [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) format structure for certain common errors that can cause buffer overruns or integer overflows.

> [!Note]  
> This function does not guarantee that the media type is valid or that code using the structure is secure.

 

## Syntax


```C++
HRESULT CheckVideoInfo2Type(
   const AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure to validate.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                                | Description                       |
|------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer value<br/> |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | Invalid media type<br/>     |



 

## Remarks

This function calls [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md) to validate the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure in the media type. If the format type is not **FORMAT\_VideoInfo2**, the function returns **VFW\_E\_TYPE\_NOT\_ACCEPTED**.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Checkbmi.h</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




