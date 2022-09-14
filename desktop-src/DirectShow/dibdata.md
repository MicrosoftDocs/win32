---
description: The DIBDATA structure contains information about a GDI device-independent bitmap (DIB).
ms.assetid: 'abbfa5b4-8789-4a44-a467-5812d3cc8238'
title: DIBDATA structure (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIBDATA
api_type: 
- HeaderDef
api_location: 
- Winutil.h
---

# DIBDATA structure

The `DIBDATA` structure contains information about a GDI device-independent bitmap (DIB).

## Syntax


```C++
typedef struct tagDIBDATA {
  LONG       PaletteVersion;
  DIBSECTION DibSection;
  HBITMAP    hBitmap;
  HANDLE     hMapping;
  BYTE       *pBase;
} DIBDATA;
```



## Members

<dl> <dt>

**PaletteVersion**
</dt> <dd>

This member should be incremented whenever the palette changes.

</dd> <dt>

**DibSection**
</dt> <dd>

**DIBSECTION** structure that contains information about the DIB. See the GDI documentation for details.

</dd> <dt>

**hBitmap**
</dt> <dd>

Handle to the bitmap.

</dd> <dt>

**hMapping**
</dt> <dd>

Handle to a file-mapping object that is used to share memory between GDI and a [**CImageSample**](cimagesample.md) object.

</dd> <dt>

**pBase**
</dt> <dd>

Address of the bitmap.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl> |



 

 




