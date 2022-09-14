---
title: VML V-Text-Kern Attribute
description: VML V-Text-Kern Attribute
ms.assetid: cece49c3-8e62-4327-8949-684a1d073293
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Kern Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether kerning is turned on. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-text-kern: *expression* ">

**Script Syntax**

*element* .style.v-text-kern="*expression*"

*expression*=*element*.style.v-text-kern

**Remarks**

If **True**, the kerning is turned on. The default is **False**. Kerning is the removal of space between certain letter pairs to compensate for uneven letterforms. For example, if kerning is turned on, extra space between a capital "T" and a lowercase "i" would be removed.

*VML Standard Attribute*

**Example**

Kerning is turned on.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-text-kern:True;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 