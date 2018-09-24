---
title: Api.JetOpenTempTable3 method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetOpenTempTable3 method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetOpenTempTable3(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_COLUMNDEF[],System.Int32,Microsoft.Isam.Esent.Interop.JET_UNICODEINDEX,Microsoft.Isam.Esent.Interop.TempTableGrbit,Microsoft.Isam.Esent.Interop.JET_TABLEID@,Microsoft.Isam.Esent.Interop.JET_COLUMNID[])
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetopentemptable3(v=EXCHG.10)
ms:contentKeyID: 55100774
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetOpenTempTable3
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetOpenTempTable3
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetOpenTempTable3 method

Creates a temporary table with a single index. A temporary table stores and retrieves records just like an ordinary table created using JetCreateTableColumnIndex. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner. Also see [JetOpenTempTable(JET\_SESID, \[\], Int32, TempTableGrbit, JET\_TABLEID, \[\])](dn292231\(v=exchg.10\).md), [JetOpenTemporaryTable(JET\_SESID, JET\_OPENTEMPORARYTABLE)](dn335326\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetOpenTempTable3 ( _
    sesid As JET_SESID, _
    columns As JET_COLUMNDEF(), _
    numColumns As Integer, _
    unicodeindex As JET_UNICODEINDEX, _
    grbit As TempTableGrbit, _
    <OutAttribute> ByRef tableid As JET_TABLEID, _
    columnids As JET_COLUMNID() _
)
'Usage
Dim sesid As JET_SESID
Dim columns As JET_COLUMNDEF()
Dim numColumns As Integer
Dim unicodeindex As JET_UNICODEINDEX
Dim grbit As TempTableGrbit
Dim tableid As JET_TABLEID
Dim columnids As JET_COLUMNID()

Api.JetOpenTempTable3(sesid, columns, _
    numColumns, unicodeindex, grbit, _
    tableid, columnids)
```

``` csharp
public static void JetOpenTempTable3(
    JET_SESID sesid,
    JET_COLUMNDEF[] columns,
    int numColumns,
    JET_UNICODEINDEX unicodeindex,
    TempTableGrbit grbit,
    out JET_TABLEID tableid,
    JET_COLUMNID[] columnids
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - columns  
    Type: \[\]  
    
    Column definitions for the columns created in the temporary table.

<!-- end list -->

  - numColumns  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    Number of column definitions.

<!-- end list -->

  - unicodeindex  
    Type: [Microsoft.Isam.Esent.Interop.JET\_UNICODEINDEX](dn351106\(v=exchg.10\).md)  
    
    The Locale ID and normalization flags that will be used to compare any Unicode key column data in the temporary table. When this is not present then the default options are used.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.TempTableGrbit](hh558517\(v=exchg.10\).md)  
    
    Table creation options.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_TABLEID](hh566310\(v=exchg.10\).md)  
    
    Returns the tableid of the temporary table. Closing this tableid with [JetCloseTable(JET\_SESID, JET\_TABLEID)](dn292109\(v=exchg.10\).md) frees the resources associated with the temporary table.

<!-- end list -->

  - columnids  
    Type: \[\]  
    
    The output buffer that receives the array of column IDs generated during the creation of the temporary table. The column IDs in this array will exactly correspond to the input array of column definitions. As a result, the size of this buffer must correspond to the size of the input array.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

