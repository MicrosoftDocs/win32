---
title: VML Inset Attribute
description: VML Inset Attribute
ms.assetid: b50f900a-b0dc-4042-af9e-050011307765
ms.topic: article
ms.date: 05/31/2018
---

# VML Inset Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Specifies inner margin values for textbox text. Read/write. **String**.

**Applies To**

[TextBox](msdn-online-vml-textbox-element.md)

**Tag Syntax**

<v: *element* inset=" *expression* ">

**Script Syntax**

*element* .inset="*expression*"

*expression*=*element*.inset

**Remarks**

The internal text margin value is specified as a string containing four values, each separated by commas or spaces. The values measure inset from the left, top, right, and bottom edges of the box specified by the [TextBoxRect](msdn-online-vml-textboxrect-attribute.md) attribute of **Path**. Missing values are set to the default, which is "0.1in, 0.05in, 0.1in, 0.05in".

For rotated shapes in browsers that do not support rotation, the bounding box will snap to the closest multiple of 90 degrees.

*VML Standard Attribute*

**Example**

The textbox will have an inset margin of 10 pixels.


```HTML
   <v:shape id="rect01"
   coordorigin="0 0" coordsize="200 200"
   strokecolor="red" fillcolor="red"
   style="top:10pt;left:10pt;width:50pt;height:50pt"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:textbox id="mytextbox" inset="10px, 10px, 10px, 10px">
   VML
   </v:textbox/>
   </v:shape>
```



 

 