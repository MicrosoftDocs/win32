---
title: VML MiterLimit Attribute
description: VML MiterLimit Attribute
ms.assetid: 74744b8a-df73-4a2e-8df7-07fd0e423a47
ms.topic: article
ms.date: 05/31/2018
---

# VML MiterLimit Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the smoothness of the miter joint. Read/write. **VgNumber**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* miterlimit=" *expression* ">

**Script Syntax**

*element* .miterlimit="*expression*"

*expression*=*element*.miterlimit

**Remarks**

The maximum distance between the inner point and outer point of a joint. This number is a multiple of the thickness of the line.

The default value is 8.

*VML Standard Attribute*

**Example**

The joints on the polyline are mitered with a limit of 10, that is, 5 times 2 points.


```HTML
   <v:polyline
   strokecolor="red" strokeweight="2pt"
   points="18pt,54pt,90pt,-9pt,180pt,63pt,261pt,27pt">
   <v:stroke miterlimit="5" joinstyle="miter"/>
   </v:polyline>
```



 

 