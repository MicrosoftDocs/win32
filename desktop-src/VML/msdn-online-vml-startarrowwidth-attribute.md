---
title: VML StartArrowWidth Attribute
description: VML StartArrowWidth Attribute
ms.assetid: 47b55330-7165-4368-ad01-5b7b38a6e5b2
ms.topic: article
ms.date: 05/31/2018
---

# VML StartArrowWidth Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the arrowhead width for the start of a line. Read/write. **VgArrowheadWidth**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* startarrowwidth=" *expression* ">

**Script Syntax**

*element* .startarrowwidth="*expression*"

*expression*=*element*.startarrowwidth

**Remarks**

Values include:

-   Narrow
-   Medium (default)
-   Wide

VML Standard Attribute

**Example**

A line is drawn with a wide classic arrowhead on the start of the stroke.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke startarrow="classic" startarrowwidth="wide"/>
   </v:line>
```



 

 