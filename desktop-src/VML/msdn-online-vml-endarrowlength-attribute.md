---
title: VML EndArrowLength Attribute
description: VML EndArrowLength Attribute
ms.assetid: 'aab898b6-4c59-4471-81fd-621f79610d63'
---

# VML EndArrowLength Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines an arrowhead length for the end of a line. Read/write. **VgArrowheadLength**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

&lt;v: *element* endarrowlength=" *expression* "&gt;

**Script Syntax**

*element* .endarrowlength="*expression*"

*expression*=*element*.endarrowlength

**Remarks**

Values include:

-   Short
-   Medium (default)
-   Long

*VML Standard Attribute*

**Example**

A line is drawn with a short classic arrowhead on the end of the stroke.


```HTML
   <v:line strokecolor="red"
   strokeweight="2pt" to="100pt,20pt" from="20pt,20pt">
   <v:stroke endarrow="classic" endarrowlength="short"/>
   </v:line>
```



 

 




