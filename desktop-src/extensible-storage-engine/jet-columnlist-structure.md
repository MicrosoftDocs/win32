---
description: "Learn more about: JET_COLUMNLIST Structure"
title: JET_COLUMNLIST Structure
TOCTitle: JET_COLUMNLIST Structure
ms:assetid: 3899676f-c96e-4f15-9089-4faea6808bc2
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269228(v=EXCHG.10)
ms:contentKeyID: 32765530
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

# JET_COLUMNLIST Structure


_**Applies to:** Windows | Windows Server_

## JET_COLUMNLIST Structure

The **JET_COLUMNLIST** structure contains the information necessary to traverse the temporary table that is created by the [JetGetColumnInfo](./jetgetcolumninfo-function.md) and [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) functions. Each row in the temporary table describes a column in the table given in the API call. This structure is used with only with [JetGetColumnInfo](./jetgetcolumninfo-function.md) and [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md).

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      unsigned long cRecord;
      JET_COLUMNID columnidPresentationOrder;
      JET_COLUMNID columnidcolumnname;
      JET_COLUMNID columnidcolumnid;
      JET_COLUMNID columnidcoltyp;
      JET_COLUMNID columnidCountry;
      JET_COLUMNID columnidLangid;
      JET_COLUMNID columnidCp;
      JET_COLUMNID columnidCollate;
      JET_COLUMNID columnidcbMax;
      JET_COLUMNID columnidgrbit;
      JET_COLUMNID columnidDefault;
      JET_COLUMNID columnidBaseTableName;
      JET_COLUMNID columnidBaseColumnName;
      JET_COLUMNID columnidDefinitionName;
    } JET_COLUMNLIST;
```

### Members

**cbStruct**

The size of the structure in bytes. The API call will update this field, so the caller should ensure that this value matches sizeof( JET_COLUMNLIST ).

**tableid**

The table identifier of the temporary table that was created. It is the responsibility of the caller to close the table.

**cRecord**

The number of records in the temporary table that was created by the API call.

**columnidPresentationOrder**

The column identifier of the presentation order.

The presentation order is used to sort the rows of the temporary table. The presentation order is a fixed [JET_coltypLong](./jet-coltyp.md). If the information level that was specified was not a compact level, then it is also marked as JET_bitColumnTTKey.

**columnidcolumnname**

The column identifier of the name of the column.

If the information level specified was not compact, then it is also marked as JET_bitColumnTTKey.

**columnidcolumnid**

The column identifier of the column identifier.

The column identifier is a fixed [JET_coltypLong](./jet-coltyp.md).

**columnidcoltyp**

The column identifier of the column type.

The column type is a fixed [JET_coltypLong](./jet-coltyp.md).

**columnidCountry**

The column identifier of the country code.

The country code is a fixed [JET_coltypShort](./jet-coltyp.md).

**columnidLangid**

The column identifier of the language identifier.

The language identifier is a fixed [JET_coltypShort](./jet-coltyp.md).

**columnidCp**

The column identifier of the code page.

The code page is a fixed [JET_coltypShort](./jet-coltyp.md).

**columnidCollate**

The column identifier of the collation sequence.

The collation sequence is a fixed [JET_coltypShort](./jet-coltyp.md).

**columnidcbMax**

The column identifier of the **cbMax** field.

The **cbMax** is a fixed [JET_coltypLong](./jet-coltyp.md).

**columnidgrbit**

The column identifier of the *grbits* of the column. The *grbit* field is a fixed [JET_coltypLong](./jet-coltyp.md). For more information about these bits, see [JET_COLUMNDEF](./jet-columndef-structure.md).

The following are possible values for **columnidgrbit**:

JET_bitColumnTagged

JET_bitColumnFixed

JET_bitColumnUpdatable

JET_bitColumnNotNULL

JET_bitColumnAutoincrement

JET_bitColumnVersion

JET_bitColumnMultiValued

JET_bitColumnEscrowUpdate

JET_bitColumnFinalize

JET_bitColumnDeleteOnZero

JET_bitColumnUserDefinedDefault

**columnidDefault**

The column identifier of the default value of the column.

The default value is a [JET_coltypLongBinary](./jet-coltyp.md).

**columnidBaseTableName**

The column identifier of the name of the table from which the table was derived.

The table name is a [JET_coltypText](./jet-coltyp.md).

**columnidBaseColumnName**

The column identifier of the name of the column from which the column was derived.

The column name is a [JET_coltypText](./jet-coltyp.md).

**columnidDefinitionName**

The column identifier of the name of the column definition.

The column definition name is a [JET_coltypText](./jet-coltyp.md).

### Remarks

By default, the order of the rows in the temporary table is sorted by the name of the column. It can also be sorted by column identifier. For more information about how to sort by column identifier, see [JetGetColumnInfo](./jetgetcolumninfo-function.md) and [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md).

The call to [JetGetColumnInfo](./jetgetcolumninfo-function.md) or [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) might specify a compact form of results. If any columns have been inherited from a template table, the compact results will not store them.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLTYP](./jet-coltyp.md)

[JET_COLUMNDEF](./jet-columndef-structure.md)

[JET_COLUMNID](./jet-columnid.md)

[JET_ERR](./jet-err.md)

[JET_GRBIT](./jet-grbit.md)

[JET_SESID](./jet-sesid.md)

[JET_TABLEID](./jet-tableid.md)

[JetGetColumnInfo](./jetgetcolumninfo-function.md)

[JetGetTableColumnInfo](./jetgettablecolumninfo-function.md)
