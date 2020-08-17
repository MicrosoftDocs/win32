---
title: VML StrokeOK Attribute
description: VML StrokeOK Attribute
ms.assetid: f150f87b-1ed9-4c53-bf7f-ebe1e81642fd
ms.topic: article
ms.date: 05/31/2018
---

# VML StrokeOK Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether a stroke will be displayed. Read/write. **VgTriState**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* strokeok=" *expression* ">

**Script Syntax**

*element* .strokeok="*expression*"

*expression*=*element*.strokeok

**Remarks**

If **False**, the path cannot be stroked. The default is **True**. This attribute overrides all other stroke attributes in the parent or **Stroke** element.

*VML Standard Attribute*

**Example**

The path will not be stroked.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50">
   <v:path id="myPath" strokeok="False" v="m 1,1 l 1,200, 200,200, 200,1 x e"/>
   </v:shape>
```



 

 