---
description: "Learn more about: Api.JetGetTableColumnInfo method (JET_SESID, JET_TABLEID, String, JET_COLUMNDEF)"
title: Api.JetGetTableColumnInfo method (JET_SESID, JET_TABLEID, String, JET_COLUMNDEF)
TOCTitle: JetGetTableColumnInfo method (JET_SESID, JET_TABLEID, String, JET_COLUMNDEF)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetTableColumnInfo(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.String,Microsoft.Isam.Esent.Interop.JET_COLUMNDEF@)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgettablecolumninfo(v=EXCHG.10)
ms:contentKeyID: 55100724
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetTableColumnInfo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetTableColumnInfo method (JET_SESID, JET_TABLEID, String, JET_COLUMNDEF)

Retrieves information about a table column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetTableColumnInfo ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    columnName As String, _
    <OutAttribute> ByRef columndef As JET_COLUMNDEF _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim columnName As String
Dim columndef As JET_COLUMNDEFApi.JetGetTableColumnInfo(sesid, _
    tableid, columnName, columndef)
```

``` csharp
public static void JetGetTableColumnInfo(
    JET_SESID sesid,
    JET_TABLEID tableid,
    string columnName,
    out JET_COLUMNDEF columndef
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The table containing the column.

<!-- end list -->

  - columnName  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the column.

<!-- end list -->

  - columndef  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNDEF](./jet-columndef-class.md)  
    
    Filled in with information about the column.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[JetGetTableColumnInfo overload](./api.jetgettablecolumninfo-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
