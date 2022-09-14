---
title: VML Limo Attribute
description: VML Limo Attribute
ms.assetid: 61919d48-0cc8-4693-a8bb-a8a4498ef840
ms.topic: article
ms.date: 05/31/2018
---

# VML Limo Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a stretch point on the path. Read/write. **Vector2D**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* limo=" *expression* ">

**Script Syntax**

*element* .limo="*expression*"

*expression*=*element*.limo

**Remarks**

The default value is "0 0". Limo stretches are points on a shape's edge that define where and how a shape may be stretched by a user in a graphical editor.

*VML Standard Attribute*

**Example**

A limo stretch point is defined halfway along the horizontal line.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" from="20pt,20pt" to="100pt,20pt">
   <v:path limo="60pt,20pt"/>
   </v:line>
```



 

 