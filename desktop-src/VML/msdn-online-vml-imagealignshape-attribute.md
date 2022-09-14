---
title: VML ImageAlignShape Attribute
description: VML ImageAlignShape Attribute
ms.assetid: 45d72560-ab64-4e85-b495-88f1557a62f1
ms.topic: article
ms.date: 05/31/2018
---

# VML ImageAlignShape Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines the alignment of the stroke image. Read/write. **VgTriState**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v:

element *imagealignshape="* expression *">*

**Script Syntax**

element *.imagealignshape="*expression*"*

expression*=*element*.imagealignshape*

**Remarks**

If **True**, align the image with the shape, else align the image with the window. The default is **True**.

*VML Standard Attribute*

**Example**

The image is aligned with the window.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red" strokeweight="20pt"
   style="top:20;left:20;width:300;height:300"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke imagealignshape="false" width="5pt" filltype="tile" src="cylinder.gif"/>
   </v:shape>
```



 

 