---
title: Position Attribute (Shape)(VML)
description: Position Attribute (Shape)(VML)
ms.assetid: 64ffe754-298b-4cf1-a236-6a4bdcd27123
ms.topic: article
ms.date: 05/31/2018
---

# Position Attribute (Shape)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the type of positioning used to place an element. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="position: *expression* ">

**Script Syntax**

*element* .style.position="*expression*"

*expression*=*element*.style.position

**Remarks**

The **Position** attribute is similar to the standard HTML **Position** attribute used with style sheets.

Values include:



| Value    | Description                                                                                                                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static   | Default. The element is positioned according to the normal flow of the page. The **Top** and **Left** attributes are ignored. If the object is anchored inline, which only happens in Microsoft Word, this value is used. |
| absolute | The element is positioned relative to the parent, using the **Top** and **Left** attributes. This value is used by Microsoft Word and Microsoft Excel floating objects, and Microsoft PowerPoint slides.                  |
| relative | The element is positioned according to the normal flow of the page, but the **Top** and **Left** attributes are used. The overlap of overlapping elements is governed by the **Z-Index** attribute.                       |



 

*VML Standard Attribute*

**Example**

The position of the rectangle is displayed using the *relative* style.


```HTML
   <v:rect id=myrect fillcolor="red"
   style="position:relative;top:1;left:1;width:20;height:20">
   </v:rect>
```



[Position Attribute Example](/previous-versions/bb264090(v=vs.85)). (Requires Microsoft Internet Explorer 5 or greater.)

 

 