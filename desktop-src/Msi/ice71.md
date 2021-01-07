---
description: ICE71 verifies that the Media table contains an entry with DiskId equal to 1.
ms.assetid: b48c2f3f-24ef-48a8-849f-7abed69c0fc9
title: ICE71
ms.topic: article
ms.date: 05/31/2018
---

# ICE71

ICE71 verifies that the [Media table](media-table.md) contains an entry with DiskId equal to 1. (Windows Installer assumes that the .msi package is on disk 1.)

## Result

ICE71 returns an error if the Media table does not contain an entry with DiskId equal to 1.

## Example

ICE71 reports the following error for the example shown.

``` syntax
The Media table requires an entry with DiskId=1. First DiskId is '2'.
```

T0 fix this error, change the DiskId of the entry where the package is stored to 1.

[Media Table](media-table.md) (partial)



| DiskId |
|--------|
| 2      |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



