---
title: VML Path Element
description: VML Path Element
ms.assetid: c5b9f9e3-edee-45fa-9387-8f15e09983ee
ms.topic: article
ms.date: 05/31/2018
---

# VML Path Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a path for a shape.

The following attributes modify a shadow.



| Attribute                                                        | Description                                                                     |
|------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [Arrowok](msdn-online-vml-arrowok-attribute.md)                 | Determines whether arrowheads will be displayed.                                |
| [ConnectAngles](msdn-online-vml-connectangles-attribute.md)     | Specifies how a curve will connect to a connection point.                       |
| [ConnectLocs](msdn-online-vml-connectlocs-attribute.md)         | Defines the location of connection points on a path.                            |
| [ConnectType](msdn-online-vml-connecttype-attribute.md)         | Defines the type of connection point used for attaching shapes to other shapes. |
| [ExtrusionOK](msdn-online-vml-extrusionok-attribute.md)         | Determines whether an extrusion will be displayed.                              |
| [FillOK](msdn-online-vml-fillok-attribute.md)                   | Determines whether a fill will be displayed.                                    |
| [GradientShapeOK](msdn-online-vml-gradientshapeok-attribute.md) | Determines whether a gradient shape will be displayed.                          |
| [ID](id-attribute--path--vml.md)                                | Defines a unique identifier for a path.                                         |
| [Limo](msdn-online-vml-limo-attribute.md)                       | Defines a stretch point on the path.                                            |
| [ShadowOK](msdn-online-vml-shadowok-attribute.md)               | Determines whether a shadow will be displayed.                                  |
| [StrokeOK](msdn-online-vml-strokeok-attribute.md)               | Determines whether a stroke will be displayed.                                  |
| [TextBoxRect](msdn-online-vml-textboxrect-attribute.md)         | Defines one or more textboxes inside a shape.                                   |
| [TextPathOK](msdn-online-vml-textpathok-attribute.md)           | Determines whether a textpath will be displayed.                                |
| [V](msdn-online-vml-v-attribute.md)                             | Defines the commands that make up a path.                                       |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

The following code shows how to define a shape with a path.


```HTML
   <v:shape strokecolor="red"
   coordorigin="0 0" coordsize="200 200"
   style="top:1;left:1;width:50;height:50">
   <v:path v="m 1,1 l 1,200, 200,200, 200,1 x e"/>
   </v:shape>
```



Note that the [V](msdn-online-vml-v-attribute.md) attribute of **Path** replaces the [Path](msdn-online-vml-path-attribute.md) attribute of [Shape](shape-element--vml.md).

**Examples**

-   [Simple Path Child Element Example](/previous-versions/bb229545(v=vs.85))
-   [Dynamic Path Child Element Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/path/x_path.md)

 

 