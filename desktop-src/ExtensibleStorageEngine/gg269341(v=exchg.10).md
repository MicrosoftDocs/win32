---
title: Indexing over Multi-Valued Columns
TOCTitle: Indexing over Multi-Valued Columns
ms:assetid: 90e31df2-2f5b-47a8-84c1-ece6bcc40858
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269341(v=EXCHG.10)
ms:contentKeyID: 32765630
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
---

# Indexing over Multi-Valued Columns


_**Applies to:** Windows | Windows Server_

## Indexing over Multi-Valued Columns

Indexing over multi-valued columns is only performed over the first multi-valued column in the index. The first multi-valued column is expanded so that every value in the column is indexed. All other multi-valued columns are indexed only over the first value in the column. For example, an index is defined over Column A, and Column B, where both of these columns are multi-valued. In a given record, Column A has the values red, and blue, and Column B has the values 1, 2, and 3. The resulting index would give entries for red-1 and blue-1. The values in the second column, Column B, are not expanded. Note that even though every tagged column may be multi-valued only tagged columns that are explicitly flagged as multi-valued via JET\_bitColumnMultiValued are expanded in this way. Also, due to the fact that primary index entries contain records, it is not permitted to have a primary index over a multi-valued column because that would result in multiple locations in the index in which the record would have to reside. For more information, see the [Tagged, Fixed and Variable Columns](gg269304\(v=exchg.10\).md) topic.

Starting in Windows Vista, users have the option to set the JET\_bitIndexCrossProduct option when the index is created with [JetCreateIndex](gg294099\(v=exchg.10\).md) or [JetCreateIndex2](gg269324\(v=exchg.10\).md) using the [JET\_INDEXCREATE](gg269186\(v=exchg.10\).md) structure. When this option is set on an index, all multi-valued key columns in the index are expanded, and a cross product is created in the index for every value in those columns. The example above now yields entries for red-1, red-2, red-3, blue-1, blue-2, blue-3. Again, each key column must be explicitly declared to be multi-valued via JET\_bitColumnMultiValued to be expanded in the index.

