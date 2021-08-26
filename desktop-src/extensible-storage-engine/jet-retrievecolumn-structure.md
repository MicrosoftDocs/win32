---
description: "Learn more about: JET_RETRIEVECOLUMN Structure"
title: JET_RETRIEVECOLUMN Structure
TOCTitle: JET_RETRIEVECOLUMN Structure
ms:assetid: 8e23bed5-5279-4733-b787-a073a0e8d5a5
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269334(v=EXCHG.10)
ms:contentKeyID: 32765623
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

# JET_RETRIEVECOLUMN Structure


_**Applies to:** Windows | Windows Server_

## JET_RETRIEVECOLUMN Structure

The **JET_RETRIEVECOLUMN** structure contains input and output parameters for [JetRetrieveColumns](./jetretrievecolumns-function.md). Fields in the structure describe what column value to retrieve, how to retrieve it, and where to save results.

```cpp
    typedef struct {
      JET_COLUMNID columnid;
      void* pvData;
      unsigned long cbData;
      unsigned long cbActual;
      JET_GRBIT grbit;
      unsigned long ibLongValue;
      unsigned long itagSequence;
      JET_COLUMNID columnidNextTagged;
      JET_ERR err;
    } JET_RETRIEVECOLUMN;
```

### Members

**columnid**

The column identifier for the column to retrieve.

**pvData**

A pointer to begin storing data that is retrieved from the column value.

**cbData**

The size of allocation beginning at **pvData**, in bytes. The retrieve column operation will not store more data at **pvData** than **cbData**.

**cbActual**

The size, in bytes, of data that is retrieved by a retrieve column operation.

**grbit**

A group of bits that contain the options for column retrieval, which include zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitRetrieveCopy</p> | <p>Retrieves the modified value instead of the original value. If the value has not been modified, then the original value is retrieved. In this way, a value that has not yet been inserted or updated can be retrieved when a record is inserted or updated.</p> | 
| <p>JET_bitRetrieveFromIndex</p> | <p>Retrieves column values from the index without accessing the record, if possible. In this way, unnecessary loading of records can be avoided when needed data is available from index entries themselves. In cases where the original column value cannot be retrieved from the index, because of irreversible transformations or data truncation, the record will be accessed and the data retrieved as normal. This is a performance option and should only be specified when it is likely that the column value can be retrieved from the index. This option should not be specified if the current index is the clustered index, since the index entries for the clustered, or primary, index are the records themselves. This bit cannot be set if JET_bitRetrieveFromPrimaryBookmark is also set.</p> | 
| <p>JET_bitRetrieveFromPrimaryBookmark</p> | <p>Retrieves column values from the index bookmark, and can differ from the index value when a column appears both in the primary index and the current index. This option should not be specified if the current index is the clustered, or primary, index. This bit cannot be set if JET_bitRetrieveFromIndex is also set.</p> | 
| <p>JET_bitRetrieveTag</p> | <p>Retrieves the sequence number of a multi-valued column value in pretinfo-&gt;itagSequence. The itagSequence field is often used an input for retrieving multi-valued column values from a record. However, when retrieving values from an index, it is also possible to associate the index entry with a particular sequence number and retrieve this sequence number as well. Retrieving the sequence number can be a costly operation and should only be done if necessary.</p> | 
| <p>JET_ bitRetrieveNull</p> | <p>Retrieves multi-valued column NULL values. If this option is not specified, multi-valued column NULL values will automatically be skipped.</p> | 
| <p>JET_bitRetrieveIgnoreDefault</p> | <p>Causes a NULL value to be returned when the requested sequence number is 1 and there are no set values for the column in the record. This option affects only multi-valued columns.</p> | 
| <p>JET_bitRetrieveLongId</p> | <p>This flag is for internal use only and is not intended to be used in your application.</p> | 
| <p>JET_bitRetrieveLongValueRefCount</p> | <p>This flag is for internal use only and is not intended to be used in your application.</p> | 



**ibLongValue**

The offset to the first byte to be retrieved from a column of type [JET_coltypLongBinary](./jet-coltyp.md) or [JET_coltypLongText](./jet-coltyp.md).

**itagSequence**

The sequence number of the values that are contained in a multi-valued column. **itagSequence** here in the **JET_RETRIEVECOLUMN** can be 0. If the **itagSequence** is 0 then the number of instances of a multi-valued column are returned instead of any column data. An **itagSequence** value of 0 cannot be used in calls to [JetRetrieveColumn](./jetretrievecolumn-function.md).

**columnidNextTagged**

The **columnid** of the tagged, multi-valued, or sparse column when all tagged columns are retrieved by passing 0 as the **columnid** to [JetRetrieveColumn](./jetretrievecolumn-function.md).

**err**

Error codes and warnings returned from the retrieval of the column.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_RETRIEVECOLUMN]()  
[JetRetrieveColumn](./jetretrievecolumn-function.md)  
[JetRetrieveColumns](./jetretrievecolumns-function.md)
