---
title: Offset Attribute (Shadow)(VML)
description: Offset Attribute (Shadow)(VML)
ms.assetid: bb5810cd-bd9a-4888-a0ce-8de732215c80
ms.topic: article
ms.date: 05/31/2018
---

# Offset Attribute (Shadow)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines how far the shadow extends past the shape. Read/write. **VgVector2D**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* offset=" *expression* ">

**Script Syntax**

*element* .offset="*expression*"

*expression*=*element*.offset

**Remarks**

The default offset for the x value is 2pt and the default for the y value is 2pt. Values are either an absolute measurement, or a fractional value of shape. If fractional, they range from 50% to -50%.

*VML Standard Attribute*

**Example**

The shape has a shadow with an offset of 5 points down and 10 points to the right.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:shadow on="True" offset="10pt,5pt"/>
   </v:shape>
```



 

 