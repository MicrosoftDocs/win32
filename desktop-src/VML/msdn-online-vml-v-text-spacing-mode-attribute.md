---
title: VML V-Text-Spacing-Mode Attribute
description: VML V-Text-Spacing-Mode Attribute
ms.assetid: 2c20e9d7-cb6a-4da7-af7a-9a7b1baa8e1f
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Spacing-Mode Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the mode for letterspacing. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-text-spacing-mode: *expression* ">

**Script Syntax**

*element* .style.v-text-spacing-mode="*expression*"

*expression*=*element*.style.v-text-spacing-mode

**Remarks**

Values include

-   **tightening** (default)
-   **tracking**

This attribute determines whether space will be removed between each letter (tightening) or added between each letter (tracking). The amount of letterspacing change is defined by the [V-Text-Spacing](msdn-online-vml-v-text-spacing-attribute.md) attribute.

*VML Standard Attribute*

**Example**

The letterspacing between each letter is increased by 200 units.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-text-spacing:200;v-text-spacing-mode:tracking;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 