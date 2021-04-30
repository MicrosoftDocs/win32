---
description: ICEM07 verifies that the order of files in the sequence table matches the order of files in MergeModule.CABinet.
ms.assetid: 5778e0c5-2f8d-4562-9c93-d6f6890a74e9
title: ICEM07
ms.topic: article
ms.date: 05/31/2018
---

# ICEM07

ICEM07 verifies that the order of files in the sequence table matches the order of files in [MergeModule.CABinet](mergemodule-cabinet.md).

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM07 posts an error if the order of files in the File table does not match the order in the cabinet file.

## Example

IC0M07 would post the following error message for the example shown.

``` syntax
The file 'FileB.GUID1' appears to be out of sequence. It has position 3 
in the CAB, but not when the file table is ordered by sequence number.
```

[File Table](file-table.md)



| File          | Sequence |
|---------------|----------|
| FileA.*GUID1* | 1        |
| FileB.*GUID1* | 8        |
| FileC.*GUID1* | 52       |



 

Embedded [MergeModule.CABinet](mergemodule-cabinet.md)



| File          |
|---------------|
| FileA.*GUID1* |
| FileC.*GUID1* |
| FileD.*GUID1* |
| FileB.*GUID1* |



 

Although the file sequence numbers in the file table do not have to be consecutive, and extra files can exist in the cabinet file, the relative sequence of all files in the File table must match the order in [MergeModule.CABinet](mergemodule-cabinet.md). To fix this error, change the sequence number of FileB to come after FileC to match the file order in the CAB, or rebuild the CAB with the files in the correct order.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



