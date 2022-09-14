---
title: Angle Attribute (Fill)(VML)
description: Angle Attribute (Fill)(VML)
ms.assetid: 97203e73-4dae-40c5-bb3d-127110525cff
ms.topic: article
ms.date: 05/31/2018
---

# Angle Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the angle of a gradient fill. Read/write. [VgAngle](msdn-online-vml-vgangleindegrees-data-type.md) .

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* angle=" *expression* ">

**Script Syntax**

*element* .angle="*expression*"

*expression*=*element*.angle

**Remarks**

The vector of a gradient is perpendicular to the vector of the blend direction from one color to another. The default value is 0 (zero) degrees, which is a horizontal vector from left to right. Positive angles rotate the gradient in a counter-clockwise direction.

*VML Standard Attribute*

**Example**

The fill of the shape is composed of a gradient of two colors, running from blue to red at an angle of 45 degrees. Red will be in the top left corner and blue will be in the bottom right corner.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="gradient" color="blue" color2="red" angle="45"/>
   </v:shape>
```



 

 