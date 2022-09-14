---
title: VML DoubleClickNotify Attribute
description: VML DoubleClickNotify Attribute
ms.assetid: 003a87f5-29c1-484e-ac15-2e4cb8e854ad
ms.topic: article
ms.date: 05/31/2018
---

# VML DoubleClickNotify Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Sends an event message when a shape is double-clicked. Read/write. **VgTriState**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* o:doubleclicknotify=" *expression* ">

**Remarks**

The default value is **False**, indicating that the event will not be fired.

*Microsoft Office Extensions Attribute*

**Example**

The shape will trigger a double-click event when double-clicked.


```HTML
   <v:rect id=myrect fillcolor="red" o:doubleclicknotify="True"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



 

 