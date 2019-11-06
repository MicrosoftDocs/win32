---
title: Api.JetGetDatabaseFileInfo method (String, JET_DBINFOMISC, JET_DbInfo)
TOCTitle: JetGetDatabaseFileInfo method (String, JET_DBINFOMISC, JET_DbInfo)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetDatabaseFileInfo(System.String,Microsoft.Isam.Esent.Interop.JET_DBINFOMISC@,Microsoft.Isam.Esent.Interop.JET_DbInfo)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetdatabasefileinfo(v=EXCHG.10)
ms:contentKeyID: 55100709
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetDatabaseFileInfo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetDatabaseFileInfo method (String, JET_DBINFOMISC, JET_DbInfo)

Retrieves certain information about the given database.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetDatabaseFileInfo ( _
    databaseName As String, _
    <OutAttribute> ByRef dbinfomisc As JET_DBINFOMISC, _
    infoLevel As JET_DbInfo _
)
'Usage
Dim databaseName As String
Dim dbinfomisc As JET_DBINFOMISC
Dim infoLevel As JET_DbInfoApi.JetGetDatabaseFileInfo(databaseName, _
    dbinfomisc, infoLevel)
```

``` csharp
public static void JetGetDatabaseFileInfo(
    string databaseName,
    out JET_DBINFOMISC dbinfomisc,
    JET_DbInfo infoLevel
)
```

#### Parameters

  - databaseName  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    The file name of the database.

<!-- end list -->

  - dbinfomisc  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBINFOMISC](hh538867\(v=exchg.10\).md)  
    
    The value to be retrieved.

<!-- end list -->

  - infoLevel  
    Type: [Microsoft.Isam.Esent.Interop.JET_DbInfo](hh163267\(v=exchg.10\).md)  
    
    The specific data to retrieve.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[JetGetDatabaseFileInfo overload](dn292157\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

