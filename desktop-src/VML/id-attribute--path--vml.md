---
title: ID Attribute (Path)(VML)
description: ID Attribute (Path)(VML)
ms.assetid: f0f3a526-d0e1-46f8-a85c-b99d27c3fdeb
ms.topic: article
ms.date: 05/31/2018
---

# ID Attribute (Path)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

A name that provides a unique identifier for a path. Read/write. **String**.

**Applies To**

[Path](msdn-online-vml-path-element.md)

**Tag Syntax**

<v: *element* id=" *expression* ">

**Script Syntax**

*element* .id="*expression*"

*expression*=*element*.id

**Remarks**

Use **ID** to refer to a specific path. Once you have created a path and given it an ID, you can use the ID name when you want to manipulate the path.

*VML Standard Attribute*

**Example**

The shape has a path ID called "myPath".


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50">
   <v:path id= "myPath" v="m 1,1 l 1,200, 200,200, 200,1 x e"/>
   </v:shape>
```



 

 