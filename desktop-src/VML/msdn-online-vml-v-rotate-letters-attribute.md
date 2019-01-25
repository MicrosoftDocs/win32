---
title: VML V-Rotate-Letters Attribute
description: VML V-Rotate-Letters Attribute
ms.assetid: f9bd5c04-7479-4dc0-83d7-4a0bd5e2d41d
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Rotate-Letters Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](https://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether the letters of the text are rotated. Read/write. **VgTriState**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-rotate-letters: *expression* ">

**Script Syntax**

*element* .style.v-rotate-letters="*expression*"

*expression*=*element*.style.v-rotate-letters

**Remarks**

If **True**, the letters of the text are rotated 90 degrees. The default value is **False**.

*VML Standard Attribute*

**Example**

The letters are rotated 90 degrees.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-rotate-letters:True;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 




