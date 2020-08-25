---
title: VML Plane Attribute
description: VML Plane Attribute
ms.assetid: e1de630b-8e25-4052-b316-251046f73e98
ms.topic: article
ms.date: 05/31/2018
---

# VML Plane Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the plane that is at right angles to the extrusion. Read/write. **String**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* plane=" *expression* ">

**Script Syntax**

*element* .plane="*expression*"

*expression*=*element*.plane

**Remarks**

Values include:



| Value | Description                                            |
|-------|--------------------------------------------------------|
| xy    | Extrusion is at right angles to the xy -plane. Default |
| zx    | Extrusion is at right angles to the zx -plane.         |
| yz    | Extrusion is at right angles to the yz -plane.         |



 

*Microsoft Office Extensions Attribute*

 

 