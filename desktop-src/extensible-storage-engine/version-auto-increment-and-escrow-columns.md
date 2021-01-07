---
description: "Learn more about: Version, Auto-Increment and Escrow Columns"
title: Version, Auto-Increment and Escrow Columns
TOCTitle: Version, Auto-Increment and Escrow Columns
ms:assetid: b12724a4-6846-49a7-9223-43895f91427e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294059(v=EXCHG.10)
ms:contentKeyID: 32765674
ms.date: 04/11/2016
ms.topic: article
---

# Version, Auto-Increment and Escrow Columns


_**Applies to:** Windows | Windows Server_

## Version, Auto-Increment and Escrow Columns

ESE provides version, auto-increment, and escrow update column types that have special abilities. The column options set in the **grbit** member of the [JET_COLUMNDEF](./jet-columndef-structure.md) structure used in the call to [JetAddColumn](./jetaddcolumn-function.md) indicate whether the column is one of the specialized types noted here.

### Version (JET_bitColumnVersion)

The version column option, applied only to JET_coltypLong columns, indicates that the column contains version information about the record that can be used to determine if an in-memory copy of a given record needs to be refreshed. Version columns are automatically incremented by ESE when the column is modified by the application via [JetUpdate](./jetupdate-function.md).

### Auto-Increment (JET_bitColumnAutoincrement)

Auto increment columns are automatically incremented by ESE when a new record is inserted into the table. The value contained in the auto-increment column is unique for every record in the table and is not guaranteed to be continuous. These values are not recycled, but can be reused in certain cases. Only columns of type JET_coltypLong and JET_coltypLongLong may be auto increment columns.

### Escrow (JET_bitColumnEscrowUpdate)

Escrow columns can be modified in the call to [JetEscrowUpdate](./jetescrowupdate-function.md). Updates in escrow are numeric delta operations that do not suffer from write conflicts. What this means is that any number of sessions can concurrently update an escrow column in a record via [JetEscrowUpdate](./jetescrowupdate-function.md) without conflicts. Note that any other update operation may still result in a write conflict with an escrow update operation. Escrow updates can only be made to columns of type JET_coltypLong that have a default value. These columns must also be added to a table before it is loaded with rows. Finally, rows containing an escrow update column may be configured to support a row finalization callback (JET_bitColumnFinalize) or to be automatically deleted if the ref count reaches zero (JET_bitColumnDeleteOnZero). For more information, see the [JET_COLUMNDEF](./jet-columndef-structure.md) structure.
