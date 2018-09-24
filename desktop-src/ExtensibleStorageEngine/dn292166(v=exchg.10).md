---
title: Api.JetGetIndexInfo method (JET_SESID, JET_DBID, String, String, JET_INDEXLIST, JET_IdxInfo) (Microsoft.Isam.Esent.Interop)
TOCTitle: JetGetIndexInfo method (JET_SESID, JET_DBID, String, String, JET_INDEXLIST, JET_IdxInfo)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetIndexInfo(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,System.String,System.String,Microsoft.Isam.Esent.Interop.JET_INDEXLIST@,Microsoft.Isam.Esent.Interop.JET_IdxInfo)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetindexinfo(v=EXCHG.10)
ms:contentKeyID: 55107227
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetIndexInfo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetIndexInfo method (JET\_SESID, JET\_DBID, String, String, JET\_INDEXLIST, JET\_IdxInfo)

Retrieves information about indexes on a table.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetIndexInfo ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    tablename As String, _
    indexname As String, _
    <OutAttribute> ByRef result As JET_INDEXLIST, _
    infoLevel As JET_IdxInfo _
)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim tablename As String
Dim indexname As String
Dim result As JET_INDEXLIST
Dim infoLevel As JET_IdxInfoApi.JetGetIndexInfo(sesid, dbid, _
    tablename, indexname, result, infoLevel)
```

``` csharp
public static void JetGetIndexInfo(
    JET_SESID sesid,
    JET_DBID dbid,
    string tablename,
    string indexname,
    out JET_INDEXLIST result,
    JET_IdxInfo infoLevel
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_DBID](hh596176\(v=exchg.10\).md)  
    
    The database to use.

<!-- end list -->

  - tablename  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The name of the table to retrieve index information about.

<!-- end list -->

  - indexname  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The name of the index to retrieve information about.

<!-- end list -->

  - result  
    Type: [Microsoft.Isam.Esent.Interop.JET\_INDEXLIST](dn335123\(v=exchg.10\).md)  
    
    Filled in with information about indexes on the table.

<!-- end list -->

  - infoLevel  
    Type: [Microsoft.Isam.Esent.Interop.JET\_IdxInfo](hh565119\(v=exchg.10\).md)  
    
    The type of information to retrieve.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[JetGetIndexInfo overload](dn292165\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

