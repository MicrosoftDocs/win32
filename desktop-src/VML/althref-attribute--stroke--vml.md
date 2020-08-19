---
title: AltHRef Attribute (Stroke)(VML)
description: AltHRef Attribute (Stroke)(VML)
ms.assetid: ee7c1710-1f8e-42c4-895f-d0f3d15ca6db
ms.topic: article
ms.date: 05/31/2018
---

# AltHRef Attribute (Stroke)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies an alternate reference for an image. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* o:althref=" *expression* ">

**Script Syntax**

*element* .althref="*expression*"

*expression*=*element*.althref

**Remarks**

Supports preservation of PICT data through HTML roundtripping. On HTML write, the alternate representation (i.e., the original PICT data if the file originated from the Macintosh) is saved. On HTML read, **AltHRef** is favored over **Src**.

*Microsoft Office Extensions Attribute*

**Example**

The stroke of the shape has an **AltHRef** that points to a file named myimage.gif.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200,200, 200, 200,1 x e">
   <v:stroke o:althref="myimage.gif"/>
   </v:shape>
```



 

 