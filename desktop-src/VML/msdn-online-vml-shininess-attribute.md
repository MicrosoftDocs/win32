---
title: VML Shininess Attribute
description: VML Shininess Attribute
ms.assetid: 99c301ff-ed61-48ef-95bb-ceaed1a2553c
ms.topic: article
ms.date: 05/31/2018
---

# VML Shininess Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the concentration of the reflected light on an extrusion surface. Read/write. **VgNumber**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* shininess=" *expression* ">

**Script Syntax**

*element* .shininess="*expression*"

*expression*=*element*.shininess

**Remarks**

High values (8-10) would approximate the shininess of a mirror and low values (2-3) would approximate a speckled effect. Values of 4-7 are typical. Reflections do not mirror other objects; only pinpoint light sources are reflected. Default value is 5.

*Microsoft Office Extensions Attribute*

 

 