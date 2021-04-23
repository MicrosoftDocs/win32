---
UID: NN:dwrite_3.IDWriteBitmapRenderTarget2
title: IDWriteBitmapRenderTarget2 (dwrite_3.h)
description: Encapsulates a 32-bit device independent bitmap and device context, which can be used for rendering glyphs.
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
 - IDWriteBitmapRenderTarget2
 - dwrite_3/IDWriteBitmapRenderTarget2
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
 - IDWriteBitmapRenderTarget2
---

# IDWriteBitmapRenderTarget2 interface (dwrite_3.h)

Encapsulates a 32-bit device independent bitmap and device context, which can be used for rendering glyphs.

> [!IMPORTANT]
> This API is available as part of the DWriteCore implementation of [DirectWrite](../direct-write-portal.md). DWriteCore is a form of DirectWrite that runs on versions of Windows down to Windows 8, and opens the door for you to use it cross-platform. For more info, and code examples, see [DWriteCore overview](/windows/win32/DirectWrite/dwrite/dwritecore-overview).

## Inheritance

The **IDWriteBitmapRenderTarget2** interface inherits from [IDWriteBitmapRenderTarget1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritebitmaprendertarget1).

## Methods

The **IDWriteBitmapRenderTarget2** interface has these methods.

| Method | Description |
| ---- |:---- |
| [IDWriteBitmapRenderTarget2::GetBitmapData](./nf-dwrite_3-idwritebitmaprendertarget2-getbitmapdata.md) | Retrieves the pixel data from a bitmap render target. |

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, Project Reunion [Win32 apps] |
| **Header** | dwrite_3.h (include dwrite_core.h) |
