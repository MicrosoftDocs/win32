---
title: Matrix Attribute (Skew)(VML)
description: Matrix Attribute (Skew)(VML)
ms.assetid: 8d039865-2261-458b-8edf-01374af65cea
ms.topic: article
ms.date: 05/31/2018
---

# Matrix Attribute (Skew)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a perspective transform of a skew. Read/write. **String**.

**Applies To**

[Skew](msdn-online-vml-skew-element.md)

**Tag Syntax**

<o: *element* matrix=" *expression* ">

**Script Syntax**

*element* .matrix="*expression*"

*expression*=*element*.matrix

**Remarks**

The matrix is a string in the form "sxx, sxy, syx, syy, px, py" where s is scale, p is perspective, and x and y are x and y values. If [Offset](offset-attribute--skew--vml.md) is in absolute units, then px and py are in emu^-1 [units](msdn-online-vml-units.md) (otherwise they are an inverse fraction of the shape size). The default value is "1,0,0,1,0,0".

*Microsoft Office Extensions Attribute*

 

 