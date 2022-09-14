---
title: VML TextBox Element
description: VML TextBox Element
ms.assetid: 3573256e-f241-4de7-8541-252c92109af7
ms.topic: article
ms.date: 05/31/2018
---

# VML TextBox Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a text box for a shape.

The following attributes modify a text box.



| Attribute                                                                    | Description                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------|
| [Direction](msdn-online-vml-direction-attribute.md)                         | Defines the direction of the text.                         |
| [ID](id-attribute--textbox--vml.md)                                         | Defines a unique identifier for the textbox.               |
| [Inset](msdn-online-vml-inset-attribute.md)                                 | Specifies inner margin values for textbox text.            |
| [InsetMode](msdn-online-vml-insetmode-attribute.md)                         | Defines how an application will allow custom inset values. |
| [Layout-Flow](msdn-online-vml-layout-flow-attribute.md)                     | Determines the flow of the text in the textbox.            |
| [MSO-Direction-Alt](msdn-online-vml-mso-direction-alt-attribute.md)         | Defines alternate directions for text in textboxes.        |
| [MSO-Fit-Shape-To-Text](msdn-online-vml-mso-fit-shape-to-text-attribute.md) | Determines whether a shape will stretch to fit text.       |
| [MSO-Fit-Text-To-Shape](msdn-online-vml-mso-fit-text-to-shape-attribute.md) | Determines whether text will stretch to fit a shape.       |
| [MSO-Layout-Flow-Alt](msdn-online-vml-mso-layout-flow-alt-attribute.md)     | Defines the alternate layout flow for text in a textbox.   |
| [MSO-Next-Textbox](msdn-online-vml-mso-next-textbox-attribute.md)           | Specifies the next textbox in a series.                    |
| [MSO-Rotate](msdn-online-vml-mso-rotate-attribute.md)                       | Determines whether text rotates with a rotated shape.      |
| [MSO-Text-Scale](msdn-online-vml-mso-text-scale-attribute.md)               | Defines the scaling factor for fitting text to shapes.     |
| [SingleClick](msdn-online-vml-singleclick-attribute.md)                     | Determines whether text is selectable with a single click. |
| [V-Text-Anchor](msdn-online-vml-v-text-anchor-attribute.md)                 | Defines the vertical anchoring of text in a textbox.       |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

The following is the minimum code needed to produce a textbox.


```HTML
   <v:oval strokecolor="red" fillcolor="yellow
   style="position:relative;top:50;left:50;width:75;height:50">
   <v:textbox>VML</v:textbox>
   </v:oval>
```



Note that the text displayed in the textbox is enclosed by the TextBox tags. The text inside the tags can be modified by ordinary HTML tags.

**Example**

-   [Simple TextBox Example](/previous-versions/bb264075(v=vs.85))

 

 