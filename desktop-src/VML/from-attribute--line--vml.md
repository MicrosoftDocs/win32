---
title: From Attribute (Line)(VML)
description: From Attribute (Line)(VML)
ms.assetid: 37cc9b2e-c18d-48ea-bac5-a2d2ea10d3d2
ms.topic: article
ms.date: 05/31/2018
---

# From Attribute (Line)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the starting point of a line. Read/write. **VgVector2D**.

**Applies To**

[Line](msdn-online-vml-line-element.md)

**Tag Syntax**

<v: *element* from=" *expression* ">

**Script Syntax**

*element* .from="*expression*"

*expression*=*element*.from

**Remarks**

Defines the starting point of the line in the coordinate space of the parent element.If the parent is not a VML element, the default [unit](msdn-online-vml-units.md) is a pixel (but in, cm, mm, pt, pc may also be specified). Default is 0,0.

*VML Standard Attribute*

**Example**

The line starts at a location 10 points down and 10 points to the right of the top left corner of the parent space.


```HTML
   <v:line id="myline"
   from="10pt,10pt" to="100pt,100pt">
   </v:line>
```



 

 