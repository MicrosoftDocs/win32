---
title: Using Columns in a Table
TOCTitle: Using Columns in a Table
ms:assetid: 064ac59e-d306-4335-a623-754a003f5ebc
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269178(v=EXCHG.10)
ms:contentKeyID: 32765481
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
---

# Using Columns in a Table


_**Applies to:** Windows | Windows Server_

## Using Columns in a Table

A table can be created with an initial set of columns by calling [JetCreateTableColumnIndex](gg269343\(v=exchg.10\).md) or without columns by calling [JetCreateTable](gg269210\(v=exchg.10\).md). When the table is created with an initial set of columns in the call to [JetCreateTableColumnIndex](gg269343\(v=exchg.10\).md) or [JetCreateTableColumnIndex2](gg294057\(v=exchg.10\).md), it contains a [JET\_TABLECREATE](gg294146\(v=exchg.10\).md) (or [JET\_TABLECREATE2](gg269203\(v=exchg.10\).md)) structure. These structures contain an array of [JET\_COLUMNCREATE](gg269252\(v=exchg.10\).md) structures that define the set of columns in the table. The **grbit** member sets the options on the column and the **coltyp** member sets the type of data that can be set in the column.

When the table is created without columns, they must be added by calling [JetAddColumn](gg294122\(v=exchg.10\).md) with the [JET\_COLUMNDEF](gg294130\(v=exchg.10\).md) structure. The **grbit** member of the [JET\_COLUMNDEF](gg294130\(v=exchg.10\).md) structure sets the options on the column and the **coltyp** member sets the type of data that can be set in the column. Default column values are set in the call to [JetAddColumn](gg294122\(v=exchg.10\).md) by specifying a value in the *pvDefault* parameter and the size in the *cbDefault* parameter. A column without a default value effectively has a default value of NULL.

The values in the table can only be set within the context of a transaction. The transaction begins in the call to [JetBeginTransaction](gg294083\(v=exchg.10\).md) and ends in the call to [JetCommitTransaction](gg269191\(v=exchg.10\).md). Inside the transaction, a single column value can be set by calling [JetSetColumn](gg294137\(v=exchg.10\).md), or multiple columns values can be set by calling [JetSetColumns](gg294050\(v=exchg.10\).md). [JetSetColumns](gg294050\(v=exchg.10\).md) uses an array of [JET\_SETCOLUMN](gg269233\(v=exchg.10\).md) structures to set multiple columns in the table. The data is contained in the *pvData* parameter of [JetSetColumn](gg294137\(v=exchg.10\).md), or the **pvData** member in [JET\_SETCOLUMN](gg269233\(v=exchg.10\).md) structure.

The [JET\_COLUMNBASE](gg269194\(v=exchg.10\).md), [JET\_COLUMNLIST](gg269228\(v=exchg.10\).md), and [JET\_COLUMNDEF](gg294130\(v=exchg.10\).md) structures are returned in the calls to [JetGetTableColumnInfo](gg294061\(v=exchg.10\).md), and [JetGetColumnInfo](gg269215\(v=exchg.10\).md) depending on the type of column that is retrieved. The [JET\_COLUMNBASE](gg269194\(v=exchg.10\).md) structure describes the parameters of the base column, and the [JET\_COLUMNLIST](gg269228\(v=exchg.10\).md) contains the information needed to traverse the temporary table that is created by the [JetGetColumnInfo](gg269215\(v=exchg.10\).md) and [JetGetTableColumnInfo](gg294061\(v=exchg.10\).md) functions.

