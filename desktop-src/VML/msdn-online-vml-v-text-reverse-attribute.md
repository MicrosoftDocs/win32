---
title: VML V-Text-Reverse Attribute
description: VML V-Text-Reverse Attribute
ms.assetid: ad302b0f-5d93-457d-a8df-c9fce184475e
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Reverse Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the layout order of rows is reversed. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-text-reverse: *expression* ">

**Script Syntax**

*element* .style.v-text-reverse="*expression*"

*expression*=*element*.style.v-text-reverse

**Remarks**

If **True**, the layout order of rows is reversed. This attribute is used for vertical text layout. The default value is **False**.

*VML Standard Attribute*

**Example**

The layout order is reversed.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-text-reverse:True;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 