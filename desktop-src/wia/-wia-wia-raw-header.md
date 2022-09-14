---
description: The WIA\_RAW\_HEADER structure defines an image in the RAW data format of a device and enables applications to use RAW format in Windows Image Acquisition (WIA) transfers.
ms.assetid: c7b50816-d596-4c62-a00e-cd8d6e303e42
title: WIA_RAW_HEADER structure (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_RAW_HEADER
api_type: 
- HeaderDef
api_location: 
- Wiadef.h
---

# WIA\_RAW\_HEADER structure

The **WIA\_RAW\_HEADER** structure defines an image in the RAW data format of a device and enables applications to use RAW format in Windows Image Acquisition (WIA) transfers.

## Syntax


```C++
typedef struct _WIA_RAW_HEADER {
  DWORD Tag;
  DWORD Version;
  DWORD HeaderSize;
  DWORD XRes;
  DWORD YRes;
  DWORD XExtent;
  DWORD YExtent;
  DWORD BytesPerLine;
  DWORD BitsPerPixel;
  DWORD ChannelsPerPixel;
  DWORD DataType;
  BYTE  BitsPerChannel[8];
  DWORD Compression;
  DWORD PhotometricInterp;
  DWORD LineOrder;
  DWORD RawDataOffset;
  DWORD RawDataSize;
  DWORD PaletteOffset;
  DWORD PaletteSize;
} WIA_RAW_HEADER;
```



## Members

<dl> <dt>

**Tag**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The name of the format. This must be the literal 'WRAW' (four single byte ASCII characters).

</dd> <dt>

**Version**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The version of the RAW format. Always use 0x00010000.

</dd> <dt>

**HeaderSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The total valid bytes in the header.

</dd> <dt>

**XRes**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The horizontal resolution in dots per inch.

</dd> <dt>

**YRes**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The vertical resolution in dots per inch.

</dd> <dt>

**XExtent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The width of the image in pixels.

</dd> <dt>

**YExtent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The height of the image in pixels.

</dd> <dt>

**BytesPerLine**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The number of bytes in a line of an uncompressed image. Use 0 when the data is compressed to signal that the number of bytes per line is unknown.

</dd> <dt>

**BitsPerPixel**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The total number of bits per pixel for all the pixel's channels.

</dd> <dt>

**ChannelsPerPixel**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The number of color channels in a pixel.

</dd> <dt>

**DataType**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The WIA\_IPA\_DATATYPE of the image. Since WIA\_IPA\_FORMAT is set to WiaImgFmt\_RAW, this is a list of allowed values from which the application picks.

</dd> <dt>

**BitsPerChannel\[8\]**
</dt> <dd>

Type: **BYTE**

</dd> <dd>

The number of bits in a channel, up to a maximum of 8.

</dd> <dt>

**Compression**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A WIA\_IPA\_COMPRESSION value specifying the type of compression used, if any.

</dd> <dt>

**PhotometricInterp**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A WIA\_IPA\_PHOTOMETRIC\_INTERP value specifying the photometric interpretation of the image.

</dd> <dt>

**LineOrder**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

A value representing the image line order. This is always either WIA\_LINE\_ORDER\_TOP\_TO\_BOTTOM or WIA\_LINE\_ORDER\_BOTTOM\_TO\_TOP.

</dd> <dt>

**RawDataOffset**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The position of the raw image data in bytes, starting from position where the header ends or the position where the palette ends.

</dd> <dt>

**RawDataSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the raw image data.

</dd> <dt>

**PaletteOffset**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The position of the palette in bytes, starting from the position where the header ends or the position where the data ends. (This value is 0, if there is no palette.)

</dd> <dt>

**PaletteSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The size, in bytes, of the palette table. (This is 0, if there is no palette.)

</dd> </dl>

## Remarks

Because this is not a file format, use an empty string for the WIA\_IPA\_FILE\_EXTENSION property.

The palette and the data can come in either order.

**RawDataSize** does not include either the header or the palette. Use this field to verify that the transfer of the image has been successful.

**PaletteSize** is bytes, not the number of entries in the palette.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




