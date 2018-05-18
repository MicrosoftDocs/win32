---
Description: 'The CheckVideoInfoType function checks a media type that contains a VIDEOINFOHEADER format structure for certain common errors that can cause buffer overruns or integer overflows.'
ms.assetid: '7ffca7de-26f9-4d8d-b70e-231eca462211'
title: CheckVideoInfoType function
---

# CheckVideoInfoType function

The `CheckVideoInfoType` function checks a media type that contains a [**VIDEOINFOHEADER**](videoinfoheader.md) format structure for certain common errors that can cause buffer overruns or integer overflows.

> [!Note]  
> This function does not guarantee that the media type is valid or that code using the structure is secure.

 

## Syntax


```C++
HRESULT CheckVideoInfoType(
   const AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to the [**AM\_MEDIA\_TYPE**](am-media-type.md) structure to validate

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                                | Description                        |
|------------------------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer value.<br/> |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | Invalid media type.<br/>     |



 

## Remarks

This function calls [**ValidateBitmapInfoHeader**](validatebitmapinfoheader.md) to validate the [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure in the media type. If the format type is not FORMAT\_VideoInfo, the function returns VFW\_E\_TYPE\_NOT\_ACCEPTED.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Checkbmi.h</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




