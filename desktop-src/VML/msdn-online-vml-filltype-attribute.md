---
title: VML FillType Attribute
description: VML FillType Attribute
ms.assetid: c6870100-8fb9-4589-9b83-cd46cc17eeb3
ms.topic: article
ms.date: 05/31/2018
---

# VML FillType Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the type of fill used for the background of a stroke. Read/write. **VgFillType**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* filltype=" *expression* ">

**Script Syntax**

*element* .filltype="*expression*"

*expression*=*element*.filltype

**Remarks**

Values include:



| DashStyle | Description                                    |
|-----------|------------------------------------------------|
| Solid     | The fill pattern is solid. Default value.      |
| Tile      | The fill image is tiled.                       |
| Pattern   | The fill image is stretched to form a pattern. |
| Frame     | The fill image becomes a border for the shape. |



 

*VML Standard Attribute*

**Example**

The stroke of the shape has a tiled texture created from the cylinder.gif image.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke width="5pt" filltype="tile" src="cylinder.gif"/>
   </v:shape>
```



 

 