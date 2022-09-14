---
title: Color2 Attribute (Stroke)(VML)
description: Color2 Attribute (Stroke)(VML)
ms.assetid: 60b8035e-9477-4f8b-817b-dd6c41bdfa79
ms.topic: article
ms.date: 05/31/2018
---

# Color2 Attribute (Stroke)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a second color for strokes. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* color2=" *expression* ">

Script Syntax

*element* .color2="*expression*"

*expression*=*element*.color2

**Remarks**

A second color is used when a stroke's fill type is a pattern.

*VML Standard Attribute*

**Example**

The shape's stroke is a pattern fill where the fill is defined by the source image but the transparent background is defined by the second color.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke filltype="pattern" width="5pt" src="cylinder.gif" color2="green"/>
   </v:shape>
```



 

 