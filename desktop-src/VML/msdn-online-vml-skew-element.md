---
title: VML Skew Element
description: VML Skew Element
ms.assetid: ab58bbd9-5fb2-434f-adea-9b3d2d170804
ms.topic: article
ms.date: 05/31/2018
---

# VML Skew Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a skew for a shape.

The following attributes modify a skew.



| Attribute                                 | Description                                    |
|-------------------------------------------|------------------------------------------------|
| [Ext](ext-attribute--skew--vml.md)       | Defines the way a skew is displayed.           |
| [ID](id-attribute--skew--vml.md)         | Defines a unique identifier for a skew.        |
| [Matrix](matrix-attribute--skew--vml.md) | Defines a perspective transform for a skew.    |
| [Offset](offset-attribute--skew--vml.md) | Defines the offset of a skew.                  |
| [On](on-attribute--skew--vml.md)         | Determines whether the skew will be displayed. |
| [Origin](origin-attribute--skew--vml.md) | Determines the origin of a skew.               |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

In addition, the [Matrix](matrix-attribute--skew--vml.md) and [On](on-attribute--skew--vml.md) attributes must be set to **True**.

The following is the minimum code needed to produce a skew.


```HTML
   <v:rect
   fillcolor="green"
   style="position:relative;top:1;left:1;width:50;height:50">
   <o:skew on="t" matrix="1,-0.5,0,0.75,0,0"/>
   </v:rect>
```



The **Skew** element is a Microsoft Office Extension to VML.

**Examples**

-   [Simple Skew Example](/previous-versions/bb229482(v=vs.85))
-   [Dynamic Skew Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/skew/x_skew.md)

 

 