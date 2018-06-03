---
title: VML ColorMode Attribute
description: VML ColorMode Attribute
ms.assetid: 92c885ca-7912-42ff-8f07-e6e779e0ef05
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML ColorMode Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines the mode of extrusion color. Read/write. **VgTriState**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

&lt;o: *element* colormode=" *expression* "&gt;

**Script Syntax**

*element* .colormode="*expression*"

*expression*=*element*.colormode

**Remarks**

Values include:



| Value  | Description                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------|
| auto   | Specifies that the color of the extrusion is the same as the fill color of the shape. Default.                |
| custom | Specifies that the extrusion will be the color of the [Color](color-attribute--extrusion--vml.md) attribute. |



 

*Microsoft Office Extensions Attribute*

 

 




