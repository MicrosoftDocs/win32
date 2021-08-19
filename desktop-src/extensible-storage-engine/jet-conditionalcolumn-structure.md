---
description: "Learn more about: JET_CONDITIONALCOLUMN Structure"
title: JET_CONDITIONALCOLUMN Structure
TOCTitle: JET_CONDITIONALCOLUMN Structure
ms:assetid: 2ca6b4ba-0dc4-47d5-b072-324e5a381d0d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269214(v=EXCHG.10)
ms:contentKeyID: 32765517
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_CONDITIONALCOLUMN Structure


_**Applies to:** Windows | Windows Server_

## JET_CONDITIONALCOLUMN Structure

The **JET_CONDITIONALCOLUMN** structure defines how conditional indexing is performed for a given index. A conditional index contains an index entry for only those rows that match the specified condition. However, the conditional column is not part of the index's key, it only controls the presence of the index entry.

```cpp
    typedef struct tagJET_CONDITIONALCOLUMN {
      unsigned long cbStruct;
      tchar* szColumnName;
      JET_GRBIT grbit;
    } JET_CONDITIONALCOLUMN;
```

### Members

**cbStruct**

This field must be initialized to sizeof( JET_CONDITIONALCOLUMN ), in bytes.

**szColumnName**

The name of the column that contains the data on which the database engine is conditionally indexing the row.

**grbit** A group of bits that gives the options for the conditional index. Passing in zero or logically-**OR**ed values is not valid for **JET_CONDITIONALCOLUMN**. The bit field must be exactly one of the following:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitIndexColumnMustBeNull</p> | <p>The column specified by the <em>szColumnName</em> parameter must be NULL for an index entry for a given row to appear in this index.</p> | 
| <p>JET_bitIndexColumnMustBeNonNull</p> | <p>The column specified by the <em>szColumnName</em> parameter must be non-NULL for an index entry in order for a given row to appear in this index.</p> | 



### Remarks

A conditional index contains an index entry for only those rows that match the specified condition. For example, a column could be named "Marked", and when a row is marked, the column is set to a non-NULL value. A JET_bitIndexColumnMustBeNonNull conditional index on this column will show all rows that are marked, and a JET_bitIndexColumnMustBeNull conditional index will show rows that are not marked. This is also a convenient way to perform a flag deletion and garbage collecting index.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_CONDITIONALCOLUMN_W</strong> (Unicode) and <strong>JET_CONDITIONALCOLUMN_A</strong> (ANSI).</p> | 



### See Also

[JET_GRBIT](./jet-grbit.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)
