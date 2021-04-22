---
UID: NS:dwrite_3.DWRITE_BITMAP_DATA_BGRA32
title: DWRITE_BITMAP_DATA_BGRA32 (dwrite_3.h)
description: Represents bitmap data in BGRA32 format.
tech.root: DirectWrite
ms.date: 11/11/2020
ms.topic: reference
req.header: dwrite_3.h
req.include-header: dwrite_core.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - DWRITE_BITMAP_DATA_BGRA32
 - dwrite_3/DWRITE_BITMAP_DATA_BGRA32
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - dwrite_3.h
api_name:
 - DWRITE_BITMAP_DATA_BGRA32
---

# DWRITE_BITMAP_DATA_BGRA32 structure (dwrite_3.h)

Represents bitmap data in BGRA32 format.

> [!IMPORTANT]
> This API is available as part of the DWriteCore implementation of [DirectWrite](../direct-write-portal.md). DWriteCore is a form of DirectWrite that runs on versions of Windows down to Windows 8, and opens the door for you to use it cross-platform. For more info, and code examples, see [DWriteCore overview](/windows/win32/DirectWrite/dwrite/dwritecore-overview).

## Syntax

```cpp
struct DWRITE_BITMAP_DATA_BGRA32
{
  UINT32 width;
  UINT32 height;
  _Field_size_(width * height) UINT32* pixels;
};
```

## Members

`width`

Type: **[UINT32](../../winprog/windows-data-types.md)**

The width, in pixels, of the bitmap.


`height`

Type: **[UINT32](../../winprog/windows-data-types.md)**

The height, in pixels, of the bitmap.


`pixels`

Type: \_Field\_size\_(width * height)**[UINT32](../../winprog/windows-data-types.md)\***

A pointer to the location of the bit values for the bitmap.


## Examples

See the [DWriteCore overview](/windows/win32/DirectWrite/dwrite/dwritecore-overview) topic, and the [DWriteCoreGallery](https://github.com/microsoft/Project-Reunion-Samples/tree/main/DWriteCore/DWriteCoreGallery) sample app.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, Project Reunion [Win32 apps] |
| **Header** | dwrite_3.h (include dwrite_core.h) |