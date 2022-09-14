---
title: VML StrokeColor Attribute
description: VML StrokeColor Attribute
ms.assetid: e7224d77-f788-43c7-aa8e-d5fc318f9d4f
ms.topic: article
ms.date: 05/31/2018
---

# VML StrokeColor Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the brush color that strokes the path of a shape. Read/write. [IVgColor](msdn-online-vml-ivgcolor.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* strokecolor=" *expression* ">

**Script Syntax**

*element* .strokecolor="*expression*"

*expression*=*element*.strokecolor

**Remarks**

The value is duplicated from the **Color** attribute of the [Stroke](msdn-online-vml-stroke-element.md) element.

*VML Standard Attribute*

**Example**

The color of the stroke of the rectangle is red.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="white"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1;width:20;height:20"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[StrokeColor Attribute Example](/previous-versions/bb264093(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 