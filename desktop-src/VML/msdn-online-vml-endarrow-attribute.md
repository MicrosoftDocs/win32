---
title: VML EndArrow Attribute
description: VML EndArrow Attribute
ms.assetid: 056cd011-bb3b-4f9a-83d0-9702e0e82e4d
ms.topic: article
ms.date: 05/31/2018
---

# VML EndArrow Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines an arrowhead for the end of a line. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* endarrow=" *expression* ">

**Script Syntax**

*element* .endarrow="*expression*"

*expression*=*element*.endarrow

**Remarks**

Values include:

-   None (default)
-   Block
-   Classic
-   Diamond
-   Oval
-   Open

*VML Standard Attribute*

**Example**

A line is drawn with a classic arrowhead on the end of the stroke.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke endarrow="classic"/>
   </v:line>
```



 

 