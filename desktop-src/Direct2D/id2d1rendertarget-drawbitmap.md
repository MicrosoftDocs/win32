---
title: ID2D1RenderTarget DrawBitmap methods
description: Draws the specified ID2D1Bitmap.
ms.assetid: 241df698-ca5e-4d94-902a-a9e140820c14
keywords:
- DrawBitmap methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
api_name: 
---

# ID2D1RenderTarget::DrawBitmap methods

Draws the specified [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap).

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F&)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawbitmap(id2d1bitmap_constd2d1_rect_f__float_d2d1_bitmap_interpolation_mode_constd2d1_rect_f_))   | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawbitmap(id2d1bitmap_constd2d1_rect_f__float_d2d1_bitmap_interpolation_mode_constd2d1_rect_f))  | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F\*,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawbitmap(id2d1bitmap_constd2d1_rect_f_float_d2d1_bitmap_interpolation_mode_constd2d1_rect_f)) | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |



## Remarks

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawBitmap**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) or [**ID2D1RenderTarget::Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) methods.

## Examples

For an example, see [How to Draw a Bitmap](how-to-draw-a-bitmap.md). For an example showing how to load a bitmap from a resource or a file, see [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md) and [How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md).

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> <dt>

[How to Draw a Bitmap](how-to-draw-a-bitmap.md)
</dt> <dt>

[How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md)
</dt> <dt>

[How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md)
</dt> </dl>

 

