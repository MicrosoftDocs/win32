---
description: "Learn more about: Api.JetRenameTable method"
title: Api.JetRenameTable method 
TOCTitle: 'JetRenameTable method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetRenameTable(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,System.String,System.String)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetrenametable(v=EXCHG.10)
ms:contentKeyID: 55100788
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetRenameTable
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetRenameTable
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetRenameTable method

Changes the name of an existing table.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetRenameTable ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    tableName As String, _
    newTableName As String _
)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim tableName As String
Dim newTableName As StringApi.JetRenameTable(sesid, dbid, _
    tableName, newTableName)
```

``` csharp
public static void JetRenameTable(
    JET_SESID sesid,
    JET_DBID dbid,
    string tableName,
    string newTableName
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](./jet-dbid-structure.md)  
    
    The database containing the table.

<!-- end list -->

  - tableName  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the table.

<!-- end list -->

  - newTableName  
    Type: [System.String](/dotnet/api/system.string)  
    
    The new name of the table.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
