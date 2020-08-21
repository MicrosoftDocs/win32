---
title: VML Method Attribute
description: VML Method Attribute
ms.assetid: 42ab9d78-f004-4571-a566-03edd8341d19
ms.topic: article
ms.date: 05/31/2018
---

# VML Method Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the method used to generate a gradient fill. Read/write. **VgSigmaType**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* method=" *expression* ">

**Script Syntax**

*element* .method="*expression*"

*expression*=*element*.method

**Remarks**

Values include:



| Value  | Description          |
|--------|----------------------|
| None   | No sigma fill.       |
| Linear | Linear sigma fill.   |
| Sigma  | Sigma fill. Default. |
| Any    | Any sigma fill.      |



 

*VML Standard Attribute*

**Example**

The shape will have a red linear gradient fill.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill color="red" type="gradient" method="linear"/>
   </v:shape>
```



 

 