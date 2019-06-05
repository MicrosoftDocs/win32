---
title: ARIA Data Table Error
description: ARIA Data Table Error
ms.assetid: 3D0448BB-50DC-4C85-93BD-D8E626475AB0
keywords:
- AriaDataTableErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Data Table Error

## Text

Table contains data but doesn't have accessible markup defined though **aria-label**, **aria-labelledby**, **title**, **caption** or **th** elements.

## Type

Error

## Description

This error applies to HTML tables with more than one cell. This error does not apply to tables with `role="presentation"` because these are considered to be layout tables.

This error indicates that a data table doesn’t have an accessible name or header information.

To fix this error, define an accessible name by using the [**CAPTION**](https://msdn.microsoft.com/library/ms535213) tag, or the [**aria-labelledby**](https://msdn.microsoft.com/library/Cc848875), [**aria-label**](https://msdn.microsoft.com/library/Hh968243), or [**title**](https://msdn.microsoft.com/library/ms534683) attributes. If the table is missing header information, use [**THead**](https://msdn.microsoft.com/library/ms535909) tags to mark header cells.

## Example


```HTML
<!-- Data tables must contain an accessibile name and header information. -->
<table>
  <caption>ARIA Examples</caption>
  <thead>
    <tr>
      <th>Name</th>
      <th>Description</th>
      ...
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Accessible tables</td>
      <td>This example illustrates how to make data tables accessible using ARIA</td>
      ...
    </tr>
  </tbody>
</table>
```



 

 




