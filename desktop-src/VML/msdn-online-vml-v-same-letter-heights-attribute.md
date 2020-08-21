---
title: VML V-Same-Letter-Heights Attribute
description: VML V-Same-Letter-Heights Attribute
ms.assetid: f06c0a50-1de1-47d8-8b94-01fe0599ed59
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Same-Letter-Heights Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether all letters will be the same height regardless of initial case. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-same-letter-heights: *expression* ">

**Script Syntax**

*element* .style.v-same-letter-heights="*expression*"

*expression*=*element*.style.v-same-letter-heights

**Remarks**

If **True**, the lowercase letters are stretched to the height of the uppercase letters. The default value is **False**.

*VML Standard Attribute*

**Example**

All letters will be the same height, regardless of case.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-same-letter-heights:True;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 