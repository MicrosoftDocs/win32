---
title: VML StartArrow Attribute
description: VML StartArrow Attribute
ms.assetid: 484dfcdb-f68d-40f9-9a83-18abb054d1c8
ms.topic: article
ms.date: 05/31/2018
---

# VML StartArrow Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the arrowhead for the start of a line. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* startarrow=" *expression* ">

**Script Syntax**

*element* .startarrow="*expression*"

*expression*=*element*.startarrow

**Remarks**

Values include:

-   None (default)
-   Block
-   Classic
-   Diamond
-   Oval
-   Open

VML Standard Attribute

**Example**

A line is drawn with a classic arrowhead on the start of the stroke.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke StartArrow="classic"/>
   </v:line>
```



 

 