---
description: "Learn more about: Api.JetRenameColumn method"
title: Api.JetRenameColumn method 
TOCTitle: 'JetRenameColumn method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetRenameColumn(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.String,System.String,Microsoft.Isam.Esent.Interop.RenameColumnGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetrenamecolumn(v=EXCHG.10)
ms:contentKeyID: 55100786
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetRenameColumn
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetRenameColumn
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetRenameColumn method

Changes the name of an existing column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetRenameColumn ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    name As String, _
    newName As String, _
    grbit As RenameColumnGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim name As String
Dim newName As String
Dim grbit As RenameColumnGrbitApi.JetRenameColumn(sesid, tableid, _
    name, newName, grbit)
```

``` csharp
public static void JetRenameColumn(
    JET_SESID sesid,
    JET_TABLEID tableid,
    string name,
    string newName,
    RenameColumnGrbit grbit
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

  - name  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the column.

<!-- end list -->

  - newName  
    Type: [System.String](/dotnet/api/system.string)  
    
    The new name of the column.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.RenameColumnGrbit](./renamecolumngrbit-enumeration.md)  
    
    Column rename options.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
