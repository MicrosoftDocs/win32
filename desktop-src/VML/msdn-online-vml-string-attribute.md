---
title: VML String Attribute
description: VML String Attribute
ms.assetid: 99609814-29c9-4349-9509-8c91f2aaeff5
ms.topic: article
ms.date: 05/31/2018
---

# VML String Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the text of the text path. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* string=" *expression* ">

**Script Syntax**

*element* .string="*expression*"

*expression*=*element*.string

**Remarks**

You must assign a text string to display text on a text path.

VML Standard Attribute

**Example**

The string that will be displayed is "VML Text".


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 