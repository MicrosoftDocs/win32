---
description: "Learn more about: Multi-Valued Sparse Columns"
title: Multi-Valued Sparse Columns
TOCTitle: Multi-Valued Sparse Columns
ms:assetid: 36e82a73-aad4-4e0d-a743-a2182c41fe9c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269225(v=EXCHG.10)
ms:contentKeyID: 32765527
ms.date: 04/11/2016
ms.topic: article
---

# Multi-Valued Sparse Columns


_**Applies to:** Windows | Windows Server_

## Multi-Valued Sparse Columns

Sparse columns may be fixed or variable length, and are unique in that they do not take up space in a record if they are NULL or left to their default value. Sparse columns, also referred to as tagged columns, can contain more than one value in a single record. Tagged columns can be any of the columns types described in the [JET_coltyp](./jet-coltyp.md) constants. They are created when the column is added to the table by setting the JET_bitColumnTagged flag in the [JET_COLUMNDEF](./jet-columndef-structure.md) structure in the call to [JetAddColumn](./jetaddcolumn-function.md), or in the [JET_COLUMNCREATE](./jet-columncreate-structure.md) structure used in the call to [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md) or [JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md). Columns of type JET_coltypLongText and JET_coltypLongBinary are automatically created as tagged columns.

Only tagged columns can contain multiple values in a record, fixed or variable length columns may not contain multiple values. There are two types of multi-valued columns:

  - Tagged columns are multi-valued by default. When a second value is added to the column, it automatically becomes multi-valued.

  - Tagged columns that are created with the JET_bitColumnMultiValued option in the [JET_COLUMNDEF](./jet-columndef-structure.md) structure in the call to [JetAddColumn](./jetaddcolumn-function.md).

The JET_bitColumnMultiValued option changes the way that the column is indexed. Multi-valued columns with the JET_bitColumnMultiValued option are indexed more extensively than tagged multi-valued columns. These columns are indexed over all values in the multi-valued column, whereas tagged multi-valued columns are only indexed over the first value in the multi-valued column. For example, consider a multi-valued column where the JET_bitColumnMultiValued option is set and it is the first multi-valued column in an index. This column contains three values: A, B, and C. An index over this column contains entries for all three values, A, B, and C. If the JET_bitColumnMultiValued option was not set, the index over this column only contains the first value, A, in the index.
