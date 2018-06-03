---
title: ARIA Presentation Table Error
description: ARIA Presentation Table Error
ms.assetid: 3D5AE911-78E5-4C40-B77B-604E65839F63
keywords:
- AriaLayoutTableErrorId
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Presentation Table Error

## Text

Table used for layout must not have header, accessible name or summary information defined (**th**, **summary**, **aria-describedby**, **aria-labelledby**, **aria-label**, **title**, **caption** attributes).

## Type

Error

## Description

This error applies to HTML table tags that have the [**role**](https://msdn.microsoft.com/library/windows/apps/hh780024) attribute set to "presentation", or with a table that has a single cell (1×1 table).

This error indicates that a table is marked as layout only (has `role="presentation"`), but it also contains accessibility information as if it was a data table, which can be confusing for screen reader users.

To address this error, determine whether the table actually is just a layout table and, if so, remove the accessible markup:

-   [**CAPTION**](https://msdn.microsoft.com/library/windows/apps/hh453023) element, [**aria-labelledby**](https://msdn.microsoft.com/library/windows/apps/hh465708), [**aria-label**](https://msdn.microsoft.com/library/windows/apps/hh968005), or [**title**](https://msdn.microsoft.com/library/windows/apps/hh780173) attributes.
-   [**summary**](https://www.bing.com/search?q=**summary**) or [**aria-describedby**](https://msdn.microsoft.com/library/windows/apps/hh465698) attributes.
-   [**THEAD**](https://msdn.microsoft.com/library/windows/apps/hh466200) tags.

## Example

![html for a table element, with attributes such as summary that trigger the aria presentation table error shown as struck-out html markup ](images/aria-layout-table.png)

## Remarks

If you determine that a table does need accessibility information, remove the [**role**](https://msdn.microsoft.com/library/windows/apps/hh780024) attribute or set it to a value other than "presentation".

 

 




