---
title: VML Stroke Element
description: VML Stroke Element
ms.assetid: 300ecde5-f19d-4ff7-89a4-af9b8e82ae9d
ms.topic: article
ms.date: 05/31/2018
---

# VML Stroke Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a stroke for a shape.

The following attributes modify a stroke.



| Attribute                                                          | Description                                                   |
|--------------------------------------------------------------------|---------------------------------------------------------------|
| [AltHRef](althref-attribute--stroke--vml.md)                      | Specifies an alternate reference for a stroke.                |
| [Color](color-attribute--stroke--vml.md)                          | Defines the color of a stroke.                                |
| [Color2](color2-attribute--stroke--vml.md)                        | Defines a second color for a stroke.                          |
| [DashStyle](msdn-online-vml-dashstyle-attribute.md)               | Specifies the dot and dash pattern for a stroke.              |
| [EndArrow](msdn-online-vml-endarrow-attribute.md)                 | Defines an arrowhead style for the end of a stroke.           |
| [EndArrowLength](msdn-online-vml-endarrowlength-attribute.md)     | Defines an arrowhead length for the end of a stroke.          |
| [EndArrowWidth](msdn-online-vml-endarrowwidth-attribute.md)       | Defines an arrowhead width for the end of a stroke.           |
| [EndCap](msdn-online-vml-endcap-attribute.md)                     | Defines the cap style for the end of a stroke.                |
| [FillType](msdn-online-vml-filltype-attribute.md)                 | Defines the type of fill used for the background of a stroke. |
| [HRef](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/bb229431(v=vs.85))    | Defines the URL to the original image for the stroke.         |
| [ID](id-attribute--stroke--vml.md)                                | Defines a unique identifier for the stroke.                   |
| [ImageAlignShape](msdn-online-vml-imagealignshape-attribute.md)   | Determines the alignment of a stroke image.                   |
| [ImageAspect](msdn-online-vml-imageaspect-attribute.md)           | Defines how the stroke image aspect ratio will be preserved.  |
| [ImageSize](msdn-online-vml-imagesize-attribute.md)               | Defines the size of the image for the stroke.                 |
| [JoinStyle](msdn-online-vml-joinstyle-attribute.md)               | Defines the join style of a polyline.                         |
| [LineStyle](msdn-online-vml-linestyle-attribute.md)               | Defines the line style of a stroke.                           |
| [MiterLimit](msdn-online-vml-miterlimit-attribute.md)             | Defines the smoothness of a miter joint.                      |
| [On](on-attribute--stroke--vml.md)                                | Determines whether the stroke will be displayed.              |
| [Opacity](opacity-attribute--stroke--vml.md)                      | Defines the amount of transparency of a stroke.               |
| [Src](src-attribute--stroke--vml.md)                              | Defines the source image to load for a stroke fill.           |
| [StartArrow](msdn-online-vml-startarrow-attribute.md)             | Defines the arrowhead for the start of a stroke.              |
| [StartArrowLength](msdn-online-vml-startarrowlength-attribute.md) | Defines the arrowhead length for the start of a stroke.       |
| [StartArrowWidth](msdn-online-vml-startarrowwidth-attribute.md)   | Defines the arrowhead width for the start of a stroke.        |
| [Title](title-attribute--stroke--vml.md)                          | Defines the title of a stroke.                                |
| [Weight](msdn-online-vml-weight-attribute.md)                     | Defines the thickness of a stroke.                            |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

The following code shows how the **Stroke** element can be used to modify a line.


```HTML
   <v:line
   to="300pt,50pt" from="50pt,50pt">
   <v:stroke weight="50pt" color="red" linestyle="ThickThin"/>
   </v:line>
```



**Examples**

-   [Simple Stroke Example](/previous-versions/bb229466(v=vs.85))
-   [Stroke Image Example](/previous-versions/bb229468(v=vs.85))

 

 