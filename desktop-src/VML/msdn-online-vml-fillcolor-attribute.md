---
title: VML FillColor Attribute
description: VML FillColor Attribute
ms.assetid: c18302e1-86a5-4046-811f-576a746ea398
ms.topic: article
ms.date: 05/31/2018
---

# VML FillColor Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the brush color that fills the closed path of a shape. Read/write. [IVgColor](msdn-online-vml-ivgcolor.md) .

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* fillcolor=" *expression* ">

**Script Syntax**

*element* .fillcolor="*expression*"

*expression*=*element*.fillcolor

**Remarks**

The **FillColor** value is duplicated from the **Color** attribute of the **Fill** element.

*VML Standard Attribute*

**See Also**

[Shape](shape-element--vml.md), [Fill](msdn-online-vml-fill-element.md), [IVgColor](msdn-online-vml-ivgcolor.md)

**Example**

The fill color of the rectangle is red.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



[FillColor Attribute Example](/previous-versions/bb229668(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 