---
Description: The CheckVideoInfo2Type function checks a media type that contains a VIDEOINFOHEADER2 format structure for certain common errors that can cause buffer overruns or integer overflows.
ms.assetid: 6a71ce7e-c6fc-4811-9182-67949644a0a5
title: CheckVideoInfo2Type function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CheckVideoInfo2Type function

The `CheckVideoInfo2Type` function checks a media type that contains a [**VIDEOINFOHEADER2**](/windows/win32/Dvdmedia/ns-dvdmedia-tagvideoinfoheader2?branch=master) format structure for certain common errors that can cause buffer overruns or integer overflows.

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

Pointer to the [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure to validate.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                                | Description                       |
|------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer value<br/> |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | Invalid media type<br/>     |



 

## Remarks

This function calls [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md) to validate the [**BITMAPINFOHEADER**](/windows/win32/WinGDI/ns-wingdi-tagbitmapinfoheader?branch=master) structure in the media type. If the format type is not **FORMAT\_VideoInfo2**, the function returns **VFW\_E\_TYPE\_NOT\_ACCEPTED**.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Checkbmi.h</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




