---
title: Color Attribute (Shadow)(VML)
description: Color Attribute (Shadow)(VML)
ms.assetid: 677615b7-b4a4-411f-b04e-3ed0399f4c05
ms.topic: article
ms.date: 05/31/2018
---

# Color Attribute (Shadow)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the color of the shadow. Read/write. **VgColor**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* color=" *expression* ">

**Script Syntax**

*element* .color="*expression*"

*expression*=*element*.color

**Remarks**

Use the color attribute to set or get the color of a shadow.

*VML Standard Attribute*

**Example**

The shadow is green.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:shadow on="True" color="green"/>
   </v:shape>
```



 

 