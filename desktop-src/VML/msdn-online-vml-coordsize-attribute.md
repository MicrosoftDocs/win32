---
title: VML CoordSize Attribute
description: VML CoordSize Attribute
ms.assetid: 4e7a7eca-7db2-4522-be8e-e817601625ed
ms.topic: article
ms.date: 05/31/2018
---

# VML CoordSize Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the horizontal and vertical units of the rectangle that bounds a shape. Read/write. [IVgVector2D](msdn-online-vml-ivgvector2d-data-type.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* coordsize=" *expression* ">

**Script Syntax**

*element* .coordsize="*expression*"

*expression*=*element*.coordsize

**Remarks**

If not specified, the coordinate size is the same as the bounding box of the shape.

Note that this attribute is a vector and that the units are relative to the length and width of the bounding rectangle.

Also note that mapping between **coordsize** and the bounding box can be made anisotropic. Make sure that the **coordsize width** and **coordsize height** is the same as the **style width** and **height** if you don't want to distort the shape.

In scripting, because this is a 2-D vector, you can access the x and y values separately, and can also determine the type of units expected.

*VML Standard Attribute*

**Example**

The shape is 100 points high and 100 points wide, but each horizontal and vertical unit in the coordinate space is 1/10 of a point.


```HTML
   <v:shape id="rect01"
   fillcolor="red" strokecolor="red"
   coordorigin="0 0" coordsize="1000 1000"
   style="position:relative;top:0;left:0;width:100pt;height:100pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[CoordSize Attribute Example](/previous-versions/bb229665(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 