---
title: VML Font-Family Attribute
description: VML Font-Family Attribute
ms.assetid: 10586ae0-1480-4ffe-a690-ce8464e9bf41
ms.topic: article
ms.date: 05/31/2018
---

# VML Font-Family Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the family of the textpath font. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="font-family: *expression* ">

**Script Syntax**

*element* .style.fontfamily="*expression*"

*expression*=*element*.style.fontfamily

**Remarks**

Defines the font name. Specific names such as Arial can be used or generic types such as serif, sans-serif, cursive, fantasy, or monospace. The values are the same as the standard HTML style attributes.

*VML Standard Attribute*

**Example**

The font family of the text is Arial.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 