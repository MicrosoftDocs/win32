---
title: ID2D1RenderTarget CreateBitmapBrush methods
description: Creates an ID2D1BitmapBrush from the specified bitmap.
ms.assetid: '7f6ef07e-4271-4605-aced-f191a0fe65af'
keywords: ["CreateBitmapBrush methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::CreateBitmapBrush methods

Creates an [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) from the specified bitmap.

### Overload list



| Method                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                      |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateBitmapBrush(ID2D1Bitmap\*,D2D1\_BITMAP\_BRUSH\_PROPERTIES&,D2D1\_BRUSH\_PROPERTIES&,ID2D1BitmapBrush\*\*)**](id2d1rendertarget-createbitmapbrush-ptr-id2d1bitmap-ref-d2d1-bitmap-brush-properties-ref-d2d1-brush-properties-ptr-ptr-id2d1bitmapbrush.md)   | Creates an [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) from the specified bitmap.<br/>                                                                                                    |
| [**CreateBitmapBrush(ID2D1Bitmap\*,D2D1\_BITMAP\_BRUSH\_PROPERTIES\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1BitmapBrush\*\*)**](id2d1rendertarget-createbitmapbrush-ptr-id2d1bitmap-ptr-d2d1-bitmap-brush-properties-ptr-d2d1-brush-properties-ptr-ptr-id2d1bitmapbrush.md) | Creates an [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) from the specified bitmap.<br/>                                                                                                    |
| [**CreateBitmapBrush(ID2D1Bitmap\*,ID2D1BitmapBrush\*\*)**](id2d1rendertarget-createbitmapbrush-ptr-id2d1bitmap-ptr-ptr-id2d1bitmapbrush.md)                                                                                                                        | Creates an [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) from the specified bitmap. The brush uses the default values for its extend mode, interpolation mode, opacity, and transform.<br/> |
| [**CreateBitmapBrush(ID2D1Bitmap\*,D2D1\_BITMAP\_BRUSH\_PROPERTIES&,ID2D1BitmapBrush\*\*)**](id2d1rendertarget-createbitmapbrush-ptr-id2d1bitmap-ref-d2d1-bitmap-brush-properties-ptr-ptr-id2d1bitmapbrush.md)                                                      | Creates an [**ID2D1BitmapBrush**](id2d1bitmapbrush.md) from the specified bitmap. The brush uses the default values for its opacity and transform.<br/>                                   |



## Examples

For an example showing how to paint an area with a bitmap brush, see [How to Create a Bitmap Brush](how-to-create-a-bitmap-brush.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](id2d1rendertarget.md)
</dt> <dt>

[How to Create a Bitmap Brush](how-to-create-a-bitmap-brush.md)
</dt> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> </dl>

 

 





