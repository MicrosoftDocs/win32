---
title: VML ExtrusionOK Attribute
description: VML ExtrusionOK Attribute
ms.assetid: 7060c744-5227-4a1e-b073-c5b5a823f8cd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML ExtrusionOK Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether an extrusion will be displayed. Read/write. **VgTriState**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

&lt;v: *element* o:extrusionok=" *expression* "&gt;

**Remarks**

If **False**, the path cannot have an extrusion. The default is **True**. This attribute overrides all other extrusion attributes in the parent or **Extrusion** element.

*Microsoft Office Extensions Attribute*

 

 




