---
title: VML ViewpointOrigin Attribute
description: VML ViewpointOrigin Attribute
ms.assetid: 4ccb3e12-bae4-4cb2-b48b-80c155ae7e03
ms.topic: article
ms.date: 05/31/2018
---

# VML ViewpointOrigin Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines the origin of the viewpoint within the bounding box of the shape. Read/write. **VgVector2D**.

**Applies To**

[Extrusion](msdn-online-vml-extrusion-element.md)

**Tag Syntax**

<o: *element* viewpointorigin=" *expression* ">

**Script Syntax**

*element* .viewpointorigin="*expression*"

*expression*=*element*.viewpointorigin

**Remarks**

Defines the viewpoint in terms of the x and y values of the original shape. The x and y values range from 0.5 to -0.5 (50% to -50% of the shape's coordinate origin). The default is 0,0.

*Microsoft Office Extensions Attribute*

 

 