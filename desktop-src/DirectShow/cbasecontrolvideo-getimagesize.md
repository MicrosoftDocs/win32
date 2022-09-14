---
description: The GetImageSize method retrieves video image size information.
ms.assetid: a6d7f949-c6a9-49e9-b10a-f6f5bd73dc00
title: CBaseControlVideo.GetImageSize method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetImageSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.GetImageSize method

The `GetImageSize` method retrieves video image size information.

## Syntax


```C++
HRESULT GetImageSize(
   VIDEOINFOHEADER *pVideoInfo,
   long            *pBufferSize,
   RECT            *pSourceRect
);
```



## Parameters

<dl> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure to be filled in.

</dd> <dt>

*pBufferSize* 
</dt> <dd>

Pointer to the size of the video buffer.

</dd> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the rectangle dimensions of the source video.

</dd> </dl>

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                  | Description                                                               |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Failure.<br/>                                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument. The data format is not compatible.<br/>           |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected error occurred. One or more arguments are **NULL**.<br/> |
| <dl> <dt>**NOERROR**</dt> </dl>       | Success.<br/>                                                       |



 

## Remarks

This member function is a helper function used for creating memory image renderings of DIB images. It is called from the base class implementation of [**CBaseControlVideo::GetCurrentImage**](cbasecontrolvideo-getcurrentimage.md) when a **NULL***pVideoImage* parameter is passed to that member function. As a result, this member function constructs and returns a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure, using the information in *pBufferSize* and *pSourceRect*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




