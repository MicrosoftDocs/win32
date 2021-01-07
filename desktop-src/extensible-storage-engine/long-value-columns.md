---
description: "Learn more about: Long Value Columns"
title: Long Value Columns
TOCTitle: Long Value Columns
ms:assetid: 0690f9d3-1a58-4e53-92e1-213630fc88f4
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269179(v=EXCHG.10)
ms:contentKeyID: 32765482
ms.date: 04/11/2016
ms.topic: article
---

# Long Value Columns


_**Applies to:** Windows | Windows Server_

## Long Value Columns

The ESE column types JET_coltypLongText and JET_coltypLongBinary are called long value column types. These columns are large string and large binary objects that may be stored in separate B+ trees away from the primary index. When long values are stored separate from the primary record, they are internally keyed on a long value ID (LID) and byte offset and accessed as a stream. Long value columns are added to the table in the call to [JetAddColumn](./jetaddcolumn-function.md) with the **coltyp** member of the [JET_COLUMNDEF](./jet-columndef-structure.md) structure set to either JET_coltypLongText or JET_coltypLongBinary. The maximum size of a Long Text or Long Binary column value is 2 GB -1.

ESE supports append, byte range overwrite, and set size operations for long value columns to support efficient stream implementations on these column types. By default, long value data is stored in a separate B+ tree if it is larger than 1024 bytes, or if the record does not fit on a single database page when the long value data is stored in the record. The application has the option to override the default behavior by setting options to store long value data in the record (JET_bitSetIntrinsicLV) or to force them to be stored in the separate B+ tree (JET_bitSetIntrinsicLV). These values are set in the *grbit* parameter in [JetSetColumn](./jetsetcolumn-function.md), or the **grbit** member [JET_SETCOLUMN](./jet-setcolumn-structure.md) used in the call to [JetSetColumns](./jetsetcolumns-function.md) as follows:

  - Append: (JET_bitSetAppendLV)

  - Byte Range Overwrite: (JET_bitSetOverwriteLV)

  - Set Size: (JET_bitSetSizeLV)

  - Force Separate: (JET_bitSetSeparateLV)

  - Store In Record: (JET_bitSetIntrinsicLV)

The long value data is set by indicating the offset into the long value blob, and the length of the long value data in the blob. The offset to the long value blob is set in the **ibLongValue** member of [JET_SETINFO](./jet-setinfo-structure.md) structure (for [JetSetColumn](./jetsetcolumn-function.md)) or the **ibLongValue** member of the [JET_SETCOLUMN](./jet-setcolumn-structure.md) structure (for [JetSetColumns](./jetsetcolumns-function.md)). The **pvData** member of [JET_SETCOLUMN](./jet-setcolumn-structure.md), and *pvData* parameter in the call to [JetSetColumn](./jetsetcolumn-function.md) contains the long value data. Updates to long value columns must be performed inside a transaction.

The long value data is always stored in a separate table is when the application sets the JET_bitSetSeparateLV or JET_bitSetIntrinsicLV, otherwise it is heuristically decided. ESE stores the long value separated if it is larger than 1024 bytes or if the record would not fit on a single database page if stored in record.

The following diagram shows the long value data stored in separate table. When a long value is stored outside the record, a new long valued ID is created to refer to its value. This allows multiple records to refer to the same column value. Reference counts to the data are increased if more than one record in the data points to the same long value data.

![ESE_Documentation_longvaluedtree2](images/Gg269179.ESE_Documentation_longvaluedtree2(EXCHG.10).gif "ESE_Documentation_longvaluedtree2")

ESE also supports a single instance store feature that allows multiple records to reference the same large binary object as though each record had its own copy of the information; thus avoiding duplicate copies of the column value data. This feature is enabled in the call to [JetPrepareUpdate](./jetprepareupdate-function.md) with the JET_prepInsertCopy option set in the *prep* parameter.
