---
title: VML Diffusity Attribute
description: VML Diffusity Attribute
ms.assetid: 1d131540-9166-47fc-bb0d-fada38f6a3de
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML Diffusity Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the amount of diffusion of reflected light from an extruded shape. Read/write. **VgNumber**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

&lt;o: *element* diffusity=" *expression* "&gt;

**Script Syntax**

*element* .diffusity="*expression*"

*expression*=*element*.diffusity

**Remarks**

This value defines the ratio of incident light to diffused reflected light. Normal values range from 0 to 1. The default value is 0.

If values greater than 1 are specified, unusual effects can result.

*Microsoft Office Extensions Attribute*

 

 




