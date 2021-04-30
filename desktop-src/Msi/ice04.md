---
description: ICE04 validates that the sequence number of every file in the File table is less than or equal to the largest sequence number in the LastSequence column of the Media table.
ms.assetid: ecde1389-50ea-479e-bbc1-a36ce3aceccd
title: ICE04
ms.topic: article
ms.date: 05/31/2018
---

# ICE04

ICE04 validates that the sequence number of every file in the [File table](file-table.md) is less than or equal to the largest sequence number in the LastSequence column of the [Media table](media-table.md).

Each record in the Media table represents a disk on the source media containing all the files with a sequence number less than or equal to the value in the LastSequence column and greater than the LastSequence value in the record of the preceding disk.

## Result

ICE04 posts an error message if there is a file with a sequence number greater than the largest LastSequence number for the source media.

## Example

ICE04 would report the following error for the example shown:

``` syntax
File: MyFile, Sequence: 210 Greater Than Max Allowed by Media Table.
```

[File Table](file-table.md) (partial)



| File   | Sequence |
|--------|----------|
| MyFile | 210      |



 

[Media Table](media-table.md) (partial)



| DiskId | LastSequence |
|--------|--------------|
| 1      | 100          |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



