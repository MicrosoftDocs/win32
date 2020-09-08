---
title: ARIA Grid Structure Error
description: ARIA Grid Structure Error
ms.assetid: 8B2AEC98-1056-4560-AD6E-C6ECA0B94692
keywords:
- AriaGridStructureErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Grid Structure Error

## Text

Element with the **grid** role doesn't have a corresponding grid structure or accessible markup.

## Type

Error

## Description

This error applies to custom elements that have the **role** attribute set to "grid". It does not apply to HTML table tags that have an implicit **role** of "grid".

An element that has its **role** attribute set to "grid" must have the structure defined by the Web Accessibility Initiative - Accessible Rich Internet Applications (WAI-ARIA) grid role, including the accessible name for the grid and its header subelements.

To fix this error, review your implementation to ensure that it complies with the WAI-ARIA specification. Specifically, ensure that the structure meets the following rules.

-   **grid** contains **row** or **rowgroup** elements.
-   **rowgroup** contains **row** elements.
-   **row** elements contain **columnheader** or **gridcell** or **rowheader** elements.

An accessible name should be defined for **grid**, **columnheader**, **gridcell** and **rowheader** elements by using one of the following attributes.

-   [**aria-labelledby**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attribute for referencing the element containing text.
-   [**aria-label**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attribute to set the accessible name directly.
-   [**title**](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/title) for creating a tooltip which is at the same time used as a name.

 

 




