---
title: VML LightFace Attribute
description: VML LightFace Attribute
ms.assetid: 552a4145-fb34-4a85-a32a-c9ef74f11f13
ms.topic: article
ms.date: 05/31/2018
---

# VML LightFace Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the front face of the extrusion will respond to changes in the lighting. Read/write. **VgTriState**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* lightface=" *expression* ">

**Script Syntax**

*element* .lightface="*expression*"

*expression*=*element*.lightface

**Remarks**

If **False**, the front face will not respond when a lighting value changes. The default is **True**.

*Microsoft Office Extensions Attribute*

 

 