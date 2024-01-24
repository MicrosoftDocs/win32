---
description: "Learn more about: Database Overview"
title: Database Overview
TOCTitle: Database Overview
ms:assetid: 6e4ebfab-8bd2-4fcf-9d91-2148a693596c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269290(v=EXCHG.10)
ms:contentKeyID: 32765582
ms.date: 04/11/2016
ms.topic: article
---

# Database Overview


_**Applies to:** Windows | Windows Server_

## Database Overview

The ESE database is an indexed sequential access method (ISAM) for storing and retrieving data. An ESE database is stored in a single file and consists of one or more user-defined tables. Data is organized in records in the table with one or more user-defined columns. Indexes that are created provide different organization for the entire set or a subset of records in the table. Using the ESE API, applications can create cursors that navigate records in the database in different sequential orders. The elements of the table are defined below:

  - **Column**: The column is a field in the table that stores a specific type of information. Columns can be fixed, or variable length, depending on the data type stored in them. Some columns, such as tagged columns take no space when **NULL** or set to the default value, and can contain multiple values.

  - **Records**: A record is a collection of columns values that have a unique identity as defined by the primary key.

  - **Index**: The index is a collection of key columns that define a stored ordering of records in the table. The clustered, or primary, index defines the order in which the records are stored within the table. Multiple indices can be defined in order to specify different orderings of traversal through records in the table. An index may also limit the set of records visible based on simple criteria such as the presence or absence of a particular key column value in the record.

  - **Cursor**: The cursor indicates the current record in the table and navigates to records in the table using the current index. The cursor also contains information on the state of the currently prepared update.

Columns and indices may be added-to or removed-from the table at any time. Although multiple indices may be defined, the data in the table is physically stored and logically clustered according to the primary index definition in a B+ tree. Each secondary index is stored in a separate B+ tree that contains only logical pointers to the actual data that is stored in the primary table. If no index is defined, the records in the table are stored in a B+ tree in the order of insertion and are referred to as the sequential index.

The diagram here is an example of how the data for the table is stored in a B+ tree according to the primary index. The primary index is for Name and ID, and a secondary index is created for the employee's office number. The entries for the secondary index are stored in a separate B+ tree that contains only pointers to the records stored in the primary table. For example, the office number 12348 in the secondary table is related to record 3 in the primary table. Record 3 contains the column values for the employee in office 12348. For more information, see the [Indexing in the Table](./indexing-in-the-table.md) topic.

![ESE_Documentation_tableandrow2](images/Gg269290.ESE_Documentation_tableandrow2(EXCHG.10).gif "ESE_Documentation_tableandrow2")
