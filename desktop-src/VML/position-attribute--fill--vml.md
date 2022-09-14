---
title: Position Attribute (Fill)(VML)
description: Position Attribute (Fill)(VML)
ms.assetid: 0d532d4c-0c96-4f41-b54f-55b6aade0c03
ms.topic: article
ms.date: 05/31/2018
---

# Position Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the position of fill image. Read/write. [VgVector2D](msdn-online-vml-ivgvector2d-data-type.md) .

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* position=" *expression* ">

**Script Syntax**

*element* .position="*expression*"

*expression*=*element*.position

**Remarks**

Specifies a point in the shape to position the origin of the image. Default is the center of the container rectangle. The vector is a fraction of the width and height of the image.

*VML Standard Attribute*

**Example**

The image of the fill is shifted right to a point 50% of the width of the shape.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="pattern" position="0.5,0" src="myimage.gif"/>
   </v:shape>
```



 

 