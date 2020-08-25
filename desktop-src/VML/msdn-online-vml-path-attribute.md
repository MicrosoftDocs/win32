---
title: VML Path Attribute
description: VML Path Attribute
ms.assetid: ecb64a2f-65f7-4eb9-8d67-d7909bf52d9c
ms.topic: article
ms.date: 05/31/2018
---

# VML Path Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the line that makes up the edges of a shape. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* path=" *expression* ">

**Script Syntax**

*element* .path="*expression*"

*expression*=*element*.path

**Remarks**

If a shape contains the [Path](msdn-online-vml-path-element.md) element, the path commands of the Path element take precedence over the shape attribute value. See the **Path** element topic for details on the command set used for paths.

*VML Standard Attribute*

**Example**

A closed square path is defined in the string of the path attribute. An initial point is defined with `m` (used for the **moveto** command) at 1,1 and a line is drawn with `l` (the letter "L" used for the command **lineto**) from the starting position (1,1) to the other three points (in order): 1,200; 200,200; 200,1. The line is closed with `x` (**close**) and ended with `e` (**end**). Note that coordinates are given in the relative coordinate space and that the real size is determined by the **width** and **height**.


```HTML
   <v:shape id="rect01"
   fillcolor="red" strokecolor="red"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1;width:20;height:20"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[Path Attribute Example](/previous-versions/bb264089(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 