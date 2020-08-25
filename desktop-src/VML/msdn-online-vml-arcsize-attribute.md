---
title: VML ArcSize Attribute
description: VML ArcSize Attribute
ms.assetid: e67d1bae-2f54-4c43-8445-1f5109e4afde
ms.topic: article
ms.date: 05/31/2018
---

# VML ArcSize Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the amount of roundness for a rounded rectangle. Read/write. [VgFraction](msdn-online-vml-vgfraction-data-type.md) .

**Applies To**

[RoundRect](msdn-online-vml-roundrect-element.md)

**Tag Syntax**

<v: *element* arcsize=" *expression* ">

**Script Syntax**

*element* .arcSize="*expression*"

*expression*=*element*.arcSize

**Remarks**

Defines the rounded corners of a rounded rectangle as a percentage of half the smaller dimension of the length and width of a rectangle. 0% would have square corners, and 100% would form circular corners. A square with an **ArcSize** value of 1.0 would be a circle. The default value is 0.2 (20%).

*VML Standard Attribute*

**Example**

The rounded rectangle is drawn with tight-but-rounded corners.


```HTML
   <v:roundrect id=myrr
   style="height:100;left:100;top:100;width:200"
   fillcolor="red"
   arcsize="5%">
   </v:roundrect>
```



 

 