---
title: ID2D1RenderTarget DrawBitmap methods
description: Draws the specified ID2D1Bitmap.
ms.assetid: '241df698-ca5e-4d94-902a-a9e140820c14'
keywords: ["DrawBitmap methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::DrawBitmap methods

Draws the specified [**ID2D1Bitmap**](id2d1bitmap.md).

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F&)**](id2d1rendertarget-drawbitmap-ptr-id2d1bitmap-ref-d2d-rect-f-float-d2d1-bitmap-interpolation-mode-ref-d2d-rect-f.md)   | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](id2d1rendertarget-drawbitmap-ptr-id2d1bitmap-ref-d2d-rect-f-float-d2d1-bitmap-interpolation-mode-ptr-d2d-rect-f.md)  | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F\*,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](id2d1rendertarget-drawbitmap-ptr-id2d1bitmap-ptr-d2d-rect-f-float-d2d1-bitmap-interpolation-mode-ptr-d2d-rect-f.md) | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |



## Remarks

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawBitmap**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](id2d1rendertarget-enddraw.md) or [**ID2D1RenderTarget::Flush**](id2d1rendertarget-flush.md) methods.

## Examples

For an example, see [How to Draw a Bitmap](how-to-draw-a-bitmap.md). For an example showing how to load a bitmap from a resource or a file, see [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md) and [How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](id2d1rendertarget.md)
</dt> <dt>

[How to Draw a Bitmap](how-to-draw-a-bitmap.md)
</dt> <dt>

[How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md)
</dt> <dt>

[How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md)
</dt> </dl>

 

 





