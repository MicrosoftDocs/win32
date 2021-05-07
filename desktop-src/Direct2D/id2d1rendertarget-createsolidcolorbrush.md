---
title: ID2D1RenderTarget CreateSolidColorBrush methods (D2d1.h)
description: Creates a new ID2D1SolidColorBrush that can be used to paint areas with a solid color.
ms.assetid: 3dbfe26f-cf36-47b0-925e-4934e0d7c390
keywords:
- CreateSolidColorBrush methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::CreateSolidColorBrush methods

Creates a new [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush)) that can be used to paint areas with a solid color.

### Overload list



| Method                                                                                                                                                                                                           | Description                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateSolidColorBrush(D2D1\_COLOR\_F&,ID2D1SolidColorBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush))                                                      | Creates a new [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush)) that has the specified color and a base opacity of 1.0f. <br/> |
| [**CreateSolidColorBrush(D2D1\_COLOR\_F&,D2D1\_BRUSH\_PROPERTIES&,ID2D1SolidColorBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush))   | Creates a new [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush)) that has the specified color and opacity. <br/>                |
| [**CreateSolidColorBrush(D2D1\_COLOR\_F\*,D2D1\_BRUSH\_PROPERTIES\*,ID2D1SolidColorBrush\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush)) | Creates a new [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createsolidcolorbrush(constd2d1_color_f__constd2d1_brush_properties__id2d1solidcolorbrush)) that has the specified color and opacity. <br/>                |



## Examples

For an example, see [How to Create a Solid Color Brush](how-to-create-a-solid-color-brush.md).

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

[Brushes Overview](direct2d-brushes-overview.md)
</dt> <dt>

[Direct2D QuickStart](getting-started-with-direct2d.md)
</dt> </dl>

�

�