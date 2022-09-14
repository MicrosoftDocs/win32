---
title: VML Margin-Right Attribute
description: VML Margin-Right Attribute
ms.assetid: 7b635bea-df3f-4a24-aa22-cfca95575599
ms.topic: article
ms.date: 05/31/2018
---

# VML Margin-Right Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the right edge of the shape's containing rectangle relative to the shape anchor. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="margin-right: *expression* ">

**Script Syntax**

*element* .style.marginright="*expression*"

*expression*=*element*.style.marginright

**Remarks**

The **Margin-Right** attribute is similar to the standard HTML **Margin-Right** attribute used with style sheets.

Note that **marginright** is used instead of **margin-right** for scripting. Also note that if the **position** is **absolute**, the margin will not appear to change.

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

The right margin is set to 25 pixels.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;margin-right:25px">
   </v:rect>
```



[Margin-Right Attribute Example](/previous-versions/bb229677(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 