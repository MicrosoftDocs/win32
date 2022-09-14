---
title: VML Switch Attribute
description: VML Switch Attribute
ms.assetid: fc099c0a-6789-41e8-ab08-36f4fd2d3bfa
ms.topic: article
ms.date: 05/31/2018
---

# VML Switch Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the handle directions are swapped. Read/write. **VgTriState**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

<v: *element* switch=" *expression* ">

**Remarks**

If **True**, the handle is switched between the x and y directions if the shape is taller than it is wide. The default value is **False**.

This attribute is used for shapes with limo stretch behavior.

*VML Standard Attribute*

 

 