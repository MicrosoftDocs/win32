---
title: VML Filled Attribute
description: VML Filled Attribute
ms.assetid: c5a71a8d-5310-4e58-9153-c5cc64b0a5e0
ms.topic: article
ms.date: 05/31/2018
---

# VML Filled Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the closed path will be filled. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* filled=" *expression* ">

**Script Syntax**

*element* .filled="*expression*"

*expression*=*element*.filled

**Remarks**

The value is duplicated from the **On** attribute of the [Fill](msdn-online-vml-fill-element.md) element.

*VML Standard Attribute*

**Example**

The shape path is filled.


```HTML
   <v:shape id="rect01" filled="True"
   strokecolor="red" fillcolor="white"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1;width:20;height:20"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[Filled Attribute Example](/previous-versions/bb229669(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 