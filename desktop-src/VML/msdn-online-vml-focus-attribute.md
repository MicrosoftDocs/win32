---
title: VML Focus Attribute
description: VML Focus Attribute
ms.assetid: 9ed52203-4142-47cd-851f-74230aac934d
ms.topic: article
ms.date: 05/31/2018
---

# VML Focus Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the center of a linear gradient fill. Read/write. **VgFraction**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* focus=" *expression* ">

**Script Syntax**

*element* .focus="*expression*"

*expression*=*element*.focus

**Remarks**

Defines the center starting position of the blend. Values range from 100% to -100%. The default value is 0. A value of 100% (or -100%) will shift the focus so that the direction of the blend will reverse (in effect reversing **Color** and **Color2**). A value of 50% will change the blend so that **Color** is at both ends and **Color2** is in the middle. A value of -50% will change the blend so that **Color2** is at both ends and **Color** is in the middle.

*VML Standard Attribute*

**Example**

The gradient focus of the fill is shifted so that red (**Color**) will be a band in the center of the shape and that the top and bottom will be blue (**Color2**).


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill type="gradient" color="red" color2="blue"
   method="linear" focus="-50%"/>
   </v:shape>
```



 

 