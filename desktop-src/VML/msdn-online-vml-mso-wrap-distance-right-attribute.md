---
title: VML MSO-Wrap-Distance-Right Attribute
description: VML MSO-Wrap-Distance-Right Attribute
ms.assetid: 2f0ec7a3-036e-4f45-a330-f8ddccb75791
ms.topic: article
ms.date: 05/31/2018
---

# VML MSO-Wrap-Distance-Right Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the distance from the right side of the shape to the text that wraps around it. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="mso-wrap-distance-right: *expression* ">

**Remarks**

Note that this attribute is different from the CSS **Margin** attribute. **Margin** changes the origin of the shape to include the margin areas, but the wrap-distance in Microsoft Office does not change the origin of the shape.

*Microsoft Office Extensions Attribute*

**Example**

The shape has a right wrap-distance of 10 points.


```HTML
   <v:shape id="rect01"
   fillcolor="red" strokecolor="red"
   coordorigin="-500 -500" coordsize="1000 1000"
   style="position:relative;top:0;left:0;width:100pt;height:100pt;mso-wrap-distance-right:10pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



 

 