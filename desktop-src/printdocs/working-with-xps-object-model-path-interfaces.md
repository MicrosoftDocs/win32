---
description: This section describes how to use the path-related interfaces of the XPS Document API in an XPS OM.
ms.assetid: 4e76355a-ad53-4177-b8c7-3e768a1d4e3f
title: Working with XPS OM Path Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Working with XPS OM Path Interfaces

This section describes how to use the path-related interfaces of the XPS Document API in an XPS OM.



| Interface name                                                            | Conceptual children                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                       |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXpsOMPath**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath)<br/>                               | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Describes a graphical path element.<br/>                                                                                                                                                    |
| [**IXpsOMBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsombrush)<br/>                             | [**IXpsOMSolidColorBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomsolidcolorbrush)<br/> [**IXpsOMTileBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomtilebrush)<br/> [**IXpsOMVisualBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualbrush)<br/> [**IXpsOMImageBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomimagebrush)<br/> [**IXpsOMGradientBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientbrush)<br/> [**IXpsOMLinearGradientBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomlineargradientbrush)<br/> [**IXpsOMRadialGradientBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomradialgradientbrush)<br/> | A brush is used to fill an area or a line.<br/>                                                                                                                                             |
| [**IXpsOMSolidColorBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomsolidcolorbrush)<br/>         | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provides solid color fills or strokes. <br/>                                                                                                                                                |
| [**IXpsOMVisualBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualbrush)<br/>                 | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provides a visual object such as a path, glyph or canvas, or a partial visual to be used as a tiling fill or stroke. <br/>                                                                  |
| [**IXpsOMImageBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomimagebrush)<br/>                   | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provides an image (or partial image) to be used as a tiling fill or stroke. <br/>                                                                                                           |
| [**IXpsOMLinearGradientBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomlineargradientbrush)<br/> | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provides a linear gradient to be used as a fill or stroke. <br/>                                                                                                                            |
| [**IXpsOMRadialGradientBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomradialgradientbrush)<br/> | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Provides a radial gradient to be used as a fill or stroke. <br/>                                                                                                                            |
| [**IXpsOMGradientStop**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientstop)<br/>               | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Defines a single color value inflection point within a linear or radial gradient. <br/>                                                                                                     |
| [**IXpsOMGeometry**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometry)<br/>                       | [**IXpsOMGeometryFigure**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometryfigure)<br/>                                                                                                                                                                                                                                                                                                                                                                                             | Provides a definition of a vector region to be used as a clipping region or path definition. Consists of one or more [**IXpsOMGeometryFigure**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometryfigure) interfaces. <br/> |
| [**IXpsOMGeometryFigure**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometryfigure)<br/>           | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Part of a region definition that is referenced by an [**IXpsOMGeometry**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometry) interface and that consists of one or more segments. <br/>                                    |
| [**IXpsOMMatrixTransform**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsommatrixtransform)<br/>         | None<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | Specifies the affine matrix transformation to be applied to the object during rendering. <br/>                                                                                              |



 

## Contents

-   [XPS OM Brushes](xps-object-model-brushes.md)
-   [XPS OM Gradients](xps-object-model-gradients.md)
-   [XPS OM Geometry Objects](xps-object-model-geometry-objects.md)

## Related topics

<dl> <dt>

[**IXpsOMPath Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath)
</dt> <dt>

[**IXpsOMDashCollection Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdashcollection)
</dt> <dt>

[**IXpsOMMatrixTransform Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsommatrixtransform)
</dt> </dl>

 

 




