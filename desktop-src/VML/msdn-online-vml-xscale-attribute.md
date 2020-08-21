---
title: VML XScale Attribute
description: VML XScale Attribute
ms.assetid: b876201d-87d1-4795-8f7f-33712a8bf493
ms.topic: article
ms.date: 05/31/2018
---

# VML XScale Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a straight textpath will be used instead of the shape path. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="xscale: *expression* ">

**Script Syntax**

*element* .style.xscale="*expression*"

*expression*=*element*.style.xscale

**Remarks**

If **True**, the text runs along apath from left to right along the x value of the lower boundary of the shape. The default value is **False**.

*VML Standard Attribute*

**Example**

The text will appear as if it were drawn on a horizontal line, even though the shape path is a diagonal.


```HTML
   <v:line from="100 100" to="400 400">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="xscale:true;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 