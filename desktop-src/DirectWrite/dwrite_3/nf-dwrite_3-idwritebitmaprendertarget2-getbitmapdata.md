---
UID: NF:dwrite_3.IDWriteBitmapRenderTarget2.GetBitmapData
title: IDWriteBitmapRenderTarget2::GetBitmapData (dwrite_3.h)
description: Retrieves the pixel data from a bitmap render target.
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
req.lib: Dwrite.lib
req.dll: Dwrite.dll
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - IDWriteBitmapRenderTarget2::GetBitmapData
 - dwrite_3/IDWriteBitmapRenderTarget2::GetBitmapData
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - COM
api_location:
 - dwrite.dll
api_name:
 - IDWriteBitmapRenderTarget2.GetBitmapData
---

# IDWriteBitmapRenderTarget2::GetBitmapData method (dwrite_3.h)

Retrieves the pixel data from a bitmap render target.

> [!IMPORTANT]
> This API is available as part of the DWriteCore implementation of [DirectWrite](../direct-write-portal.md). DWriteCore is a form of DirectWrite that runs on versions of Windows down to Windows 8, and opens the door for you to use it cross-platform. For more info, and code examples, see [DWriteCore overview](../dwritecore-overview.md).

## Syntax

```cpp
HRESULT GetBitmapData(
  _Out_ DWRITE_BITMAP_DATA_BGRA32* bitmapData
);
```

## Parameters

`bitmapData`

Type: \_Out\_**[DWRITE_BITMAP_DATA_BGRA32](./ns-dwrite_3-dwrite_bitmap_data_bgra32.md)\***

A pointer to the pixel data.

## Return value

Type: <b>HRESULT</b>

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Examples

See the [DWriteCore overview](../dwritecore-overview.md) topic, and the [DWriteCoreGallery](https://github.com/microsoft/Project-Reunion-Samples/tree/main/DWriteCore/DWriteCoreGallery) sample app.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, Project Reunion [Win32 apps] |
| **Header** | dwrite_3.h (include dwrite_core.h) |
| **Library** | Dwrite.lib |
| **DLL** | Dwrite.dll |

## See also

[IDWriteBitmapRenderTarget2](/windows/win32/api/dwrite_1/nn-dwrite_3-idwritebitmaprendertarget2)