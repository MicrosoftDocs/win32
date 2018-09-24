---
title: Api.GetTableIndexes method (JET_SESID, JET_DBID, String) (Microsoft.Isam.Esent.Interop)
TOCTitle: GetTableIndexes method (JET_SESID, JET_DBID, String)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.GetTableIndexes(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,System.String)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.gettableindexes(v=EXCHG.10)
ms:contentKeyID: 55100648
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.GetTableIndexes
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.GetTableIndexes method (JET\_SESID, JET\_DBID, String)

Iterates over all the indexs in the table, returning information about each one.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function GetTableIndexes ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    tablename As String _
) As IEnumerable(Of IndexInfo)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim tablename As String
Dim returnValue As IEnumerable(Of IndexInfo)

returnValue = Api.GetTableIndexes(sesid, _
    dbid, tablename)
```

``` csharp
public static IEnumerable<IndexInfo> GetTableIndexes(
    JET_SESID sesid,
    JET_DBID dbid,
    string tablename
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_DBID](hh596176\(v=exchg.10\).md)  
    
    The database containing the table.

<!-- end list -->

  - tablename  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The name of the table.

#### Return value

Type: [System.Collections.Generic.IEnumerable](http://msdn2.microsoft.com/en-us/library/9eekhta0)\<[IndexInfo](dn350919\(v=exchg.10\).md)\>  
An iterator over an IndexInfo for each index in the table.  

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[GetTableIndexes overload](dn292087\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

