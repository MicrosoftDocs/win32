---
title: VML Fill Element
description: VML Fill Element
ms.assetid: ea790017-5aaa-4e75-8fc7-77fc94fd1d1e
ms.topic: article
ms.date: 05/31/2018
---

# VML Fill Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a fill for a shape.

The following attributes modify a fill.



| Attribute                                                          | Description                                            |
|--------------------------------------------------------------------|--------------------------------------------------------|
| [AlignShape](msdn-online-vml-alignshape-attribute.md)             | Determines whether an image will align with a shape.   |
| [AltHRef](althref-attribute--fill--vml.md)                        | Specifies an alternate reference for an image.         |
| [Angle](angle-attribute--fill--vml.md)                            | Defines the angle of a gradient fill.                  |
| [Aspect](msdn-online-vml-aspect-attribute.md)                     | Specifies how the fill image aspect will be preserved. |
| [Color](color-attribute--fill--vml.md)                            | Defines the color of a fill.                           |
| [Color2](color2-attribute--fill--vml.md)                          | Defines the second color for a fill.                   |
| [Colors](msdn-online-vml-colors-attribute.md)                     | Defines multiple colors for a gradient fill.           |
| [DetectMouseClick](detectmouseclick-attribute--fill--vml.md)      | Determines whether a mouse click is detected.          |
| [Focus](msdn-online-vml-focus-attribute.md)                       | Defines the center of a linear gradient fill.          |
| [FocusPosition](msdn-online-vml-focusposition-attribute.md)       | Defines the center of a radial gradient fill.          |
| [FocusSize](msdn-online-vml-focussize-attribute.md)               | Defines the focus size for a radial fill.              |
| [HRef](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/bb229574(v=vs.85)) | Defines a URL to the original image file.              |
| [ID](id-attribute--fill--vml.md)                                  | Defines a unique identifier for the fill.              |
| [Method](msdn-online-vml-method-attribute.md)                     | Defines the method used to generate a gradient fill.   |
| [On](on-attribute--fill--vml.md)                                  | Determines whether the fill wil be displayed.          |
| [Opacity](opacity-attribute--fill--vml.md)                        | Defines the transparency of a fill.                    |
| [Opacity2](msdn-online-vml-opacity2-attribute.md)                 | Defines the transparency of the second fill color.     |
| [Origin](origin-attribute--fill--vml.md)                          | Defines the center of an image.                        |
| [Position](position-attribute--fill--vml.md)                      | Defines the position of an image.                      |
| [Size](size-attribute--fill--vml.md)                              | Defines the size of an image.                          |
| [Src](src-attribute--fill--vml.md)                                | Defines the image to load for a fill.                  |
| [Title](title-attribute--fill--vml.md)                            | Defines the title of a fill.                           |
| [Type](type-attribute--fill--vml.md)                              | Defines the type of fill.                              |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

The following code shows a simple gradient fill for a shape.


```HTML
   <v:shape
   style="position:relative;top:1;left:1;width:400;height:400"
   path = "m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type=gradient color="blue" color2="yellow"/>
   </v:shape>
```



**Examples**

-   [Simple Gradient Fill](/previous-versions/bb229620(v=vs.85))
-   [Dynamic Fill Example](/previous-versions/bb229621(v=vs.85))

 

 