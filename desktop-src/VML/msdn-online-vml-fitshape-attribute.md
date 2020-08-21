---
title: VML FitShape Attribute
description: VML FitShape Attribute
ms.assetid: a6e5a198-1478-4256-a4f2-b9ae6db6d7fb
ms.topic: article
ms.date: 05/31/2018
---

# VML FitShape Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines whether the text fits bounding box of a shape. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* fitshape=" *expression* ">

**Script Syntax**

*element* .fitshape="*expression*"

*expression*=*element*.fitshape

**Remarks**

If **True**, stretches the text out to the edges of the box that defines the entire shape. The default is **False**.

*VML Standard Attribute*

**Example**

The text will stretch to fit the shape.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text" fitshape="True"
   style="font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 