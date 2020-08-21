---
title: VML ForceDash Attribute
description: VML ForceDash Attribute
ms.assetid: 659e99bb-16d9-425a-97b1-7767c065ec41
ms.topic: article
ms.date: 05/31/2018
---

# VML ForceDash Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a dashed outline is used to draw a shape when a shape has no line or fill. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:forcedash=" *expression* ">

**Remarks**

Used by Microsoft PowerPoint placeholders to draw a dashed outline when there is no line and no fill for a shape. Default is **False**. If **True**, a dashed outline will be used to indicate a placeholder.

*Microsoft Office Extensions Attribute*

**Example**

A dashed line will be used to render the shape if there is no line or fill.


```HTML
   <v:rect id=myrect fillcolor="red" o:forcedash="True"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 