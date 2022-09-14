---
title: Title Attribute (Stroke)(VML)
description: Title Attribute (Stroke)(VML)
ms.assetid: 47cdec4a-9b35-47d7-a44d-e128c6c8a812
ms.topic: article
ms.date: 05/31/2018
---

# Title Attribute (Stroke)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the title of a stroke image. Read/write. **String**.

**Applies To**

[Stroke](msdn-online-vml-stroke-element.md)

**Tag Syntax**

<v: *element* title=" *expression* ">

**Script Syntax**

*element* .title="*expression*"

*expression*=*element*.title

**Remarks**

If this attribute has a value, then the stroke image is *embedded*. The actual value of the attribute is the text to be displayed with the picture when the mouse pointer moves over the image.

If the **HRef** tag is used, then **Title** is ignored.

This attribute is used by Microsoft Office but is not used by Microsoft Internet Explorer.

**Microsoft Office Extensions Attribute**

 

 