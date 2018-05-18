---
title: VML EndCap Attribute
description: VML EndCap Attribute
ms.assetid: 'd8669a34-0fec-461e-90de-d9d5f7749a15'
---

# VML EndCap Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the cap style for the end of a stroke. Read/write. **VgLineEndCapStyle**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

&lt;v: *element* endcap=" *expression* "&gt;

**Script Syntax**

*element* .endcap="*expression*"

*expression*=*element*.endcap

**Remarks**

Values include:

-   Flat (default)
-   Square
-   Round

*VML Standard Attribute*

**Example**

A line is drawn with a flat cap on the end of the stroke.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke endcap="flat"/>
   </v:line>
```



 

 




