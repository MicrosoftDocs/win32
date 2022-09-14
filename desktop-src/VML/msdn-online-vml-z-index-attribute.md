---
title: VML Z-Index Attribute
description: VML Z-Index Attribute
ms.assetid: 54a2c556-e40e-462e-a621-ec07911d5261
ms.topic: article
ms.date: 05/31/2018
---

# VML Z-Index Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines the display order of overlapping shapes. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="z-index: *expression* ">

**Script Syntax**

*element* .style.zindex="*expression*"

*expression*=*element*.style.zindex

**Remarks**

The **Z-Index** attribute is similar to the standard HTML **Z-Index** attribute for styles.

Values include:



| Value | Description                                                                                                                                                                                            |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto  | The order that the shapes appear in the HTML page will be used, bottom to top.                                                                                                                         |
| order | A number that represents the stacking precedence. A shape with a a higher number will be displayed as if it wereoverlapping (in "front" of) a shape with a lower number. Negative numbers can be used. |



 

*VML Standard Attribute*

**Example**

The red shape will be displayed in "front" of the blue shape, because it has a higher z-index.


```HTML
   <v:rect id=bluerect fillcolor="blue"
   style="position:relative;top:1;left:1;width:20;height:20;z-index:1">
   </v:rect>
   <v:rect id=redrect fillcolor="red"
   style="position:relative;top:10;left:10;width:20;height:20;z-index:2">
   </v:rect>
```



[Z-Index Attribute Example](/previous-versions/ms530275(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 