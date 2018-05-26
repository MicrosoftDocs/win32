---
Description: The ConvertVideoInfoToVideoInfo2 function converts a media type that uses VIDEOINFOHEADER to one that uses VIDEOINFOHEADER2.
ms.assetid: d938bfc0-a5ae-475b-b183-56ff39b4bae1
title: ConvertVideoInfoToVideoInfo2 function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ConvertVideoInfoToVideoInfo2 function

The `ConvertVideoInfoToVideoInfo2` function converts a media type that uses [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) to one that uses [**VIDEOINFOHEADER2**](/windows/win32/Dvdmedia/ns-dvdmedia-tagvideoinfoheader2?branch=master).

## Syntax


```C++
HRESULT STDAPI ConvertVideoInfoToVideoInfo2(
   AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to the [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure to convert. The structure must have format type FORMAT\_VideoInfo.

</dd> </dl>

## Return value

Returns S\_OK or E\_OUTOFMEMORY.

## Remarks

This function allocates a new **VIDEOINFOHEADER2** structure, copies the members of the **VIDEOINFOHEADER** structure into it, and replaces the old structure with the new structure in the format block of the media type.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




