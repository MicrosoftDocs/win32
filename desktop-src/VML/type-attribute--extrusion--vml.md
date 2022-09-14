---
title: Type Attribute (Extrusion)(VML)
description: Type Attribute (Extrusion)(VML)
ms.assetid: 2c7ad2f1-fb5d-49fb-b490-3efe59ee5177
ms.topic: article
ms.date: 05/31/2018
---

# Type Attribute (Extrusion)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the way that the shape is extruded. Read/write. **String**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* type=" *expression* ">

**Script Syntax**

*element* .type="*expression*"

*expression*=*element*.type

**Remarks**

Values include:



| Value       | Description                                                                                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| parallel    | Extrusion is rendered so that the center of projection is infinitely far away; that is, the extrusion lines do not converge (unlike perspective projections). Default. |
| perspective | Extrusion is rendered to a center of projection, which is the same as the vanishing point for unrotated objects.                                                       |



 

**Microsoft Office Extensions Attribute**

 

 