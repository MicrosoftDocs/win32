---
title: VML Font-Weight Attribute
description: VML Font-Weight Attribute
ms.assetid: d7b2b0c5-b5cf-4e7d-bbca-c554d12bf97e
ms.topic: article
ms.date: 05/31/2018
---

# VML Font-Weight Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the thickness of the letters of the font. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

<v: *element* style="font-weight: *expression* ">

**Script Syntax**

*element* .style.fontweight="*expression*"

*expression*=*element*.style.fontweight

**Remarks**

The values are the same as the standard HTML style attributes. Values include:



| Value   | Description                                                                 |
|---------|-----------------------------------------------------------------------------|
| normal  | Normal. Default.                                                            |
| bold    | Bold.                                                                       |
| bolder  | Heavier than normal.                                                        |
| lighter | Lighter than normal.                                                        |
| 100     | At least as light as the 200 weight.                                        |
| 200     | At least as bold as the 100 weight and at least as light as the 300 weight. |
| 300     | At least as bold as the 200 weight and at least as light as the 400 weight. |
| 400     | Normal.                                                                     |
| 500     | At least as bold as the 400 weight and at least as light as the 600 weight. |
| 600     | At least as bold as the 500 weight and at least as light as the 700 weight. |
| 700     | Bold.                                                                       |
| 800     | At least as bold as the 700 weight and at least as light as the 900 weight. |
| 900     | At least as bold as the 800 weight.                                         |



 

*VML Standard Attribute*

**Example**

The font weight is bold.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="font:normal normal bold 36pt Arial"/>
   </v:line>
```



 

 