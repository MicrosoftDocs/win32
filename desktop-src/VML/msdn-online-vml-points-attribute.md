---
title: VML Points Attribute
description: VML Points Attribute
ms.assetid: 343d843e-9a09-4c89-af54-fb079129429b
ms.topic: article
ms.date: 05/31/2018
---

# VML Points Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a set of points that make up a polyline. Read/write. [IVgPoints](msdn-online-vml-ivgpoints-data-type.md) .

**Applies To**

[Polyline](msdn-online-vml-polyline-element.md)

**Tag Syntax**

<v: *element* points=" *expression* ">

**Script Syntax**

*element* .points="*expression***"**

*expression*=*element*.points

**Remarks**

Defines a set of straight line segments that are composed of a series of points. If the parent is not a VML element, the default [unit](msdn-online-vml-units.md) is a pixel (but in, cm, mm, pt, pc may also be specified). The default value is "0,0 10,10". Note that commas are not required, but they make for easier readability.

*VML Standard Attribute*

**Example**

The polyline starts at the point 10,10 and ends at 100,100, with the valuesin points.


```HTML
   <v:polyline id="mypolyline"
   points="10pt,10pt 100pt,100pt">
   </v:polyline>
```



 

 