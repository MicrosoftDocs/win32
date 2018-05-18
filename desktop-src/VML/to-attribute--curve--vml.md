---
title: To Attribute (Curve)(VML)
description: To Attribute (Curve)(VML)
ms.assetid: '61469921-5095-4cb6-b032-f3e250874958'
---

# To Attribute (Curve)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the ending point of a curve. Read/write. **VgVector2D**.

**Applies To**

[Curve](msdn-online-vml-curve-element.md)

**Tag Syntax**

&lt;v: *element* to=" *expression* "&gt;

**Script Syntax**

*element* .to="*expression*"

*expression*=*element*.to

**Remarks**

Defines the ending point of a cubic bezier curve in the coordinate space of the parent element. If the parent is not a VML element, the default [unit](msdn-online-vml-units.md) is a pixel (but in, cm, mm, pt, pc may also be specified). Default is 30,20.

**VML Standard Attribute**

**Example**

The curve is smiling. It starts at the left and ends at the right. The two control points are situated along the way so as to pull the curve down to give the appearance of a smile.


```HTML
   <v:curve id="mycurve"
   from="10pt,10pt" to="100pt,10pt"
   control1="40pt,30pt" control2="70pt,30pt">
   </v:curve>
```



 

 




