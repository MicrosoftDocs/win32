---
title: VML RadiusRange Attribute
description: VML RadiusRange Attribute
ms.assetid: bff2b185-7683-4994-9104-09a7579f963d
ms.topic: article
ms.date: 05/31/2018
---

# VML RadiusRange Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the range of a polar handle. Read/write. **VgVector2D**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

<v: *element* radiusrange=" *expression* ">

**Remarks**

A minimum and maximum value is defined for a radial handle. Each value can be a constant or a formula. If a value is not defined, the handle can be moved without limit in the radial direction. This attribute applies only to polar adjust handles. The default value is 0,0.

*VML Standard Attribute*

 

 