---
title: VML Imagedata Element
description: VML Imagedata Element
ms.assetid: 91004646-b031-4973-a32d-7afdd10dab48
ms.topic: article
ms.date: 05/31/2018
---

# VML Imagedata Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines an image for a shape.

The following attributes modify an image.



| Attribute                                                          | Description                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------|
| [AltHRef](althref-attribute--imagedata--vml.md)                   | Specifies an alternate reference for an image.                        |
| [Bilevel](msdn-online-vml-bilevel-attribute.md)                   | Determines whether an image will display in black and white.          |
| [BlackLevel](msdn-online-vml-blacklevel-attribute.md)             | Determines the intensity of black in an image.                        |
| [Chromakey](msdn-online-vml-chromakey-attribute.md)               | Defines the color in the palatte that will be treated as transparent. |
| [CropBottom](msdn-online-vml-cropbottom-attribute.md)             | Defines the percentage of picture removal from the bottom side.       |
| [CropLeft](msdn-online-vml-cropleft-attribute.md)                 | Defines the percentage of picture removal from the left side.         |
| [CropRight](msdn-online-vml-cropright-attribute.md)               | Defines the percentage of picture removal from the right side.        |
| [CropTop](msdn-online-vml-croptop-attribute.md)                   | Defines the percentage of picture removal from the top side.          |
| [DetectMouseClick](detectmouseclick-attribute--imagedata--vml.md) | Determines whether a mouse click will be detected.                    |
| [EmbossColor](msdn-online-vml-embosscolor-attribute.md)           | Defines the color for embossed color effects.                         |
| [Gain](msdn-online-vml-gain-attribute.md)                         | Defines the intensity of all colors in an image.                      |
| [Gamma](msdn-online-vml-gamma-attribute.md)                       | Defines the amount of contrast for an image.                          |
| [GrayScale](msdn-online-vml-grayscale-attribute.md)               | Determines whether a picture will display in grayscale mode.          |
| [HRef](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/bb229574(v=vs.85)) | Defines a URL for an image.                                           |
| [ID](id-attribute--image--vml.md)                                 | Defines a unique identifier for an image.                             |
| [Movie](msdn-online-vml-movie-attribute.md)                       | Defines a pointer to a movie image.                                   |
| [OLEID](msdn-online-vml-oleid-attribute.md)                       | Stores the OLE ID of an image.                                        |
| [Src](src-attribute--imagedata--vml.md)                           | Defines a source for the image.                                       |
| [Title](title-attribute--imagedata--vml.md)                       | Defines the title of an image.                                        |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

In addition, the [**Src**](src-attribute--imagedata--vml.md) attribute must point to an image.

The following is the minimum code needed to produce an image.


```HTML
   <v:rect
   style="position:relative;top:1;left:1;width:50;height:50">
   <v:imagedata src="../art/kids.jpg"/>
   </v:rect>
```



> [!Note]  
> In pre-release versions of VML, this element was called **Image** .

 

**Examples**

-   [Simple ImageData Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/image/t_image.md)
-   [Dynamic ImageData Example](https://samples.msdn.microsoft.com/workshop/samples/vml/shape/image/x_image.md)

 

 