---
title: VML Flip Attribute
description: VML Flip Attribute
ms.assetid: 0d3d4c54-e769-4f6b-a9f5-6e48125a7215
ms.topic: article
ms.date: 05/31/2018
---

# VML Flip Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Switches the orientation of a shape. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="flip: *expression* ">

**Script Syntax**

*element* .style.flip="*expression*"

*expression*=*element*.style.flip

**Remarks**

Values include:



| Value | Description                                           |
|-------|-------------------------------------------------------|
| x     | Flip along the y-axis, reversing the *x*-coordinates. |
| y     | Flip along the *x*-axis, reversing the y-coordinates. |
| xy    | Flip along both the y- and *x*-axis.                  |
| yx    | Flip along both the *x*- and *y*-axis.                |



 

*VML Standard Attribute*

**See Also**

[VgFlipOrientation](msdn-online-vector-markup-language-object-model-reference.md)

**Example**

The shape is flipped along the *y* -axis by reversing the *x* -coordinates.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;flip:x">
   </v:rect>
```



[Flip Attribute Example](/previous-versions/bb229670(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 