---
title: Size Attribute (Fill)(VML)
description: Size Attribute (Fill)(VML)
ms.assetid: a84d2d81-0f6f-4011-867d-516225a314aa
ms.topic: article
ms.date: 05/31/2018
---

# Size Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the size of the image for the fill. Read/write. [VgVector2D](msdn-online-vml-ivgvector2d-data-type.md) .

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* size=" *expression* ">

**Script Syntax**

*element* .size="*expression***"**

*expression*=*element*.size

**Remarks**

The default is the size of the original image. Sizes that are larger than the shapewill display a magnified but clipped version of the image.

*VML Standard Attribute*

**Example**

Even though the original size of the image is 50-by-50 points, the image will be displayed as a 10-by-10 image in the center of the fill.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill src="myimage.gif" type="frame" size="10pt,10pt"/>
   </v:shape>
```



 

 