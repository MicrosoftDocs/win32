---
description: The ValidateBitmapInfoHeader function checks a BITMAPINFOHEADER structure for certain common errors that can cause buffer overruns or integer overflows.
ms.assetid: a797c286-ed77-437f-9ec1-1ef3a189bf62
title: ValidateBitmapInfoHeader function (Checkbmi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ValidateBitmapInfoHeader
api_type: 
- HeaderDef
api_location: 
- checkbmi.h
---

# ValidateBitmapInfoHeader function

The `ValidateBitmapInfoHeader` function checks a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure for certain common errors that can cause buffer overruns or integer overflows.

> [!Note]  
> This function does not guarantee that the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure is valid or that code using the structure is secure.

 

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

Pointer to the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure to validate.

</dd> <dt>

*cbSize* 
</dt> <dd>

Size of the memory block that holds the structure, in bytes.

</dd> </dl>

## Return value

Returns a Boolean value. If the value is **FALSE**, the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure is not valid.

## Remarks

This function guards against the following errors:

-   Arithmetic overflow in the structure size or an invalid structure size.
-   Invalid value for the **biClrUsed** member.
-   Arithmetic overflow in the image size (**biSizeImage**).
-   Invalid values for the image size (**biSizeImage**) for RGB formats.

The function does not check whether the structure describes a valid video format.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Checkbmi.h</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




