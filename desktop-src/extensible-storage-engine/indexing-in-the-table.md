---
description: "Learn more about: Indexing in the Table"
title: Indexing in the Table
TOCTitle: Indexing in the Table
ms:assetid: d86c2c6b-d001-468d-ab74-937911b0036d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294106(v=EXCHG.10)
ms:contentKeyID: 32765721
ms.date: 04/11/2016
ms.topic: article
---

# Indexing in the Table


_**Applies to:** Windows | Windows Server_

## Indexing in the Table

An index is a set of key columns that define a persistent ordering of records in a table. Records are index entries in the primary index. One primary index and multiple secondary indexes can be defined to create different orders of data in the table.

Although multiple indices can be defined, the records are physically stored in B+ trees in the order specified by the primary index. The primary index is always a clustered index, and must also be unique. The primary index must be declared before the first table update to preserve the index ordering. When no primary index is defined by the application, the data is stored in the order in which records are added to the table. This special index is referred to as a sequential index.

Separate B+ trees are used to order records according to the secondary index. Index entries in the secondary index contain pointers to the data stored according to the primary index. The index entries for records in the primary index must be unique because the secondary index points to the record using the primary key of the record. Secondary indices may or may not have a uniqueness constraint. For more information, see the [Database Overview](./database-overview.md) topic.
