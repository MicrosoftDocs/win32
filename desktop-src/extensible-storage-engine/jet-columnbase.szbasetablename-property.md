---
description: "Learn more about: JET_COLUMNBASE.szBaseTableName property"
title: JET_COLUMNBASE.szBaseTableName property 
TOCTitle: 'szBaseTableName property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.szBaseTableName
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_columnbase.szbasetablename(v=EXCHG.10)
ms:contentKeyID: 55103375
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.szBaseTableName
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.get_szBaseTableName
- Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.set_szBaseTableName
- Microsoft.Isam.Esent.Interop.JET_COLUMNBASE.szBaseTableName
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNBASE.szBaseTableName property

Gets the table from which the current table inherits its DDL.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property szBaseTableName As String
    Get
    Friend Set
'Usage
Dim instance As JET_COLUMNBASE
Dim value As String

value = instance.szBaseTableName
```

``` csharp
public string szBaseTableName { get; internal set; }
```

#### Property value

Type: [System.String](/dotnet/api/system.string)  

## See also

#### Reference

[JET_COLUMNBASE class](./jet-columnbase-class.md)

[JET_COLUMNBASE members](./jet-columnbase-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
