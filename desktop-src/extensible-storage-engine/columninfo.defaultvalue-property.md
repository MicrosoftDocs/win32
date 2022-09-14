---
description: "Learn more about: ColumnInfo.DefaultValue property"
title: ColumnInfo.DefaultValue property 
TOCTitle: 'DefaultValue property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnInfo.DefaultValue
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columninfo.defaultvalue(v=EXCHG.10)
ms:contentKeyID: 55100932
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnInfo.DefaultValue
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnInfo.DefaultValue
- Microsoft.Isam.Esent.Interop.ColumnInfo.get_DefaultValue
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnInfo.DefaultValue property

Gets the default value of the column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property DefaultValue As IList(Of Byte)
    Get
'Usage
Dim instance As ColumnInfo
Dim value As IList(Of Byte)

value = instance.DefaultValue
```

``` csharp
public IList<byte> DefaultValue { get; }
```

#### Property value

Type: [System.Collections.Generic.IList](/dotnet/api/system.collections.generic.ilist-1)\<[Byte](/dotnet/api/system.byte)\>  

## See also

#### Reference

[ColumnInfo class](./columninfo-class.md)

[ColumnInfo members](./columninfo-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
