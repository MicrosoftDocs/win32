---
title: VML Render Attribute
description: VML Render Attribute
ms.assetid: a05e7f6e-4784-4ff8-9deb-0501d3a5658e
ms.topic: article
ms.date: 05/31/2018
---

# VML Render Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the rendering mode of the extrusion. Read/write. **String**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* render=" *expression* ">

**Script Syntax**

*element* .render="*expression*"

*expression*=*element*.render

**Remarks**

Values include:



| Value        | Description                                                   |
|--------------|---------------------------------------------------------------|
| solid        | Rendering displays a solid shape. Default.                    |
| wireframe    | Rendering displays a wireframe shape.                         |
| boundingcube | Rendering displays the bounding cube that contains the shape. |



 

*Microsoft Office Extensions Attribute*

 

 