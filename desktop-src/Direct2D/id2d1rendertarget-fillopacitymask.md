---
title: ID2D1RenderTarget FillOpacityMask methods
description: Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target.
ms.assetid: a5e56d8a-2929-4f7b-b1c4-fb358c202721
keywords:
- FillOpacityMask methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID2D1RenderTarget::FillOpacityMask methods

Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target.

### Overload list



| Method                                                                                                                                                                                                                          | Description                                                                                                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**FillOpacityMask(ID2D1Bitmap\*,ID2D1Brush\*,D2D1\_OPACITY\_MASK\_CONTENT,D2D\_RECT\_F&,D2D\_RECT\_F&)**](/windows/win32/d2d1/?branch=master)       | Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target. <br/> |
| [**FillOpacityMask(ID2D1Bitmap\*,ID2D1Brush\*,D2D1\_OPACITY\_MASK\_CONTENT,D2D\_RECT\_F\*,D2D\_RECT\_F\*)**](/windows/win32/d2d1/?branch=master) | Applies the opacity mask described by the specified bitmap to a brush and uses that brush to paint a region of the render target. <br/> |



## Remarks

For this method to work properly, the render target must be using the [**D2D1\_ANTIALIAS\_MODE\_ALIASED**](/windows/win32/d2d1/ne-d2d1-d2d1_antialias_mode?branch=master) antialiasing mode. You can set the antialiasing mode by calling the [**ID2D1RenderTarget::SetAntialiasMode**](/windows/win32/d2d1/?branch=master) method.

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **FillOpacityMask**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](/windows/win32/d2d1/?branch=master) or [**ID2D1RenderTarget::Flush**](/windows/win32/d2d1/?branch=master) methods.

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/d2d1/?branch=master)
</dt> </dl>

 

 





