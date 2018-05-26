---
title: VML Obscured Attribute
description: VML Obscured Attribute
ms.assetid: b8cdb066-e4fc-4dd6-a55a-7c2488f89e61
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML Obscured Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Determines whether a shadow is transparent. Read/write. **VgTriState**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

&lt;v: *element* obscured=" *expression* "&gt;

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



 

 




