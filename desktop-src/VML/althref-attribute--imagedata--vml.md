---
title: AltHRef Attribute (ImageData)(VML)
description: AltHRef Attribute (ImageData)(VML)
ms.assetid: c55ede90-3d57-4f27-9940-1fe4751cef71
ms.topic: article
ms.date: 05/31/2018
---

# AltHRef Attribute (ImageData)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies an alternate reference for an image. Read/write. **String**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* o:althref=" *expression* ">

**Script Syntax**

*element* .althref="*expression*"

*expression*=*element*.althref

**Remarks**

Supports preservation of PICT data through HTML roundtripping. On HTML write, the alternate representation (that is, the original PICT data if the file originated from the Macintosh) is saved. On an HTML read, **AltHRef** is favored over **Src**.

*Microsoft Office Extensions Attribute*

 

 