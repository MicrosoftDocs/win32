---
title: VML Specularity Attribute
description: VML Specularity Attribute
ms.assetid: df04c15c-cfad-4172-81fa-a28e13f205fc
ms.topic: article
ms.date: 05/31/2018
---

# VML Specularity Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the specularity of an extruded shape. Read/write. **VgNumber**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* specularity=" *expression* ">

**Script Syntax**

*element* .specularity="*expression*"

*expression*=*element*.specularity

**Remarks**

This value defines the ratio of incident light to specularly reflected light. Normal values range from 0 to 1. The default value is 0.

If values greater than 1 are specified, unusual effects can result.

Microsoft Office Extensions Attribute

 

 