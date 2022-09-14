---
title: VML EndAngle Attribute
description: VML EndAngle Attribute
ms.assetid: fc8276dc-8f61-42f4-b405-e92ca31e4637
ms.topic: article
ms.date: 05/31/2018
---

# VML EndAngle Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the endpoint of the arc. Read/write. [VgAngleInDegrees](msdn-online-vml-vgangleindegrees-data-type.md) .

**Applies To**

[Arc](msdn-online-vml-arc-element.md)

**Tag Syntax**

<v: *element* endangle=" *expression* ">

**Script Syntax**

*element* .endAngle="*expression*"

*expression*=*element*.endAngle

**Remarks**

The arc is defined as a stroke drawn along an oval bounded by the **Style** attributes of a shape. The end of the stroke is defined by an angle measured from straight up (12 o'clock) clockwise. The default value is 90 degrees.

*VML Standard Attribute*

**Example**

The arc is smiling. The start point is at the 90-degree point of an oval inscribed inside the shape bounding box. The end point is at the 270-degree point of the oval.


```HTML
   <v:arc id="myarc"
   style="position:relative;top:10;left:10;width:200;height:200"
   startangle="90" endangle="270">
   </v:arc>
```



 

 