---
description: ICE58 checks that your Media table does not have more than 80 rows.
ms.assetid: 693b195e-1e69-4895-87dd-59714646cff9
title: ICE58
ms.topic: article
ms.date: 05/31/2018
---

# ICE58

ICE58 checks that your [Media table](media-table.md) does not have more than 80 rows.

## Result

Warnings reported by ICE58 cause the installation to fail unless the package is installed with Windows Installer 2.0 or later. Beginning with Windows Installer 2.0, the restriction to more than 80 media table entries is removed. No warning is issued if the package's [**Page Count Summary**](page-count-summary.md) Property is greater than or equal to 150. Packages of schema 200 or higher can only be installed by Windows Installer 2.0 or later.

## Example

ICE58 reports the following errors and warnings for the example shown.

``` syntax
This package has 81 media entries. Packages are limited to 80 entries in the media table.
```

To fix this error, eliminate any unused media table entries, consolidate media table entries that refer to the same media, and repackage your application to reduce the media required.

[Media Table](media-table.md) (partial)



| DiskId | LastSequence\_ |
|--------|----------------|
| 1      | 10             |
| 2      | 20             |
| ...    | ...            |
| 81     | 810            |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



