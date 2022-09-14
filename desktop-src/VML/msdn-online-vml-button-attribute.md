---
title: VML Button Attribute
description: VML Button Attribute
ms.assetid: 273024ac-683f-48d2-b6a0-574824f4c05d
ms.topic: article
ms.date: 05/31/2018
---

# VML Button Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a shape will be processed as a button. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:button=" *expression* ">

**Remarks**

The default is **False**. If **True**, the shape is processed as a button.

*Microsoft Office Extensions Attribute*

**Example**

The shape is a button.


```HTML
   <v:rect id=myrect fillcolor="red" o:button="True"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 