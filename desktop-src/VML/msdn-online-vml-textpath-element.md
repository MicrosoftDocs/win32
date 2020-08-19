---
title: VML TextPath Element
description: VML TextPath Element
ms.assetid: dcc3b723-4c5c-4069-93c7-c41737292109
ms.topic: article
ms.date: 05/31/2018
---

# VML TextPath Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a text path for a shape.

The following attributes modify a text path.



| Attribute                                                                    | Description                                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [FitPath](msdn-online-vml-fitpath-attribute.md)                             | Defines whether the text fits the path of a shape.                             |
| [FitShape](msdn-online-vml-fitshape-attribute.md)                           | Defines whether the text fits the shape boundaries.                            |
| [Font-Family](msdn-online-vml-font-family-attribute.md)                     | Specifies the font-family of text.                                             |
| [Font-Size](msdn-online-vml-font-size-attribute.md)                         | Specifies the font-size of text.                                               |
| [Font-Style](msdn-online-vml-font-style-attribute.md)                       | Specifies the font-style of text.                                              |
| [Font-Variant](msdn-online-vml-font-variant-attribute.md)                   | Specifies the font-variant of text.                                            |
| [Font-Weight](msdn-online-vml-font-weight-attribute.md)                     | Specifies the font-weight of text.                                             |
| [Font](msdn-online-vml-font-attribute.md)                                   | Specifies the compound font value of text.                                     |
| [MSO-Text-Shadow](msdn-online-vml-mso-text-shadow-attribute.md)             | Defines whether a shadow is applied to the text.                               |
| [On](on-attribute--textpath--vml.md)                                        | Defines whether the text is displayed.                                         |
| [String](msdn-online-vml-string-attribute.md)                               | Defines the text string.                                                       |
| [Text-Decoration](msdn-online-vml-text-decoration-attribute.md)             | Defines the text-decoration of the text.                                       |
| [Trim](msdn-online-vml-trim-attribute.md)                                   | Defines whether extra space is removed above and below the text.               |
| [V-Rotate-Letters](msdn-online-vml-v-rotate-letters-attribute.md)           | Determines whether the letters of the text are rotated.                        |
| [V-Same-Letter-Heights](msdn-online-vml-v-same-letter-heights-attribute.md) | Determines whether all letters will have the same height.                      |
| [V-Text-Align](msdn-online-vml-v-text-align-attribute.md)                   | Defines the alignment of the text.                                             |
| [V-Text-Kern](msdn-online-vml-v-text-kern-attribute.md)                     | Determines whether kerning is turned on.                                       |
| [V-Text-Reverse](msdn-online-vml-v-text-reverse-attribute.md)               | Determines whether the layout order of rows is reversed.                       |
| [V-Text-Spacing-Mode](msdn-online-vml-v-text-spacing-mode-attribute.md)     | Defines the mode for letterspacing.                                            |
| [V-Text-Spacing](msdn-online-vml-v-text-spacing-attribute.md)               | Defines the amount of spacing for text.                                        |
| [XScale](msdn-online-vml-xscale-attribute.md)                               | Determines whether a straight textpath will be used instead of the shape path. |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

In addition to the normal fill, string, and style attributes, the [TextPathOK](msdn-online-vml-textpathok-attribute.md) attribute of [Path](msdn-online-vml-path-element.md) must be set to **True** and the [On](on-attribute--textpath--vml.md) attribute of TextPath must be set to **True** to display text on a text path.

The following is the minimum code needed to display text on a path.


```HTML
   <v:line from="50 200" to="400 100">
   <v:fill on="True" color="red"/>
   <v:path textpathok="True"/>
   <v:textpath on="True" string="VML Text"
   style="font:normal normal normal 36pt Arial"/>
   </v:line>
```



**Examples**

-   [Simple TextPath Example](/previous-versions/bb264038(v=vs.85))
-   [Dynamic TextPath Typeface Example](/previous-versions/bb264042(v=vs.85))
-   [Dynamic TextPath Curve Example](/previous-versions/bb264041(v=vs.85))

 

 