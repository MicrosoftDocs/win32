---
title: Ext Attribute (Skew)(VML)
description: Ext Attribute (Skew)(VML)
ms.assetid: ff1dfb2f-9098-4418-a2f7-c7159328bd09
ms.topic: article
ms.date: 05/31/2018
---

# Ext Attribute (Skew)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the way a skew is displayed. Read/write. **String**.

**Applies To**

[Skew](msdn-online-vml-skew-element.md)

**Tag Syntax**

<o: *element* v:ext=" *expression* ">

**Script Syntax**

*element* .ext="*expression*"

*expression*=*element*.ext

**Remarks**

This attribute is used to tell graphical editors how to process the **Skew** element. Values include:

-   **edit**
-   **view** (default)
-   **backwardCompatible**

If an extension is set to **edit**, it can be ignored by a software viewer. If set to **view**, the viewer must render the bitmap representation instead.

*Microsoft Office Extensions Attribute*

 

 