---
title: AltHRef Attribute (Fill)(VML)
description: AltHRef Attribute (Fill)(VML)
ms.assetid: 3f6376e3-24db-412c-b265-5916950c3824
ms.topic: article
ms.date: 05/31/2018
---

# AltHRef Attribute (Fill)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines an alternate reference for an image. Read/write. **String**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* o:althref=" *expression* ">

**Script Syntax**

*element* .althref="*expression*"

*expression*=*element*.althref

**Remarks**

Supports preservation of PICT data through HTML roundtripping. On HTML write, the alternate representation (the original PICT data if the file originated from the Apple Macintosh) is saved. On HTML read, **AltHRef** is favored over **Src**.

*Microsoft Office Extensions Attribute*

**Example**

The fill of the shape has an **AltHRef** that points to a file named myimage.gif.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill o:althref="myimage.gif"/>
   </v:shape>
```



 

 