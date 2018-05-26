---
title: VML Polar Attribute
description: VML Polar Attribute
ms.assetid: b7ea8764-057d-4c14-81ad-77ae82b1aa31
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML Polar Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Specifies the center position for polar handles. Read/write. **VgVector2D**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

&lt;v: *element* polar=" *expression* "&gt;

**Remarks**

The default value is a null string. If values are specified, this indicates that the measurement is polar and that the [Position](position-attribute--h--vml.md) attribute defines radius and angle values of the handle instead of x and y values.

*VML Standard Attribute*

 

 




