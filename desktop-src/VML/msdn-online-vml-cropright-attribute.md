---
title: VML CropRight Attribute
description: VML CropRight Attribute
ms.assetid: 1e2bd8e8-3d56-435d-bfaf-fb07f6b6fba6
ms.topic: article
ms.date: 05/31/2018
---

# VML CropRight Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the percentage of picture removal from the right side. Read/write. **VgNumber**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* cropright=" *expression* ">

**Script Syntax**

*element* .cropright="*expression*"

*expression*=*element*.cropright

**Remarks**

The amount of cropping can range from -1.0 to 1.0. The default value is 0. Note that a value of 1 will display no picture at all. Negative values will result in the picture being squeezed inward from the edge being cropped (the empty space between the picture and the cropped edge will be filled by the fill color of the shape). Positive values less than 1 will result in the remaining picture being stretched to fit the shape.

*VML Standard Attribute*

**Example**

The picture will be squeezed from the right side by 20% of the width. The empty space between the picture and the right edge will be filled by the fill color of the shape.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="blue"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata cropright="-.2" src="kids.jpg"/>
   </v:shape>
```





 

 