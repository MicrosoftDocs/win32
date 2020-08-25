---
title: Ext Attribute (Extrusion)(VML)
description: Ext Attribute (Extrusion)(VML)
ms.assetid: 5c7b2137-ddb6-422c-a202-6de494dc993f
ms.topic: article
ms.date: 05/31/2018
---

# Ext Attribute (Extrusion)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the default extrusion behavior for graphical editors. Read/write. **String**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* v:ext=" *expression* ">

**Script Syntax**

*element* .ext="*expression*"

*expression*=*element*.ext

**Remarks**

Instructs a graphical editor to render the element. If it can't render the element, the bitmap representation should be used instead. The default value is **view**.

*VML Standard Attribute*

 

 