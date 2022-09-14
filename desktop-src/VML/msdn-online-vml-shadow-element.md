---
title: VML Shadow Element
description: VML Shadow Element
ms.assetid: 3e7d3e8c-45f8-4db3-95f3-7d993b7c2ef7
ms.topic: article
ms.date: 05/31/2018
---

# VML Shadow Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a shadow for a shape.

The following attributes modify a shadow.



| Attribute                                          | Description                                        |
|----------------------------------------------------|----------------------------------------------------|
| [Color](color-attribute--shadow--vml.md)          | Defines the color of a shadow.                     |
| [Color2](color2-attribute--shadow--vml.md)        | Defines the second color of a shadow.              |
| [ID](id-attribute--shadow--vml.md)                | Specifies the unique identifier of a shadow.       |
| [Matrix](matrix-attribute--shadow--vml.md)        | Defines the perspective transform of a shadow.     |
| [Obscured](msdn-online-vml-obscured-attribute.md) | Determines whether the shadow is transparent.      |
| [Offset](offset-attribute--shadow--vml.md)        | Defines how far the shadow extends past the shape. |
| [Offset2](msdn-online-vml-offset2-attribute.md)   | Defines a second offset.                           |
| [On](on-attribute--shadow--vml.md)                | Determines whether a shadow is displayed.          |
| [Opacity](opacity-attribute--shadow--vml.md)      | Determines the transparency of a shadow.           |
| [Origin](origin-attribute--shadow--vml.md)        | Defines the center of the shadow.                  |
| [Type](type-attribute--shadow--vml.md)            | Specifies the type of shadow.                      |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

In addition, the [On](on-attribute--shadow--vml.md) attribute must be set to **True**.

The following is the minimum code needed to produce a shadow.


```HTML
   <v:rect
   fillcolor="green"
   style="top:1;left:1;width:50;height:50">
   <v:shadow on="True"/>
   </v:rect>
```



You may not notice the shadow unless you increase the [Offset](offset-attribute--shadow--vml.md) values, since the default offset is 2pt,2pt.

**Examples**

-   [Simple Shadow Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/shadow/t_shadow.md)
-   [Dynamic Shadow Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/shadow/x_shadow.md)

 

 