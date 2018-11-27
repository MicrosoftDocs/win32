---
title: Columns
TOCTitle: Columns
ms:assetid: bc16ca4c-e3c9-43db-ac16-284d7cc0926d
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294073(v=EXCHG.10)
ms:contentKeyID: 32765688
ms.date: 04/11/2016
ms.topic: article
---

# Columns


_**Applies to:** Windows | Windows Server_

## Columns

A table can be created either with an initial set of columns by calling [JetCreateTableColumnIndex](gg269343\(v=exchg.10\).md) or without an initial set of columns by calling [JetCreateTable](gg269210\(v=exchg.10\).md). Tables in ESE can contain up to 127 fixed-length columns, 128 variable-length columns, and 64,993 tagged columns. Columns are identified by their name and ID and can be dynamically added to the table with [JetAddColumn](gg294122\(v=exchg.10\).md). Columns are created with a specific data type and an optional set of attributes, such as whether the column is fixed-length or whether it can be NULL or not.

The type of a column determines the data that may be stored in the column and many of the properties of the column, including its order for indexing. ESE supports a wide range of column types, ranging in size from 1 bit to 2 GB (2146483647 ASCII characters or 1073741823 Unicode characters). For a complete list of the column data types supported by ESE, see the [JET\_COLTYP](gg269213\(v=exchg.10\).md) topic. The topics below discuss a few of the columns types supported by ESE:

  - [Tagged, Fixed and Variable Columns](gg269304\(v=exchg.10\).md)

  - [Version, Auto-Increment and Escrow Columns](gg294059\(v=exchg.10\).md)

  - [Long Value Columns](gg269179\(v=exchg.10\).md)

  - [Multi-Valued Sparse Columns](gg269225\(v=exchg.10\).md)

  - [User Defined Columns](gg294091\(v=exchg.10\).md)

  - [Using Columns in a Table](gg269178\(v=exchg.10\).md)

