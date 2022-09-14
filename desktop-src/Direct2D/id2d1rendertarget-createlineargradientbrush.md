---
title: ID2D1RenderTarget CreateLinearGradientBrush methods (D2d1.h)
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

Creates an [**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) object for painting areas with a linear gradient.

### Overload list



| Method                                                                                                                                                                                                                       | Description                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlineargradientbrush(constd2d1_linear_gradient_brush_properties__id2d1gradientstopcollection_id2d1lineargradientbrush))                            | Creates an [**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) that contains the specified gradient stops, has no transform, and has a base opacity of 1.0. <br/> |
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES&,D2D1\_BRUSH\_PROPERTIES&,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlineargradientbrush(constd2d1_linear_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1lineargradientbrush))   | Creates an [**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |
| [**CreateLinearGradientBrush(D2D1\_LINEAR\_GRADIENT\_BRUSH\_PROPERTIES\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1GradientStopCollection\*,ID2D1LinearGradientBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlineargradientbrush(constd2d1_linear_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1lineargradientbrush)) | Creates an [**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) that contains the specified gradient stops and has the specified transform and base opacity. <br/> |



## Examples

For an example showing how to create a gradient stop collection and use it to define a linear gradient, see [How to Create a Linear Gradient Brush](how-to-create-a-linear-gradient-brush.md).

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

[**CreateGradientStopCollection**](id2d1rendertarget-creategradientstopcollection.md)
</dt> <dt>

[**ID2D1GradientStopCollection**](/windows/win32/api/d2d1/nn-d2d1-id2d1gradientstopcollection)
</dt> <dt>

[**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush)
</dt> <dt>

[**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush)
</dt> <dt>

[How to Create a Linear Gradient Brush](how-to-create-a-linear-gradient-brush.md)
</dt> <dt>

[Brushes Overview](direct2d-brushes-overview.md)
</dt> </dl>

�

�
