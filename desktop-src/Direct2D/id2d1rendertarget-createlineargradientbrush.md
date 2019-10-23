---
title: ID2D1RenderTarget CreateLinearGradientBrush methods
description: Creates an ID2D1LinearGradientBrush object for painting areas with a linear gradient.
ms.assetid: dc07113f-ff93-4b0f-8328-02dd481dccb0
keywords:
- CreateLinearGradientBrush methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::CreateLinearGradientBrush methods

Creates an [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx) object for painting areas with a linear gradient.

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371845(v=VS.85).aspx)                            | Creates an [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx) that contains the specified gradient stops, has no transform, and has a base opacity of 1.0. <br/> |
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES&,D2D1\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371850(v=VS.85).aspx)   | Creates an [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371842(v=VS.85).aspx) | Creates an [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |



## Examples

For an example showing how to create a gradient stop collection and use it to define a linear gradient, see [How to Create a Linear Gradient Brush](how-to-create-a-linear-gradient-brush.md).

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

[**CreateGradientStopCollection**](id2d1rendertarget-creategradientstopcollection.md)
</dt> <dt>

[**ID2D1GradientStopCollection**](https://msdn.microsoft.com/en-us/library/Dd316783(v=VS.85).aspx)
</dt> <dt>

[**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371488(v=VS.85).aspx)
</dt> <dt>

[**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx)
</dt> <dt>

[How to Create a Linear Gradient Brush](how-to-create-a-linear-gradient-brush.md)
</dt> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> </dl>

�

�





