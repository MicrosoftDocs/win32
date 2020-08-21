---
title: VML CropTop Attribute
description: VML CropTop Attribute
ms.assetid: b54939b6-0505-43b0-bf82-c3df82dc2633
ms.topic: article
ms.date: 05/31/2018
---

# VML CropTop Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the percentage of picture removal from the top side. Read/write. **VgNumber**.

**Applies To**

[ImageData](msdn-online-vml-imagedata-element.md)

**Tag Syntax**

<v: *element* croptop=" *expression* ">

**Script Syntax**

*element* .croptop="*expression*"

*expression*=*element*.croptop

**Remarks**

The amount of cropping can range from -1.0 to 1.0. The default value is 0. Note that a value of 1 will display no picture at all. Negative values will result in the picture being squeezed inward from the edge being cropped (the empty space between the picture and the cropped edge will be filled by the fill color of the shape). Positive values less than 1 will result in the remaining picture being stretched to fit the shape.

*VML Standard Attribute*

**Example**

The picture will be squeezed into a narrow sliver at the bottom of the shape.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:300;height:200"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:imagedata croptop="-.8" src="kids.jpg"/>
   </v:shape>
```





 

 