---
title: Src Attribute (Stroke)(VML)
description: Src Attribute (Stroke)(VML)
ms.assetid: dac6b5b7-2038-4534-97e9-a1340102777e
ms.topic: article
ms.date: 05/31/2018
---

# Src Attribute (Stroke)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the source image to load for a stroke fill. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* src=" *expression* ">

**Script Syntax**

*element* .src="*expression*"

*expression*=*element*.src

**Remarks**

URL to an image to load for image and pattern fills. This attribute must always be present and point to valid image data for a picture to appear. If this attribute appears alone, that is, no **HRef** or **Title**, then the image is linked.

*VML Standard Attribute*

**Example**

The stroke is created with the image specified by the cylinder.gif file.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke src="cylinder.gif" filltype="tile" width="10pt"/>
   </v:shape>
```





 

 