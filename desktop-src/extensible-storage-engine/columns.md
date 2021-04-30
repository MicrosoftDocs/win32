---
description: "Learn more about: Columns"
title: Columns
TOCTitle: Columns
ms:assetid: bc16ca4c-e3c9-43db-ac16-284d7cc0926d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294073(v=EXCHG.10)
ms:contentKeyID: 32765688
ms.date: 04/11/2016
ms.topic: article
---

# Columns


_**Applies to:** Windows | Windows Server_

## Columns

A table can be created either with an initial set of columns by calling [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md) or without an initial set of columns by calling [JetCreateTable](./jetcreatetable-function.md). Tables in ESE can contain up to 127 fixed-length columns, 128 variable-length columns, and 64,993 tagged columns. Columns are identified by their name and ID and can be dynamically added to the table with [JetAddColumn](./jetaddcolumn-function.md). Columns are created with a specific data type and an optional set of attributes, such as whether the column is fixed-length or whether it can be NULL or not.

The type of a column determines the data that may be stored in the column and many of the properties of the column, including its order for indexing. ESE supports a wide range of column types, ranging in size from 1 bit to 2 GB (2146483647 ASCII characters or 1073741823 Unicode characters). For a complete list of the column data types supported by ESE, see the [JET_COLTYP](./jet-coltyp.md) topic. The topics below discuss a few of the columns types supported by ESE:

  - [Tagged, Fixed and Variable Columns](./tagged-fixed-and-variable-columns.md)

  - [Version, Auto-Increment and Escrow Columns](./version-auto-increment-and-escrow-columns.md)

  - [Long Value Columns](./long-value-columns.md)

  - [Multi-Valued Sparse Columns](./multi-valued-sparse-columns.md)

  - [User Defined Columns](./user-defined-columns.md)

  - [Using Columns in a Table](./using-columns-in-a-table.md)
