---
title: VML Font Attribute
description: VML Font Attribute
ms.assetid: 5a48fc54-e2dd-4b68-863c-3a83f9386108
ms.topic: article
ms.date: 05/31/2018
---

# VML Font Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies a compound value of font attributes. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="font: *expression* ">

**Script Syntax**

*element* .style.font="*expression*"

*expression*=*element*.style.font

**Remarks**

Defines the attributes of a font, including family, style, weight, size, and variant. The order of definitions in the string is: **font-style**, **font-variant**, **font-weight**, **font-size**, **line-height**, and **font-family**. The values are the same as the standard HTML style attributes.

*VML Standard Attribute*

**Example**

The font of the textpath text is italic, small-caps, bold, 36 point Arial.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="font:italic small-caps bold 36pt Arial"/>
   </v:line>
```



 

 