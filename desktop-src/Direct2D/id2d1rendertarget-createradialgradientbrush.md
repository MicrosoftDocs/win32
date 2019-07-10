---
title: ID2D1RenderTarget CreateRadialGradientBrush methods
description: Creates an ID2D1RadialGradientBrush object that can be used to paint areas with a radial gradient.
ms.assetid: 985a4c1b-d29b-46ed-bc55-6dcd313718a8
keywords:
- CreateRadialGradientBrush methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
---

# ID2D1RenderTarget::CreateRadialGradientBrush methods

Creates an [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx) object that can be used to paint areas with a radial gradient.

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371859(v=VS.85).aspx)                            | Creates an [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx) that contains the specified gradient stops, has no transform, and has a base opacity of 1.0. <br/> |
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES&,D2D1\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371861(v=VS.85).aspx)   | Creates an [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371855(v=VS.85).aspx) | Creates an [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/Dd371529(v=VS.85).aspx) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |



## Examples

For an example, see [How to Create a Radial Gradient Brush](how-to-create-a-radial-gradient-brush.md).

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

[How to Create a Radial Gradient Brush](how-to-create-a-radial-gradient-brush.md)
</dt> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> </dl>

�

�





