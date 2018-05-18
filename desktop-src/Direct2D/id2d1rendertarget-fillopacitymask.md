---
title: ID2D1RenderTarget FillOpacityMask methods
description: Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target.
ms.assetid: 'a5e56d8a-2929-4f7b-b1c4-fb358c202721'
keywords: ["FillOpacityMask methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::FillOpacityMask methods

Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target.

### Overload list



| Method                                                                                                                                                                                                                          | Description                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**FillOpacityMask(ID2D1Bitmap\*,ID2D1Brush\*,D2D1\_OPACITY\_MASK\_CONTENT,D2D\_RECT\_F&,D2D\_RECT\_F&)**](id2d1rendertarget-fillopacitymask-ptr-id2d1bitmap-ptr-id2d1brush-ref-d2d-rect-f-ref-d2d-rect-f-d2d1-gamma.md)       | Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target. <br/> |
| [**FillOpacityMask(ID2D1Bitmap\*,ID2D1Brush\*,D2D1\_OPACITY\_MASK\_CONTENT,D2D\_RECT\_F\*,D2D\_RECT\_F\*)**](id2d1rendertarget-fillopacitymask-ptr-id2d1bitmap-ptr-id2d1brush-ptr-d2d-rect-f-ptr-d2d-rect-f-ptr-d2d1-gamma.md) | Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target. <br/> |



## Remarks

For this method to work properly, the render target must be using the [**D2D1\_ANTIALIAS\_MODE\_ALIASED**](d2d1-antialias-mode.md) antialiasing mode. You can set the antialiasing mode by calling the [**ID2D1RenderTarget::SetAntialiasMode**](id2d1rendertarget-setantialiasmode.md) method.

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **FillOpacityMask**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](id2d1rendertarget-enddraw.md) or [**ID2D1RenderTarget::Flush**](id2d1rendertarget-flush.md) methods.

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](id2d1rendertarget.md)
</dt> </dl>

 

 





