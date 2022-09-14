---
title: Color Attribute (Stroke)(VML)
description: Color Attribute (Stroke)(VML)
ms.assetid: 8fa19789-0bd6-4e9f-8af4-566155eafc6a
ms.topic: article
ms.date: 05/31/2018
---

# Color Attribute (Stroke)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the color of a stroke. Read/write. **VgColor**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* color=" *expression* ">

**Script Syntax**

*element* .color="*expression*"

*expression*=*element*.color

**Remarks**

Overrides the **StrokeColor** attribute of a shape. The default value is **black**.

*VML Standard Attribute*

**Example**

The shape has a stroke color of **green**, not **red**.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke color="green"/>
   </v:shape>
```



 

 