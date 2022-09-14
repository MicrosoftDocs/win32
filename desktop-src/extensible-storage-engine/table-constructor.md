---
description: "Learn more about: Table constructor"
title: Table constructor 
TOCTitle: 'Table constructor '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Table.#ctor(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,System.String,Microsoft.Isam.Esent.Interop.OpenTableGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.table.table(v=EXCHG.10)
ms:contentKeyID: 55104142
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Table.Table
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Table..ctor
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Table constructor

Initializes a new instance of the Table class. The table is opened from the given database.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub New ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    name As String, _
    grbit As OpenTableGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim name As String
Dim grbit As OpenTableGrbit

Dim instance As New Table(sesid, dbid, _
    name, grbit)
```

``` csharp
public Table(
    JET_SESID sesid,
    JET_DBID dbid,
    string name,
    OpenTableGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](./jet-dbid-structure.md)  
    
    The database to open the table in.

<!-- end list -->

  - name  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the table.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.OpenTableGrbit](./opentablegrbit-enumeration.md)  
    
    JetOpenTable options.

## See also

#### Reference

[Table class](./table-class.md)

[Table members](./table-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
