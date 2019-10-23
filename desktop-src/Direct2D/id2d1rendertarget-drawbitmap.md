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

Draws the specified [**ID2D1Bitmap**](https://msdn.microsoft.com/en-us/library/Dd371109(v=VS.85).aspx).

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                     |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F&)**](https://msdn.microsoft.com/en-us/library/Dd371880(v=VS.85).aspx)   | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F&,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](https://msdn.microsoft.com/en-us/library/Dd371878(v=VS.85).aspx)  | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |
| [**DrawBitmap(ID2D1Bitmap\*,D2D1\_RECT\_F\*,FLOAT,D2D1\_BITMAP\_INTERPOLATION\_MODE,D2D1\_RECT\_F\*)**](https://msdn.microsoft.com/en-us/library/Dd371876(v=VS.85).aspx) | Draws the specified bitmap after scaling it to the size of the specified rectangle. <br/> |



## Remarks

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawBitmap**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/en-us/library/Dd316801(v=VS.85).aspx) methods.

## Examples

For an example, see [How to Draw a Bitmap](how-to-draw-a-bitmap.md). For an example showing how to load a bitmap from a resource or a file, see [How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md) and [How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371766(v=VS.85).aspx)
</dt> <dt>

[How to Draw a Bitmap](how-to-draw-a-bitmap.md)
</dt> <dt>

[How to Load a Bitmap from a Resource](how-to-load-a-bitmap-from-a-resource.md)
</dt> <dt>

[How to Load a Bitmap from a File](how-to-load-a-direct2d-bitmap-from-a-file.md)
</dt> </dl>

 

 





