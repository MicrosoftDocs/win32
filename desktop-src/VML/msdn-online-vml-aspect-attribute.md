---
title: VML Aspect Attribute
description: VML Aspect Attribute
ms.assetid: 5486ed48-d28f-4bbb-b8ed-fc5a5aa12f25
ms.topic: article
ms.date: 05/31/2018
---

# VML Aspect Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies how the fill image aspect ratio will be preserved. Read/write. **String**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* aspect=" *expression* ">

**Script Syntax**

*element* .aspect="*expression*"

*expression*=*element*.aspect

**Remarks**

Values include:



| Value   | Description                           |
|---------|---------------------------------------|
| ignore  | Ignore aspect issues. Default.        |
| atleast | Image is at least as big as **Size**. |
| atmost  | Image is no bigger than **Size**.     |



 

*VML Standard Attribute*

**Example**

The image that makes up the fill is greater than or equal to a size of 10 points by 10 points.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:fill aspect="atleast" size="10pt,10pt" src="myimage.gif"/>
   </v:shape>
```



 

 