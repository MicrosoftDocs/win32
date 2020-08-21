---
title: VML ReGroupID Attribute
description: VML ReGroupID Attribute
ms.assetid: 2fbcc8c5-6e31-4301-9fb8-c2618bb17a1b
ms.topic: article
ms.date: 05/31/2018
---

# VML ReGroupID Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a previous group for a shape. Read/write. **VgInteger**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:regroupid=" *expression* ">

**Remarks**

An ID number is used to identify groups of shapes that are no longer grouped. Allows shapes to be regrouped programmatically.

*Microsoft Office Extensions Attribute*

**Example**

The shape was part of a group denoted by the group ID 040754.


```HTML
   <v:shape id="rect01" ReGroupID="040754"
   fillcolor="red" strokecolor="red"
   coordorigin="-500 -500" coordsize="1000 1000"
   style="position:relative;top:0;left:0;width:100pt;height:100pt;mso-wrap-distance-top:10pt"
   path="m 5,5 l 5,195, 195,195, 195,5 x e">
   </v:shape>
```



 

 