---
title: VML Margin-Left Attribute
description: VML Margin-Left Attribute
ms.assetid: 65488c47-06c2-4a8f-8d29-4837865465f4
ms.topic: article
ms.date: 05/31/2018
---

# VML Margin-Left Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the left edge of the shape's containing rectangle relative to the shape anchor. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="margin-left: *expression* ">

**Script Syntax**

*element* .style.marginleft="*expression*"

*expression*=*element*.style.marginleft

**Remarks**

The **Margin-Left** attribute is similar to the standard HTML **Margin-Left** attribute used with style sheets.

Note that **marginleft** is used instead of **margin-left** for scripting. Also note that if the **position** is **absolute**, the margin will not appear to change.

This property is used instead of **Left** for shapes in Microsoft Word and Microsoft Excel that are floating in a position relative to an anchor point.

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

The left margin is set to 25 pixels.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20;margin-left:25px">
   </v:rect>
```



[Margin-Left Attribute Example](/previous-versions/visualstudio/design-tools/expression-studio-3/ee371308(v=expression.40)#examples). (Requires Microsoft Internet Explorer 5 or greater.)

 

 