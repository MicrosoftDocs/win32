---
title: Matrix Attribute (Shadow)(VML)
description: Matrix Attribute (Shadow)(VML)
ms.assetid: 29bebd2f-7f66-4883-8c12-57fef4a0ac9e
ms.topic: article
ms.date: 05/31/2018
---

# Matrix Attribute (Shadow)(VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines a perspective transform for a shadow. Read/write. **String**.

**Applies To**

[Shadow](msdn-online-vml-shadow-element.md)

**Tag Syntax**

<v: *element* matrix=" *expression* ">

**Script Syntax**

*element* .matrix="*expression*"

*expression*=*element*.matrix

**Remarks**

A perspective transform matrix in the form "sxx,sxy,syx,syy,px,py" where s= scale and p = perspective. If offset is in absolute units then px, py are in 1/emu units; otherwise they are an inverse fraction of the shape size.

*VML Standard Attribute*

 

 