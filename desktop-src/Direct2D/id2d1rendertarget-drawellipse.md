---
title: ID2D1RenderTarget DrawEllipse methods
description: Draws the outline of an ellipse with the specified dimensions and stroke.
ms.assetid: 'dabbb399-2d72-41c3-8b2f-aea49d7ad0cb'
keywords: ["DrawEllipse methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::DrawEllipse methods

Draws the outline of an ellipse with the specified dimensions and stroke.

### Overload list



| Method                                                                                                                                                                 | Description                                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**DrawEllipse(D2D1\_ELLIPSE&,ID2D1Brush\*,FLOAT,ID2D1StrokeStyle\*)**](https://msdn.microsoft.com/en-us/library/Dd371886(v=VS.85).aspx)  | Draws the outline of the specified ellipse using the specified stroke style. <br/> |
| [**DrawEllipse(D2D1\_ELLIPSE\*,ID2D1Brush\*,FLOAT,ID2D1StrokeStyle\*)**](https://msdn.microsoft.com/en-us/library/Dd371883(v=VS.85).aspx) | Draws the outline of the specified ellipse using the specified stroke style. <br/> |



## Remarks

The **DrawEllipse** method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawEllipse**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/en-us/library/Dd316801(v=VS.85).aspx) methods.

## Examples

For an example, see [How to Draw and Fill a Basic Shape](how-to-draw-an-ellipse.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx)
</dt> <dt>

[**FillEllipse**](https://msdn.microsoft.com/en-us/library/Dd742849(v=VS.85).aspx)
</dt> </dl>

�

�





