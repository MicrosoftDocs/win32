---
title: VML RotationAngle Attribute
description: VML RotationAngle Attribute
ms.assetid: d5432512-1ac2-497b-a415-cec3c1217120
ms.topic: article
ms.date: 05/31/2018
---

# VML RotationAngle Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the rotation of the object about the x and y -axes. Read/write. **VgVector2D**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* rotationangle=" *expression* ">

**Script Syntax**

*element* .rotationangle="*expression*"

*expression*=*element*.rotationangle

**Remarks**

The rotation of the object is defined by a rotation angle about the y-axis followed by the rotation angle about the x-axis.The z-axis angle is controlled by the value of the shape's standard HTML Style **Rotation** attribute. The default value is 0,0.

*Microsoft Office Extensions Attribute*

 

 