---
title: Src Attribute (ImageData)(VML)
description: Src Attribute (ImageData)(VML)
ms.assetid: ef6b57d9-dca7-4f6e-8fd1-e846e4d09fb7
ms.topic: article
ms.date: 05/31/2018
---

# Src Attribute (ImageData)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a source for the image. Read/write. **String**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* src=" *expression* ">

**Script Syntax**

*element* .src="*expression*"

*expression*=*element*.src

**Remarks**

This attribute must always be used with the [ImageData](msdn-online-vml-imagedata-element.md) element and point to valid image data for a picture to be displayed. If this attribute appears without [HRef](https://www.bing.com/search?q=HRef) or [Title](title-attribute--imagedata--vml.md), then the image is linked.

*VML Standard Attribute*

**Example**

The source of the image is a file named "kids.jpg".


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata src="kids.jpg"/>
   </v:shape>
```



 

 