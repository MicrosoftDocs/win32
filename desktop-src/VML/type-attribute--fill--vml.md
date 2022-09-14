---
title: Type Attribute (Fill)(VML)
description: Type Attribute (Fill)(VML)
ms.assetid: 5dcc53cd-a156-48cd-ae32-951660d91556
ms.topic: article
ms.date: 05/31/2018
---

# Type Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines the type of fill. Read/write. **VgFillType**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* type=" *expression* ">

**Script Syntax**

*element* .type="*expression*"

*expression*=*element*.type

**Remarks**

Values include:



| Type           | Description                                                             |
|----------------|-------------------------------------------------------------------------|
| solid          | The fill pattern is solid. Default.                                     |
| gradient       | The fill colors blend together in a linear gradient from bottom to top. |
| gradientradial | The fill colors blend together in a radial gradient.                    |
| tile           | The fill image is tiled.                                                |
| pattern        | The image is used to create a pattern using the fill colors.            |
| frame          | The image is stretched to fill the shape.                               |



 

**VML Standard Attribute**

**Example**

A red foreground and blue background fill is created using the pattern of the image myimage.gif.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill color="red" color2="blue" type="pattern" src="myimage.gif"/>
   </v:shape>
```



 

 