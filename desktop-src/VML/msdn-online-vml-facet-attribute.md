---
title: VML Facet Attribute
description: VML Facet Attribute
ms.assetid: 6b874d79-a34e-45f7-bbbf-44d652410b1e
ms.topic: article
ms.date: 05/31/2018
---

# VML Facet Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the number of facets used to describe curved surfaces of an extrusion. Read/write. **VgNumber**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* facet=" *expression* ">

**Script Syntax**

*element* .facet="*expression*"

*expression*=*element*.facet

**Remarks**

Defines the way that a rendering engine will approximate the extrusion. A lower number will indicate a lower rendering tolerance to the rendering engine and will yield more facets. Higher numbers will make the extrusion appear more faceted. The default value is 30,000.

*Microsoft Office Extensions Attribute*

 

 