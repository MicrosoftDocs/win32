---
title: VML Margin-Bottom Attribute
description: VML Margin-Bottom Attribute
ms.assetid: c1101430-f4fc-4fa5-8e02-7cee126c2c1c
ms.topic: article
ms.date: 05/31/2018
---

# VML Margin-Bottom Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the bottom edge of the shape's containing rectangle relative to the shape anchor. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* margin-bottom=" *expression* ">

**Script Syntax**

*element* .marginbottom="*expression*"

*expression*=*element*.marginbottom

**Remarks**

The **Margin-Bottom** attribute is similar to the standard HTML **Margin-Bottom** attribute used with style sheets.

Note that **marginbottom** is used instead of **margin-bottom** for scripting. Also note that if the **position** is **absolute**, the margin will not appear to change.

Values include:



| Value      | Description                                                                                                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto       | Default position of an element in the flow of the page.                                                                                                                                           |
| units      | Default. A number with an absolute units designator (cm, mm, in, pt, pc, or px) or a relative units designator (em or ex). If no units are given, pixels (px) is assumed. The default value is 0. |
| percentage | Value expressed as a percentage of the parent object's height.                                                                                                                                    |



 

*VML Standard Attribute*

**See Also**

[Units](msdn-online-vml-units.md)

**Example**

The bottom margin is set to 25 pixels.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;margin-bottom:25px">
   </v:rect>
```



[Margin-Bottom Attribute Example](/previous-versions/bb229675(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 