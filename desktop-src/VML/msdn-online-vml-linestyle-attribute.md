---
title: VML LineStyle Attribute
description: VML LineStyle Attribute
ms.assetid: eec5c1f3-5256-4104-b021-ebf799665752
ms.topic: article
ms.date: 05/31/2018
---

# VML LineStyle Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the line style of the stroke. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* linestyle=" *expression* ">

**Script Syntax**

*element* .linestyle="*expression*"

*expression*=*element*.linestyle

**Remarks**

Values include:

-   Single (default)
-   ThinThin
-   ThinThick
-   ThickThin
-   ThickBetweenThin

*VML Standard Attribute*

**Example**

A double line is drawn with two thin strokes.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke linestyle="thinthin" />
   </v:line>
```



 

 