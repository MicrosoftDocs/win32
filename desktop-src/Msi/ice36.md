---
description: ICE36 validates that every icon in the Icon table is listed at least once in the ARPPRODUCTICON property or the Class, ProgId, or Shortcut tables.
ms.assetid: d502c0a9-17e5-467a-8b02-8b254e77b96b
title: ICE36
ms.topic: article
ms.date: 05/31/2018
---

# ICE36

ICE36 validates that every icon in the Icon table is listed at least once in the [**ARPPRODUCTICON**](arpproducticon.md) property or the [Class](class-table.md), [ProgId](progid-table.md), or [Shortcut](shortcut-table.md) tables.

During advertisement, the installer installs all the icons listed in the [Icon table](icon-table.md) on the user's computer. Having unused icons in the Icon table does not prevent the installation from running, however it does unnecessarily increase the size of the .msi file and the time and space required to advertise a feature.

If an icon is not referenced in the property or table and there is no UI provided to create a reference at run time, you should remove the icon to achieve better performance.

## Result

ICE36 posts a message if there is a icon in the Icon table that is not referenced in the [Class](class-table.md), [ProgId](progid-table.md), or [Shortcut](shortcut-table.md) tables and if there is no UI provided to create such a reference at run time.

## Example

ICE36 reports the following error for the example shown.

``` syntax
Icon Bloat. Icon Icon4 is not used in the Class, Shortcut, or ProgID table. This adversely affects performance.
```

[Icon Table](icon-table.md) (partial)



| Name  | Data     |
|-------|----------|
| Icon1 | Control1 |
| Icon2 | Control2 |
| Icon3 | Control3 |
| Icon4 | Control4 |



 

[ProgID Table](progid-table.md) (partial)



| ProgID    |
|-----------|
| Property1 |



 

[Class Table](class-table.md) (partial)



| CLSID                                  |
|----------------------------------------|
| {3E469ABA-3644-11d2-8892-00A0C981B015} |



 

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Icon\_ |
|-----------|--------|
| Shortcut1 | Icon2  |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



