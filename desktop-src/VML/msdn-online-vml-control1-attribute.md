---
title: VML Control1 Attribute
description: VML Control1 Attribute
ms.assetid: 4a304936-4da8-4197-b7f3-d89551de0c85
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VML Control1 Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the first control point of a bezier curve. Read/write. **VgVector2D**.

**Applies To**

[Curve](msdn-online-vml-curve-element.md)

**Tag Syntax**

&lt;v: *element* control1=" *expression* "&gt;

**Script Syntax**

*element* .control1="*expression*"

*expression*=*element*.control1

**Remarks**

Defines the first control point of a cubic bezier curve in the coordinate space of the parent element.If the parent is not a VML element, the default [unit](msdn-online-vml-units.md) is a pixel (but in, cm, mm, pt, pc may also be specified). Default is 10,10.

*VML Standard Attribute*

**Example**

The curve is smiling. It starts at the left and ends at the right. The two control points are situated along the way so as to pull the curve down to give the appearance of a smile.


```HTML
   <v:curve id="mycurve"
   from="10pt,10pt" to="100pt,10pt"
   control1="40pt,10pt" control2="70pt,10pt">
   </v:curve>
```



[Show Me](http://samples.msdn.microsoft.com/workshop/samples/vml/shape/predef/t_curve.md)

 

 




