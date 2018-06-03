---
Description: The GetBitmapSubtype function returns the media subtype GUID for the specified bitmap.
ms.assetid: 0af8a64b-8d3c-4308-9fd6-174864a1ca26
title: GetBitmapSubtype function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetBitmapSubtype function

The `GetBitmapSubtype` function returns the media subtype **GUID** for the specified bitmap.

## Syntax


```C++
const GUID GetBitmapSubtype(
   const BITMAPINFOHEADER *pHeader
);
```



## Parameters

<dl> <dt>

*pHeader* 
</dt> <dd>

Pointer to a [**BITMAPINFOHEADER**](/windows/desktop/api/WinGDI/ns-wingdi-tagbitmapinfoheader) structure.

</dd> </dl>

## Return value

Returns the media subtype **GUID**.

## Remarks

For uncompressed RGB types, this function maps the **biBitCount** field to the subtype. For compressed video types, this function uses the [**FOURCCMap**](fourccmap.md) class to map the **biCompression** field to the subtype.

If the function cannot match the format to a subtype, the return value is GUID\_NULL.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Video and Image Functions](video-and-image-functions.md)
</dt> </dl>

 

 




