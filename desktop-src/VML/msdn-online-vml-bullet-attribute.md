---
title: VML Bullet Attribute
description: VML Bullet Attribute
ms.assetid: 17c24b97-191b-4170-8a2d-9284f500e728
ms.topic: article
ms.date: 05/31/2018
---

# VML Bullet Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a shape is a graphical bullet. Read/write **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:bullet=" *expression* ">

**Remarks**

The default is **False**. If **True**, the shape is a graphical bullet.

*Microsoft Office Extensions Attribute*

**Example**

The shape is a bullet.


```HTML
   <v:rect id=myrect fillcolor="red" o:bullet="True"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 