---
title: VML Vertices Attribute
description: VML Vertices Attribute
ms.assetid: 3b887ecb-19e8-4ebf-9db6-bf3ed4f7d589
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML Vertices Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether the vertices of a path can be changed by an editor. Read/write. **VgTriState**.

**Applies To**

[Locks](msdn-online-vml-locks-element.md)

**Tag Syntax**

<o: *element* vertices=" *expression* ">

**Remarks**

If **True**, the edit points of the vertices of a path are locked. The default value is **True** for Microsoft Office AutoShapes, but otherwise is **False**.

*Microsoft Office Extensions Attribute*

 

 




