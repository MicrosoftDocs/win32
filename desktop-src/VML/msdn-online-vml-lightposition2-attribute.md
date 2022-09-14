---
title: VML LightPosition2 Attribute
description: VML LightPosition2 Attribute
ms.assetid: 75ae4154-240f-4981-a527-d9e0a721e8b4
ms.topic: article
ms.date: 05/31/2018
---

# VML LightPosition2 Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the position of the secondary light in a scene. Read/write. **VgVector3D**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* lightposition2=" *expression* ">

**Script Syntax**

*element* .lightposition2="*expression*"

*expression*=*element*.lightposition2

**Remarks**

Use this value to move the second light source for an extrusion. Different positions will lighten or darken each face of the extrusion. The default value is -50000, 0, 10000.

*Microsoft Office Extensions Attribute*

 

 