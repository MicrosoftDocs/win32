---
description: Overview of using active accessibility to expose text.
ms.assetid: c04ade90-5f17-4e16-b82b-c99230000954
title: Using Active Accessibility to Expose Text
ms.topic: article
ms.date: 05/31/2018
---

# Using Active Accessibility to Expose Text

Applications can use Microsoft Active Accessibility to expose text. However, the [**IAccessible**](/windows/win32/api/oleacc/nn-oleacc-iaccessible) interface defined by earlier versions of Active Accessibility is not optimized for exposing large amounts of rich text. Later versions define interfaces that are optimized for exposing large amounts of text and textual attributes.

To expose large amounts text, create separate Component Object Model (COM) objects that support [**IAccessible**](/windows/win32/api/oleacc/nn-oleacc-iaccessible), or child elements, to represent each run of text. A run is a line, or portion of a line, that shares the same formatting.

Active Accessibility exposes only the text and its location, but has no mechanism for exposing the formatting of the text. Despite these limitations, some programs use Active Accessibility to expose text. For example, Microsoft Internet Explorer and Microsoft Visual Studio both use Active Accessibility to expose large amounts of text.

For more information about exposing text by using Active Accessibility, see [Accessibility](../accessibility/accessibility.md).

 

 
