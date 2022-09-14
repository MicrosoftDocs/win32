---
title: ID2D1RenderTarget CreateRadialGradientBrush methods (D2d1.h)
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
ms.topic: reference
---

# ID2D1RenderTarget::CreateRadialGradientBrush methods

Creates an [**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) object that can be used to paint areas with a radial gradient.

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createradialgradientbrush(constd2d1_radial_gradient_brush_properties__id2d1gradientstopcollection_id2d1radialgradientbrush))                            | Creates an [**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) that contains the specified gradient stops, has no transform, and has a base opacity of 1.0. <br/> |
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES&,D2D1\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createradialgradientbrush(constd2d1_radial_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1radialgradientbrush))   | Creates an [**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |
| [**CreateRadialGradientBrush(D2D1\_RADIAL\_GRADIENT\_BRUSH\_PROPERTIES\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1GradientStopCollection\*,ID2D1RadialGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createradialgradientbrush(constd2d1_radial_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1radialgradientbrush)) | Creates an [**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |



## Examples

For an example, see [How to Create a Radial Gradient Brush](how-to-create-a-radial-gradient-brush.md).

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> <dt>

[How to Create a Radial Gradient Brush](how-to-create-a-radial-gradient-brush.md)
</dt> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> </dl>

�

�
