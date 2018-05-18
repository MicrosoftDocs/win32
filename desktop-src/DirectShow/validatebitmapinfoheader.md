---
Description: 'The ValidateBitmapInfoHeader function checks a BITMAPINFOHEADER structure for certain common errors that can cause buffer overruns or integer overflows.'
ms.assetid: 'a797c286-ed77-437f-9ec1-1ef3a189bf62'
title: ValidateBitmapInfoHeader function
---

# ValidateBitmapInfoHeader function

The `ValidateBitmapInfoHeader` function checks a [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure for certain common errors that can cause buffer overruns or integer overflows.

> [!Note]  
> This function does not guarantee that the [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure is valid or that code using the structure is secure.

 

## Syntax


```C++
BOOL ValidateBitmapInfoHeader(
   const BITMAPINFOHEADER *pbmi,
         DWORD            cbSize
);
```



## Parameters

<dl> <dt>

*pbmi* 
</dt> <dd>

Pointer to the [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure to validate.

</dd> <dt>

*cbSize* 
</dt> <dd>

Size of the memory block that holds the structure, in bytes.

</dd> </dl>

## Return value

Returns a Boolean value. If the value is **FALSE**, the [**BITMAPINFOHEADER**](bitmapinfoheader.md) structure is not valid.

## Remarks

This function guards against the following errors:

-   Arithmetic overflow in the structure size or an invalid structure size.
-   Invalid value for the **biClrUsed** member.
-   Arithmetic overflow in the image size (**biSizeImage**).
-   Invalid values for the image size (**biSizeImage**) for RGB formats.

The function does not check whether the structure describes a valid video format.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Checkbmi.h</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




