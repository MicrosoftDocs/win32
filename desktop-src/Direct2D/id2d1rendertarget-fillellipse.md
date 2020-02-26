---
title: ID2D1RenderTarget FillEllipse methods (D2d1.h)
description: Paints the interior of the specified ellipse.
ms.assetid: 149fb303-d2e8-416c-b28f-8bc5f1482ba6
keywords:
- FillEllipse methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::FillEllipse methods

Paints the interior of the specified ellipse.

### Overload list



| Method                                                                                                             | Description                                               |
|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------|
| [**FillEllipse(D2D1\_ELLIPSE&,ID2D1Brush\*)**](https://msdn.microsoft.com/library/Dd371930(v=VS.85).aspx)  | Paints the interior of the specified ellipse. <br/> |
| [**FillEllipse(D2D1\_ELLIPSE\*,ID2D1Brush\*)**](https://msdn.microsoft.com/library/Dd371928(v=VS.85).aspx) | Paints the interior of the specified ellipse. <br/> |



## Remarks

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **FillEllipse**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/library/Dd316801(v=VS.85).aspx) methods.

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

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> <dt>

[How to Draw and Fill a Basic Shape](how-to-draw-an-ellipse.md)
</dt> </dl>

�

�





