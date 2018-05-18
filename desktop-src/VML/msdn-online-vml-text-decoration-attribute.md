---
title: VML Text-Decoration Attribute
description: VML Text-Decoration Attribute
ms.assetid: 'a64985bd-d025-4e9c-bb4b-bf0450d5143a'
---

# VML Text-Decoration Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be [migrated to SVG](http://go.microsoft.com/fwlink/p/?LinkID=236964) or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](https://msdn.microsoft.com/library/hh772377). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](http://go.microsoft.com/fwlink/p/?linkid=204313).

 

Defines the style of text decoration. Read/write. **String**.

**Applies To**

[TextPath](msdn-online-vml-textpath-element.md)

**Tag Syntax**

&lt;v: *element* style="text-decoration: *expression* "&gt;

**Script Syntax**

*element* .style.textdecoration="*expression*"

*expression*=*element*.style.textdecoration

**Remarks**

Values include:

-   none (default)
-   underline
-   overline
-   line-through
-   blink

*VML Standard Attribute*

**Example**

The text will be underlined.


```HTML
   <v:line from="50 100" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="text-decoration:underline;font:normal normal normal 36pt Arial"/>
   </v:line>
```



 

 




