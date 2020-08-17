---
title: VML Stroked Attribute
description: VML Stroked Attribute
ms.assetid: 3a62a04b-8165-4d83-8b6d-d5e9bbde2796
ms.topic: article
ms.date: 05/31/2018
---

# VML Stroked Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines whether the path will be stroked. Read/write. [VgTriState](msdn-online-vml-vgtristate.md) .

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* stroked=" *expression* ">

**Script Syntax**

*element* .stroked="*expression*"

*expression*=*element*.stroked

**Remarks**

The value is duplicated from the **On** attribute of the [Stroke](msdn-online-vml-stroke-element.md) element.

*VML Standard Attribute*

**Example**

The shape path is stroked.


```HTML
   <v:shape id="rect01" stroked="True"
   strokecolor="red" fillcolor="white"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1;width:20;height:20"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[Stroked Attribute Example](/previous-versions/bb264094(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 