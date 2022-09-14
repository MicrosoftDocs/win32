---
title: VML V-Text-Align Attribute
description: VML V-Text-Align Attribute
ms.assetid: ca2cbbf6-ddbb-4f2b-942c-3fe0033bd649
ms.topic: article
ms.date: 05/31/2018
---

# VML V-Text-Align Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the alignment of text. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="v-text-align: *expression* ">

**Script Syntax**

*element* .style.v-text-align="*expression*"

*expression*=*element*.style.v-text-align

**Remarks**

Values include:

-   **left** (default)
-   **right**
-   **center**
-   **justify**
-   **letter-justify**
-   **stretch-justify**

*VML Standard Attribute*

**Example**

The text will be stretched out to fit the path, but the extra space will be put between each letter.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="v-text-align:letter-justify;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 