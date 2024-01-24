---
description: ICE32 validates that keys and foreign keys in the .msi file are of the same size and column definition types.
ms.assetid: cc488ec5-e17a-4829-9763-38ba3c33bfde
title: ICE32
ms.topic: article
ms.date: 05/31/2018
---

# ICE32

ICE32 validates that keys and foreign keys in the .msi file are of the same size and column definition types. This ICE custom action makes the comparison using the [\_Validation table](-validation-table.md) and using the definition types that are returned by [**MsiViewGetColumnInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewgetcolumninfo). For more information, see [Column Definition Format](column-definition-format.md).

## Result

ICE32 posts errors if the .msi file contains any foreign keys to keys of a different column length or column data type.

## Example

ICE32 posts two errors for the example shown:

-   There is a foreign key and key defined that differ in size.
-   There is a foreign key and key defined that differ in their definition type.

[\_Validation Table](-validation-table.md) (partial)



| Table | Column  | KeyTable | KeyColumn |
|-------|---------|----------|-----------|
| File  | Version | File     | 1         |
| Flap  | Column8 | Flap     | 1         |



 

Column Definitions (partial)



| Table | Column  | Type | Size |
|-------|---------|------|------|
| File  | File    | s    | 72   |
| File  | Version | S    | 32   |
| Flap  | Column1 | i    | 2    |
| Flap  | Column8 | S    | 32   |



 

The Version column of the File table can be a foreign key to another file in the File table. This occurs with companion files. However, the Version column only allows a string length 32, whereas the File column allows a string length 72. To fix this error change the string lengths to match.

There is a foreign key and key defined that differ in their definition types. Column8 of the Flap Table is listed as a foreign key to Column1. Column8 is a string column and Column1 is an integer column. The foreign key and key pairs must be defined so that their data types match.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



