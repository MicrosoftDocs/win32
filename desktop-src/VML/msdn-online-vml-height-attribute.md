---
title: VML Height Attribute
description: VML Height Attribute
ms.assetid: 5667ddc5-c840-40d8-894e-58396f56e0fc
ms.topic: article
ms.date: 05/31/2018
---

# VML Height Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies the height of the shape. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="height: *expression* ">

**Script Syntax**

*element* .style.height="*expression*"

*expression*=*element*.style.height

**Remarks**

The **Height** attribute is similar to the standard HTML **Height** attribute for styles.

Units may be mapped to the parent element or may be in absolute units.

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

The height of the shape is set to 30.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:30">
   </v:rect>
```



[Height Attribute Example](/previous-versions/bb229671(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 