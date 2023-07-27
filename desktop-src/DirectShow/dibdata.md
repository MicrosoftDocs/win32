---
description: The DIBDATA structure contains information about a GDI device-independent bitmap (DIB).
ms.assetid: 'abbfa5b4-8789-4a44-a467-5812d3cc8238'
title: DIBDATA structure (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIBDATA
api_type: 
- HeaderDef
api_location: 
- Winutil.h
ms.custom: UpdateFrequency5
---

# DIBDATA structure

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 




