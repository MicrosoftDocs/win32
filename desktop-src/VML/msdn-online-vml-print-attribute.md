---
title: VML Print Attribute
description: VML Print Attribute
ms.assetid: ef9f9f11-782a-40db-986c-946d9ee03071
ms.topic: article
ms.date: 05/31/2018
---

# VML Print Attribute

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Determines whether the shape will be printed. Read/write. [VgTriState](msdn-online-vml-vgtristate.md).

**Applies To**

[Shape](shape-element--vml.md)

**Tag Syntax**

<v: *element* print=" *expression* ">

**Script Syntax**

*element* .print="*expression*"

*expression*=*element*.print

**Remarks**

Provided as a way to specify whether shapes will be printed. Note that a shape can still be displayed on the screen, even if it is not printed as a result of this attribute being **False**. The default value is **True**.

This attribute is used by Microsoft Office but is not used by Microsoft Internet Explorer.

*Microsoft Office Extensions Attribute*

 

 