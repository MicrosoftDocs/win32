---
title: VML AutoRotationCenter Attribute
description: VML AutoRotationCenter Attribute
ms.assetid: beb6771f-42f4-458a-b525-4eb67bc1eff0
ms.topic: article
ms.date: 05/31/2018
---

# VML AutoRotationCenter Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the center of rotation will be the geometric center of the extrusion. Read/write. **VgTriState**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* autorotationcenter=" *expression* ">

**Script Syntax**

*element* .autorotationcenter="*expression*"

*expression*=*element*.autorotationcenter

**Remarks**

The geometric center of an extruded shape is 0,0,0. If the value of this attribute is **False**, the center of rotation is determined by the [RotationCenter](msdn-online-vml-rotationcenter-attribute.md) attribute. The default is **False**.

*Microsoft Office Extensions Attribute*

 

 