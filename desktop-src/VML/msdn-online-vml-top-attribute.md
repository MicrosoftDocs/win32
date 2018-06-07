---
title: VML Top Attribute
description: VML Top Attribute
ms.assetid: faad0c76-3566-4a51-962b-971667df2025
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML Top Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the position of the shape relative to the element above it in the flow of the page. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

&lt;v: *element* style="top: *expression* "&gt;

**Script Syntax**

*element* .style.top="*expression*"

*expression*=*element*.style.top

**Remarks**

The **Top** attribute is similar to the standard HTML **Top** attribute for styles.

Units may be mapped to the parent element or may be in absolute units. This attribute may not be written out for shapes anchored inline.

Values include:



| Value      | Description                                                                                                                                                      |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto       | Default position of an element in the flow of the page.                                                                                                          |
| units      | A number with an absolute units designator (cm, mm, in, pt, pc, or px) or a relative units designator (em or ex). If no units are given, pixels (px) is assumed. |
| percentage | Value expressed as a percentage of the parent object's height.                                                                                                   |



 

*VML Standard Attribute*

**See Also**

[Units](msdn-online-vml-units.md)

**Example**

The top edge of the shape is 5 pixels below the object that precedes it in the flow of the page.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:5;left:1;width:20;height:20">
   </v:rect>
```



[Top Attribute Example](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/examples/x_top.md). (Requires Microsoft Internet Explorer 5 or greater.)

 

 




