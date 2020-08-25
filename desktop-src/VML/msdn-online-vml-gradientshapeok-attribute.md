---
title: VML GradientShapeOK Attribute
description: VML GradientShapeOK Attribute
ms.assetid: c26ac4cb-f7f0-4666-b32f-d9fcaf9044a2
ms.topic: article
ms.date: 05/31/2018
---

# VML GradientShapeOK Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a gradient path will be made up of repeated concentric paths. Read/write. **VgTriState**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* gradientshapeok=" *expression* ">

**Script Syntax**

*element* .gradientshapeok="*expression*"

*expression*=*element*.gradientshapeok

**Remarks**

If **True**, the path will be filled with a concentric gradient fill using the path as the repeated shape of the gradient.The default is **False**.

*VML Standard Attribute*

**Example**

The path will be filled with a concentric gradient fill made up of repeated rectangles.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:path gradientshapeok="True"/>
   </v:shape>
```



 

 