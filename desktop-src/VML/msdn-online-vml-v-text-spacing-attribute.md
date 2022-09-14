---
title: VML V-Text-Spacing Attribute
description: VML V-Text-Spacing Attribute
ms.assetid: c0d83854-4009-4d1d-aa8a-37f660dd0ef7
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Spacing Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the amount of spacing for text. Read/write. **VgNumber**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-text-spacing: *expression* ">

**Script Syntax**

*element* .style.v-text-spacing="*expression*"

*expression*=*element*.style.v-text-spacing

**Remarks**

The default value is 100. See the [V-Text-Spacing-Mode](msdn-online-vml-v-text-spacing-mode-attribute.md) attribute for more information about text spacing.

*VML Standard Attribute*

**Example**

The letterspacing between each letter is tightened by 200 units.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-text-spacing:200;v-text-spacing-mode:tightening;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 