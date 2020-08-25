---
title: VML FocusPosition Attribute
description: VML FocusPosition Attribute
ms.assetid: 1aebf79d-c887-4a61-b50c-01a4ebfd68a3
ms.topic: article
ms.date: 05/31/2018
---

# VML FocusPosition Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the center of a radial gradient. Read/write. **VgVector2D**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* focusposition=" *expression* ">

**Script Syntax**

*element* .focusposition="*expression*"

*expression*=*element*.focusposition

**Remarks**

Specifies the center positionfor radial gradients. The vector is a fraction of the width and height of the shape. The first is a percentage of the fill to the left edge; the second is a percentage of the fill to the top. The default value is 0,0. To position a radial fill at the center of a shape, use the value of 50%,50%.

*VML Standard Attribute*

**Example**

The radial fill will be centered so that blue will start in the center and radiate outward, gradually changing to red by the time it reaches the outside edges and corners.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="GradientRadial" color="red" color2="blue"
   focusposition="50%,50%"/>
   </v:shape>
```



 

 