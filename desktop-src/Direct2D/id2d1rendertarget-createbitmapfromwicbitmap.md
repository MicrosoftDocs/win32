---
title: ID2D1RenderTarget CreateBitmapFromWicBitmap methods
description: Creates an ID2D1Bitmap by copying the specified Microsoft Windows Imaging Component (WIC) bitmap.
ms.assetid: 463fc2f9-8ec6-47e8-8d48-a9015616e656
keywords:
- CreateBitmapFromWicBitmap methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID2D1RenderTarget::CreateBitmapFromWicBitmap methods

Creates an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) by copying the specified Microsoft Windows Imaging Component (WIC) bitmap.

### Overload list



| Method                                                                                                                                                                                                              | Description                                                                                                                         |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateBitmapFromWicBitmap(IWICBitmapSource\*,ID2D1Bitmap\*\*)**](/windows/desktop/api/d2d1/)                                                       | Creates an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) by copying the specified Microsoft Windows Imaging Component(WIC) bitmap.<br/>  |
| [**CreateBitmapFromWicBitmap(IWICBitmapSource\*,D2D1\_BITMAP\_PROPERTIES&,ID2D1Bitmap\*\*)**](/windows/desktop/api/d2d1/)  | Creates an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) by copying the specified Microsoft Windows Imaging Component (WIC) bitmap.<br/> |
| [**CreateBitmapFromWicBitmap(IWICBitmapSource\*,D2D1\_BITMAP\_PROPERTIES\*,ID2D1Bitmap\*\*)**](/windows/desktop/api/d2d1/) | Creates an [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) by copying the specified Microsoft Windows Imaging Component (WIC) bitmap.<br/> |



## Remarks

Before Direct2D can load a WIC image, it must be converted to a supported pixel format and alpha mode. For a list of supported pixel formats and alpha modes, see [Supported Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md).

## Examples

For examples, see [How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md) and [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/desktop/api/d2d1/)
</dt> <dt>

[**ID2D1Bitmap**](/windows/desktop/api/d2d1/)
</dt> <dt>

[How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md)
</dt> <dt>

[Supported Pixel Formats and Alpha Modes](supported-pixel-formats-and-alpha-modes.md)
</dt> </dl>

 

 





