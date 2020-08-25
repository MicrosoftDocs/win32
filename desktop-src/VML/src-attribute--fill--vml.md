---
title: Src Attribute (Fill)(VML)
description: Src Attribute (Fill)(VML)
ms.assetid: 88ad9413-1863-41e2-855b-2bf155ce23cc
ms.topic: article
ms.date: 05/31/2018
---

# Src Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the image to load for a fill. Read/write. **String**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* src=" *expression* ">

**Script Syntax**

*element* .src="*expression***"**

*expression*=*element*.src

**Remarks**

URL to an image to load for image and pattern fills. This attribute must always be present and point to valid image data for a picture to appear. If this attribute appears alone (that is, no **HRef** or **Title** attribute), then the image is linked.

*VML Standard Attribute*

**Example**

A tiled image using the file myimage.gif as a source is displayed.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="tile" src="myimage.gif"/>
   </v:shape>
```



 

 