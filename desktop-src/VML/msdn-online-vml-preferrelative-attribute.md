---
title: VML PreferRelative Attribute
description: VML PreferRelative Attribute
ms.assetid: 7de616e8-4fc3-4bcb-8e5e-ea153d6d4b54
ms.topic: article
ms.date: 05/31/2018
---

# VML PreferRelative Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the original size of an object is saved after reformatting. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:preferrelative=" *expression* ">

**Remarks**

The default is **False**. If **True**, the original size of the object will be stored and all resizing will be based on a percentage of that original size. Otherwise, each resizing will reset the scale to 100%.

*Microsoft Office Extensions Attribute*

**Example**

If the shape is resized, the original size will not be stored.


```HTML
   <v:rect id=myrect fillcolor="red" preferrelative="False"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 