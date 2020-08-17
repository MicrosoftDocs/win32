---
title: VML FocusSize Attribute
description: VML FocusSize Attribute
ms.assetid: 6ca5af2c-3064-423f-a7bb-202f23bf95da
ms.topic: article
ms.date: 05/31/2018
---

# VML FocusSize Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the focus size for radial fills. Read/write. **VgVector2D**.

**Applies To**

[Fill](msdn-online-vml-fill-element.md)

**Tag Syntax**

<v: *element* focussize=" *expression* ">

**Script Syntax**

*element* .focussize="*expression*"

*expression*=*element*.focussize

**Remarks**

The values are fractions of the width and height of the shape. The first is a percentage of the fill to the right edge of the shape and the second is a percentage of the fill to the bottom of the shape. The default value is 0,0. A **FocusSize** value of 100%,100% and a **FocusPosition** of 0,0 would make Color2 dominate the blend completely. Small values of around 10%,10% are recommended for balanced blends.

*VML Standard Attribute*

**Example**

The radial fill will create a blend starting in the center as blue and becoming red on all four edges. The center of the blend is defined by **FocusPosition** and the size of the inner starting color is determined by **FocusSize**.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red"
   style="top:1;left:1;width:50;height:50"
   path="m 1,1 l1,200, 200,200, 200,1 x e">
   <v:fill type="gradientradial" color="red" color2="blue"
   focusposition=".5,.5" focussize=".1,.1"/>
   </v:shape>
```



 

 