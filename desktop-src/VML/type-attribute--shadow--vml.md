---
title: Type Attribute (Shadow)(VML)
description: Type Attribute (Shadow)(VML)
ms.assetid: 569957c6-508a-4323-804d-25f9a3e58c38
ms.topic: article
ms.date: 05/31/2018
---

# Type Attribute (Shadow)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the type of shadow. Read/write. **String**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* type=" *expression* ">

**Script Syntax**

*element* .type="*expression*"

*expression*=*element*.type

**Remarks**

Values include:



| Value           | Description                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| single          | Single shadow. Default.                                                                                                                                                                              |
| double          | A double shadow. [Color2](color2-attribute--shadow--vml.md) is used for the color of the second shadow and [Offset2](msdn-online-vml-offset2-attribute.md) is used for the second shadow's offset. |
| perspective     | A perspective shadow.                                                                                                                                                                                |
| shapeRelative   | The shadow is created relative to the shape.                                                                                                                                                         |
| drawingRelative | The shadow is created relative to the drawing.                                                                                                                                                       |
| emboss          | The shadow has an embossed look.                                                                                                                                                                     |



 

**VML Standard Attribute**

**Example**

A double shadow is created with the second shadow green and offset 5 points down and to the right.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:shadow on="True" type="double" color2="green" offset2="5pt,5pt"/>
   </v:shape>
```



 

 