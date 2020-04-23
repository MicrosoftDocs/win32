---
title: ID2D1RenderTarget PushAxisAlignedClip methods (D2d1\_1.h)
description: Specifies a rectangle to which all subsequent drawing operations are clipped.
ms.assetid: 8b777425-07b1-4494-889a-0c947fb61315
keywords:
- PushAxisAlignedClip methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::PushAxisAlignedClip methods

Specifies a rectangle to which all subsequent drawing operations are clipped.

### Overload list



| Method                                                                                                                                         | Description                                                                               |
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**PushAxisAlignedClip(D2D1\_RECT\_F&,D2D1\_ANTIALIAS\_MODE)**](https://msdn.microsoft.com/library/Dd316860(v=VS.85).aspx)  | Specifies a rectangle to which all subsequent drawing operations are clipped. <br/> |
| [**PushAxisAlignedClip(D2D1\_RECT\_F\*,D2D1\_ANTIALIAS\_MODE)**](https://msdn.microsoft.com/library/Dd316856(v=VS.85).aspx) | Specifies a rectangle to which all subsequent drawing operations are clipped. <br/> |



## Remarks

A [**PushAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316860(v=VS.85).aspx) and [**PopAxisAlignedClip**](https://msdn.microsoft.com/library/Dd316850(v=VS.85).aspx) pair can occur around or within a [**PushLayer**](https://msdn.microsoft.com/library/Dd742856(v=VS.85).aspx) and [**PopLayer**](https://msdn.microsoft.com/library/Dd316852(v=VS.85).aspx), but cannot overlap. For example, the sequence of **PushAxisAlignedClip**, [**PushLayer**](https://msdn.microsoft.com/library/Dd316869(v=VS.85).aspx), **PopLayer**, **PopAxisAlignedClip** is valid, but the sequence of **PushAxisAlignedClip**, **PushLayer**, **PopAxisAlignedClip**, **PopLayer** is invalid.

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **PushAxisAlignedClip**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/library/Dd316801(v=VS.85).aspx) methods.

## Examples

For an example, see the [How to Clip with an Axis-Aligned Clip Rectangle](how-to-clip-with-axis-aligned-rects.md).

## Requirements



|                    |                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1\_1.h (include D2d1.h)</dt> </dl> |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl>                   |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> </dl>

�

�





