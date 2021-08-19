---
description: "Learn more about: JET_ENUMCOLUMN Structure"
title: JET_ENUMCOLUMN Structure
TOCTitle: JET_ENUMCOLUMN Structure
ms:assetid: f8f512fd-5fcf-47ed-a5db-2fb3bd76c2d7
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294138(v=EXCHG.10)
ms:contentKeyID: 32765752
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

# JET_ENUMCOLUMN Structure


_**Applies to:** Windows | Windows Server_

## JET_ENUMCOLUMN Structure

The **JET_ENUMCOLUMN** structure enumerates the column values of a record when the [JetEnumerateColumns](./jetenumeratecolumns-function.md) function is used. [JetEnumerateColumns](./jetenumeratecolumns-function.md) returns an array of **JET_ENUMCOLUMN** structures. The array is returned in memory that is allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to that API.

```cpp
    typedef struct {
      JET_COLUMNID columnid;
      JET_ERR err;
      union {
        struct {
          unsigned long cEnumColumnValue;
          JET_ENUMCOLUMNVALUE rgEnumColumnValue;
        };
        struct {
          unsigned long cbData;
          void* pvData;
        };
      };
    } JET_ENUMCOLUMN;
```

### Members

**columnid**

The column ID that was enumerated.

**err**

The column status code that results from the enumeration of the column.


| <p>Error Codes</p> | <p>Meaning</p> | 
|--------------------|----------------|
| <p>JET_errBadColumnId</p> | <p>The column ID is outside the legal limits of a column ID.</p> | 
| <p>JET_errColumnNotFound</p> | <p>The column described by the column ID does not exist in the table.</p> | 
| <p>JET_wrnColumnNull</p> | <p>All values for this column are NULL.</p> | 
| <p>JET_wrnColumnPresent</p> | <p>JET_bitEnumeratePresenceOnly was specified and at least one non-NULL column value would have been returned for this column.</p> | 
| <p>JET_wrnColumnSingleValue</p> | <p>JET_bitEnumerateCompressOutput was specified and exactly one non-NULL column value has been returned for this column. As a result, the compressed form of <strong>JET_ENUMCOLUMN</strong> has been returned. See <strong>JET_ENUMCOLUMN</strong> for more information.</p> | 
| <p>JET_wrnColumnSkipped</p> | <p>The column ID in the <a href="gg269251(v=exchg.10).md">JET_ENUMCOLUMNID</a> struct corresponding to this <strong>JET_ENUMCOLUMN</strong> struct was zero.</p> | 



**cEnumColumnValue**

The array of column values that was enumerated for the column. The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This output buffer is used when the column status code is not equal to JET_wrnColumnSingleValue. For more information, see [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This is returned if "err \!= JET_wrnColumnSingleValue".

**rgEnumColumnValue**

The array of column values that was enumerated for the column. The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This output buffer is used when the column status code is not equal to JET_wrnColumnSingleValue. For more information, see [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This is returned if "err \!= JET_wrnColumnSingleValue".

**cbData**

The column value that was enumerated for the column.

The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This output buffer is only used when the column status code is JET_wrnColumnSingleValue. For more information, see [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This is returned if "err == JET_wrnColumnSingleValue".

**pvData**

The column value that was enumerated for the column.

The output buffer is returned in memory that was allocated using the [realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019) compatible callback that was supplied to [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This output buffer is only used when the column status code is JET_wrnColumnSingleValue. For more information, see [JetEnumerateColumns](./jetenumeratecolumns-function.md).

This is returned if "err == JET_wrnColumnSingleValue".

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_ENUMCOLUMNID](./jet-enumcolumnid-structure.md)  
[JET_ENUMCOLUMNVALUE](./jet-enumcolumnvalue-structure.md)  
[JetEnumerateColumns](./jetenumeratecolumns-function.md)  
[realloc](/cpp/c-runtime-library/reference/realloc?view=vs-2019)
