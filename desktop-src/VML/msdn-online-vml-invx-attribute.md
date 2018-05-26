---
title: VML InvX Attribute
description: VML InvX Attribute
ms.assetid: 59fbd4c0-ae31-4198-a9e7-be12cd50288f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML InvX Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether the x position of the handle is inverted. Read/write. **VgTriState**.

**Applies To**

[H](msdn-online-vml-h-element.md) (subelement of [Handles](msdn-online-vml-handles-element.md))

**Tag Syntax**

&lt;v: *element* invx=" *expression* "&gt;

**Remarks**

If **True**, the x position of the handle is inverted by subtracting the x value from the x value of **CoordOrigin** added to the x value of **CoordSize**. The default value is **False**.

This attribute is the equivalent of

coordorigin.x + coordsize.x - h.position.x

*VML Standard Attribute*

 

 




