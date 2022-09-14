---
title: VML Colors Attribute
description: VML Colors Attribute
ms.assetid: 466ed1d7-8861-44db-bd96-a2fd119b12f4
ms.topic: article
ms.date: 05/31/2018
---

# VML Colors Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines multiple colors for a gradient fill. Read/write. **IVgGradientColorArray**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* colors=" *expression* ">

**Script Syntax**

*element* .colors="*expression*"

*expression*=*element*.colors

**Remarks**

Used to define an array consisting of paired values of percentages ([VgFraction](msdn-online-vml-vgfraction-data-type.md)) and color ([VgColor](msdn-online-vml-ivgcolor.md)). The array creates a blended fill using each point in the array, starting at 0% (defined by **Color**) and ending at 100% (defined by **Color2**). Intermediate colors along the way can be defined by assigning a color value to a percentage. The percent and color pair are not separated by a comma, but pairs are separated from each other by commas.

VML Standard Attribute

**Example**

The shape has a gradient fill consisting of four colors, starting with red, blending to yellow, then green, and finallyblue.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="gradient" color="red" color2="blue"
   colors="30% yellow,70% green"/>
   </v:shape>
```



 

 