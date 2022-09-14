---
title: VML Obscured Attribute
description: VML Obscured Attribute
ms.assetid: b8cdb066-e4fc-4dd6-a55a-7c2488f89e61
ms.topic: article
ms.date: 05/31/2018
---

# VML Obscured Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a shadow is transparent. Read/write. **VgTriState**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* obscured=" *expression* ">

**Script Syntax**

*element* .obscured="*expression*"

*expression*=*element*.obscured

**Remarks**

If **True**, lets you see through the shadow if there is no fill on the shape. Default is **False**.

*VML Standard Attribute*

**Example**

The background shows through the shadow.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m1,1 l 1,200,200,200, 200,1 x e">
   <v:shadow on="True" obscured="True"/>
   </v:shape>
```



 

 