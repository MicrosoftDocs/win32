---
title: VML LockRotationCenter Attribute
description: VML LockRotationCenter Attribute
ms.assetid: 80b822d3-9122-475b-88ca-7019daa5de77
ms.topic: article
ms.date: 05/31/2018
---

# VML LockRotationCenter Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the rotation of the extruded object is specified by the [RotationAngle](msdn-online-vml-rotationangle-attribute.md) attribute. Read/write. **VgTriState**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* lockrotationcenter=" *expression* ">

**Script Syntax**

*element* .lockrotationcenter="*expression*"

*expression*=*element*.lockrotationcenter

**Remarks**

If **False**, the rotation is specified by the [Orientation](msdn-online-vml-orientation-attribute.md) attribute. The default is **True**.

Note that:


```HTML
   <o:extrusion lockrotationcenter="false" orientationangle="45" orientation="(0,1,0)"/>
```



is the same as:


```HTML
   <o:extrusion lockrotationcenter="true" rotationangle="45"/>
```



*Microsoft Office Extensions Attribute*

 

 