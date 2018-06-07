---
title: VML CoordOrigin Attribute
description: VML CoordOrigin Attribute
ms.assetid: 0630e670-6ebe-424e-a5e0-545597454283
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML CoordOrigin Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Specifies the coordinate unit origin of the rectangle that bounds a shape. Read/write. [IVgVector2D](msdn-online-vml-ivgvector2d-data-type.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

&lt;v: *element* coordorigin=" *expression* "&gt;

**Script Syntax**

*element* .coordorigin="*expression*"

*expression*=*element*.coordorigin

**Remarks**

If not specified, the origin coordinates are (0,0) at the top left corner of the shape bounding box.

The x value of **CoordSize** is added to the x value of **CoordOrigin** to determine the range of the horizontal values. For example,if the x value of **CoordOrigin** is -100 and the x value of **CoordSize** is 200, the horizontal units will range from -100 to +100. If the x value of **CoordOrigin** is 100 and the x value of **CoordSize** is 200, the horizontal units will range from 100 to 300, all within the bounding box. The same is true for the y values.

Note that this attribute is a vector and that the units are the same type of unit as [CoordSize](msdn-online-vml-coordsize-attribute.md) .

In scripting, because this is a 2-D vector, you can access the x and y values separately, and can also determine the type of units expected.

*VML Standard Attribute*

**Example**

The center of the bounding box will be the origin (0,0) of the path for the shape. Because **CoordOrigin** is "-500 -500" and **CoordSize** is "1000 1000", the horizontal and vertical units will range from -500 to +500. The left and top corner of the path will be at the center of the bounding box defined by the left and top points as defined by **Style**.


```HTML
   <v:shape id="rect01"
   fillcolor="red" strokecolor="red"
   coordorigin="-500 -500" coordsize="1000 1000"
   style="position:relative;top:0;left:0;width:100pt;height:100pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[CoordOrigin Attribute Example](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/examples/x_coorig.md). (Requires Microsoft Internet Explorer 5 or greater.)

 

 




