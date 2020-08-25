---
title: Color2 Attribute (Fill)(VML)
description: Color2 Attribute (Fill)(VML)
ms.assetid: 971c8783-8c7b-43c7-8b94-01159336eef6
ms.topic: article
ms.date: 05/31/2018
---

# Color2 Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a second color for fills. Read/write. [VgColor](msdn-online-vml-ivgcolor.md) .

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* color2=" *expression* ">

**Script Syntax**

*element* .color2="*expression*"

*expression*=*element*.color2

**Remarks**

A second color is used when a fill type is a pattern or a gradient. The default value is **White**.

*VML Standard Attribute*

**Example**

The shape's fill type is a pattern where the foreground fill is defined by the source image but the transparent background is defined by the second color.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="pattern" color2="green" src="myimage.gif"/>
   </v:shape>
```



 

 