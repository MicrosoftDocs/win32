---
title: VML Introduction
description: VML Introduction
ms.assetid: 8b603e95-3f02-47d6-9c5c-c781fa5d8459
keywords:
- Vector Markup Language (VML),reference
- VML (Vector Markup Language),reference
- vector graphics,VML reference
- vector graphics,Vector Markup Language (VML)
- reference for Vector Markup Language (VML)
- VML reference
- Vector Markup Language (VML),Shape element
- VML (Vector Markup Language),Shape element
- vector graphics,Shape element
- Shape element
- VML elements,Shape
- Vector Markup Language (VML),VBScript
- VML (Vector Markup Language),VBScript
- Vector Markup Language (VML),Javascript
- VML (Vector Markup Language),Javascript
ms.topic: article
ms.date: 05/31/2018
---

# VML Introduction

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

This document gives a complete detailed reference to the implementation of the Vector Markup Language (VML) that is shipped with Microsoft Office 2000. Other implementations may vary. Consult the [VML specification](https://www.w3.org/TR/NOTE-datetime.html) for more information about VML as a standard.

VML is defined as a set of XML elements and the corresponding attributes for each element. Since the **Shape** element is the basic building block of VML, click [here](shape-element--vml.md) to begin the reference.

Note that this reference contains several examples and demos. You must have Microsoft Internet Explorer 5.0 or greater installed to view the live VML.

In addition to the information about using elements and attributes as XML tags that extend HTML, this reference contains syntax and examples that show how to use the scripting and the Document Object Model features of Internet Explorer 5 or greater. Using script with VML enables you to create elements "on the fly" and manipulate attributes in real time.

This examples in this reference uses VBScript and Javascript. If you use use a different scripting language than the one shown in an example, you must match the case of all element and attribute names. The reference gives scripting syntax that is correct for case-sensitive languages such as JavaScript. If in doubt regarding the correct character case, use an object browser (such as OLEView) to explore the VGX.DLL to determine the exact case of an element or attribute. Note that when VML is used as XML tags, case sensitivity depends on the document type of you underlying document. If you are using a strict mode !DOCTYPE, elements and attributes will be case sensitive.

[The VML Reference](shape-element--vml.md)

 

 