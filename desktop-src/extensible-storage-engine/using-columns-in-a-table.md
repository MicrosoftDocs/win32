---
description: "Learn more about: Using Columns in a Table"
title: Using Columns in a Table
TOCTitle: Using Columns in a Table
ms:assetid: 064ac59e-d306-4335-a623-754a003f5ebc
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269178(v=EXCHG.10)
ms:contentKeyID: 32765481
ms.date: 04/11/2016
ms.topic: article
---

# Using Columns in a Table


_**Applies to:** Windows | Windows Server_

## Using Columns in a Table

A table can be created with an initial set of columns by calling [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md) or without columns by calling [JetCreateTable](./jetcreatetable-function.md). When the table is created with an initial set of columns in the call to [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md) or [JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md), it contains a [JET_TABLECREATE](./jet-tablecreate-structure.md) (or [JET_TABLECREATE2](./jet-tablecreate2-structure.md)) structure. These structures contain an array of [JET_COLUMNCREATE](./jet-columncreate-structure.md) structures that define the set of columns in the table. The **grbit** member sets the options on the column and the **coltyp** member sets the type of data that can be set in the column.

When the table is created without columns, they must be added by calling [JetAddColumn](./jetaddcolumn-function.md) with the [JET_COLUMNDEF](./jet-columndef-structure.md) structure. The **grbit** member of the [JET_COLUMNDEF](./jet-columndef-structure.md) structure sets the options on the column and the **coltyp** member sets the type of data that can be set in the column. Default column values are set in the call to [JetAddColumn](./jetaddcolumn-function.md) by specifying a value in the *pvDefault* parameter and the size in the *cbDefault* parameter. A column without a default value effectively has a default value of NULL.

The values in the table can only be set within the context of a transaction. The transaction begins in the call to [JetBeginTransaction](./jetbegintransaction-function.md) and ends in the call to [JetCommitTransaction](./jetcommittransaction-function.md). Inside the transaction, a single column value can be set by calling [JetSetColumn](./jetsetcolumn-function.md), or multiple columns values can be set by calling [JetSetColumns](./jetsetcolumns-function.md). [JetSetColumns](./jetsetcolumns-function.md) uses an array of [JET_SETCOLUMN](./jet-setcolumn-structure.md) structures to set multiple columns in the table. The data is contained in the *pvData* parameter of [JetSetColumn](./jetsetcolumn-function.md), or the **pvData** member in [JET_SETCOLUMN](./jet-setcolumn-structure.md) structure.

The [JET_COLUMNBASE](./jet-columnbase-structure.md), [JET_COLUMNLIST](./jet-columnlist-structure.md), and [JET_COLUMNDEF](./jet-columndef-structure.md) structures are returned in the calls to [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md), and [JetGetColumnInfo](./jetgetcolumninfo-function.md) depending on the type of column that is retrieved. The [JET_COLUMNBASE](./jet-columnbase-structure.md) structure describes the parameters of the base column, and the [JET_COLUMNLIST](./jet-columnlist-structure.md) contains the information needed to traverse the temporary table that is created by the [JetGetColumnInfo](./jetgetcolumninfo-function.md) and [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) functions.
