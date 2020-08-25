---
title: VML Weight Attribute
description: VML Weight Attribute
ms.assetid: 40164818-6b04-4afe-91cc-9fb8b12cb718
ms.topic: article
ms.date: 05/31/2018
---

# VML Weight Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the thickness of a stroke. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* weight=" *expression* ">

**Script Syntax**

*element* .weight="*expression*"

*expression*=*element*.weight

**Remarks**

This attribute is the same as the **StrokeWeight** attribute of **Shape** and overrides it. The default value is 1 point.

*VML Standard Attribute*

**Example**

The stroke has a thickness of 5 points, not 2 points.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red" strokeweight="2pt"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke weight="5pt"/>
   </v:shape>
```



 

 