---
title: VML StrokeWeight Attribute
description: VML StrokeWeight Attribute
ms.assetid: 364882b2-e5f4-4a86-b7d7-352f8780ebdc
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VML StrokeWeight Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the brush thickness that strokes the path of a shape. Read/write. **VGLength**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

&lt;v: *element* strokeweight=" *expression* "&gt;

**Script Syntax**

*element* .strokeweight="*expression*"

*expression*=*element*.strokeweight

**Remarks**

The value is duplicated from the **Weight** attribute of the **Stroke** element. If a number is specified, but no units are added, the default unit of measurement is the Emu. If no value is specified, the default is 1 pixel (1px).

For scripting, however, the default unit of measurement is in points.

*VML Standard Attribute*

**See Also**

[Stroke](msdn-online-vml-stroke-element.md), [IVgLength](msdn-online-vml-vglength.md), [Units](msdn-online-vml-units.md)

**Example**

The stroke weight of the shape is 1 point.


```HTML
   <v:shape id="rect01" strokeweight="1pt"
   strokecolor="red" fillcolor="white"
   coordorigin="0 0" coordsize="200 200"
   style="position:relative;top:1;left:1;width:20;height:20"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



[StrokeWeight Attribute Example](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/examples/x_strwgt.md). (Requires Microsoft Internet Explorer 5 or greater.)

 

 




