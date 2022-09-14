---
title: VML Offset2 Attribute
description: VML Offset2 Attribute
ms.assetid: a2792992-71a1-4932-8180-82ca38bd6dd2
ms.topic: article
ms.date: 05/31/2018
---

# VML Offset2 Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines a second offset. Read/write. **VgVector2D**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* offset2=" *expression* ">

**Script Syntax**

*element* .offset2="*expression*"

*expression*=*element*.offset2

**Remarks**

The default for a second offset for the x value is 0 and the default for the y value is 0. Values are either an absolute measurement, or a fractional value of shape. If fractional, the values range from 50% to -50%.

Use a second offset to create special shadow effects. See the [Type](type-attribute--shadow--vml.md) attribute for more information about second offsets.

*VML Standard Attribute*

**Example**

A double shadow is created for the shape.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:shadow on="True" color="red" color2="blue"
   offset="50%" offset2="-20%" type="double"/>
   </v:shape>
```



 

 