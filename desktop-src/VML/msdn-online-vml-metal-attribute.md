---
title: VML Metal Attribute
description: VML Metal Attribute
ms.assetid: 4d2efaed-d391-494f-9f0c-d57ad019f71d
ms.topic: article
ms.date: 05/31/2018
---

# VML Metal Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the surface of the extruded shape will resemble metal. Read/write. **VgTriState**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* metal=" *expression* ">

**Script Syntax**

*element* .metal="*expression*"

*expression*=*element*.metal

**Remarks**

If set to **True**, this attribute causes the specularly reflected light to be the material color instead of the light source color, making the object seem more metallic.To further approximate a metallic material requires that specularity be relatively high (about 1.2) and diffusity be relatively low (about 0.6). The default value is **False**.

*Microsoft Office Extensions Attribute*

 

 