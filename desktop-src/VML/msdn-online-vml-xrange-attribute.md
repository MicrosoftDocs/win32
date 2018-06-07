---
title: VML XRange Attribute
description: VML XRange Attribute
ms.assetid: c2881fd6-08b2-4ec8-b4fd-b271a049da09
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML XRange Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines thexrange of a handle. Read/write **VgVector2D**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

&lt;v: *element* xrange=" *expression* "&gt;

**Remarks**

A minimum and maximum value is defined for the handle in the x direction. Each value can be a constant or a formula. If a value is not defined, the handle can be moved without limit in this direction. The default value is 0,0.

*VML Standard Attribute*

 

 




