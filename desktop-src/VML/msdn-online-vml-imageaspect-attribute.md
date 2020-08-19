---
title: VML ImageAspect Attribute
description: VML ImageAspect Attribute
ms.assetid: 9ae58a76-f097-4feb-9008-ab6212bae8fb
ms.topic: article
ms.date: 05/31/2018
---

# VML ImageAspect Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines how the stroke image aspect ratio will be preserved. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v:

element *imageaspect="* expression *">*

**Script Syntax**

element *.imageaspect="*expression*"*

expression*=*element*.imageaspect*

**Remarks**

Values include:



| Value   | Description                                |
|---------|--------------------------------------------|
| Ignore  | Ignore aspect issues.                      |
| AtLeast | Image is at least as big as **ImageSize**. |
| AtMost  | Image is no bigger than **ImageSize**.     |



 

In each case, the **ImageSize** attribute will be adjusted to preserve the aspect of the image.

*VML Standard Attribute*

**Example**

The stroke image will be at least as big as the image size.


```HTML
   <v:shape id="rect01"
   strokecolor="red" fillcolor="red"
   style="top:20;left:20;width:30;height:30"
   path="m 1,1 l 1,200, 200,200, 200,1 x e">
   <v:stroke imageaspect="AtLeast"/>
   </v:shape>
```



 

 