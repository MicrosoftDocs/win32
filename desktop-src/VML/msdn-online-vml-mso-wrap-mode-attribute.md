---
title: VML MSO-Wrap-Mode Attribute
description: VML MSO-Wrap-Mode Attribute
ms.assetid: 51c4e90d-62cc-4646-9c71-8a6bf3366b2f
ms.topic: article
ms.date: 05/31/2018
---

# VML MSO-Wrap-Mode Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the wrapping mode for text. Read/write. **String**.

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* style="mso-wrap-mode: *expression* ">

**Remarks**

Values include:



| Value          | Description                          |
|----------------|--------------------------------------|
| square         | Wraps text around shape in a square. |
| tight          | Text is wrapped close to the shape.  |
| top-and-bottom | Text jumps from top to bottom.       |
| through        | Text displays through the shape.     |
| none           | Text doesn't wrap.                   |



 

Used by Microsoft PowerPoint for saving to HTML to indicate whether word wrap inside an AutoShape is on (**square**) or off (**none**).

*Microsoft Office Extensions Attribute*

**Example**

The following code indicates that wordwrap inside an AutoShape is turned on in PowerPoint.


```HTML
   <v:shape id="rect01"
   fillcolor="red" strokecolor="red"
   coordorigin="-500 -500" coordsize="1000 1000"
   style="position:relative;top:0;left:0;width:100pt;height:100pt;mso-wrap-mode:square"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   </v:shape>
```



 

 