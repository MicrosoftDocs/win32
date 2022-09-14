---
title: VML AlignShape Attribute
description: VML AlignShape Attribute
ms.assetid: 427e5969-4545-47b2-80f8-0e8783c52d65
ms.topic: article
ms.date: 05/31/2018
---

# VML AlignShape Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether an image will align with a shape. Read/write. **VgTriState**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* alignshape=" *expression* ">

**Script Syntax**

*element* .alignshape="*expression*"

*expression*=*element*.alignshape

**Remarks**

If **True**, the image used to create the fill is aligned with the shape. If **False**, the image used to create the fill is aligned with the window. Default is **True**.

*VML Standard Attribute*

**Example**

The tiled fill image created from myimage.gif is aligned with the window, not the shape; even though the shape is rotated, the image is not.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50;rotation:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill alignshape="False" type="tile" src="myimage.gif"/>
   </v:shape>
```



 

 