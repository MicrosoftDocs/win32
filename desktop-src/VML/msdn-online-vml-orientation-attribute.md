---
title: VML Orientation Attribute
description: VML Orientation Attribute
ms.assetid: 62298908-6e88-470d-bca2-0cfc1a38c2eb
ms.topic: article
ms.date: 05/31/2018
---

# VML Orientation Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the vector around which a shape can be rotated. Read/write. **VgVector3D**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* orientation=" *expression* ">

**Script Syntax**

*element* .orientation="*expression*"

*expression*=*element*.orientation

**Remarks**

Use the [OrientationAngle](msdn-online-vml-orientationangle-attribute.md) attribute to specify the amount of rotation around this vector. Default value is 100,0,0.

*Microsoft Office Extensions Attribute*

 

 