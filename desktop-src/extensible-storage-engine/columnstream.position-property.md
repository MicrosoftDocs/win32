---
description: "Learn more about: ColumnStream.Position property"
title: ColumnStream.Position property 
TOCTitle: 'Position property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnStream.Position
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columnstream.position(v=EXCHG.10)
ms:contentKeyID: 55100958
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnStream.Position
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnStream.get_Position
- Microsoft.Isam.Esent.Interop.ColumnStream.set_Position
- Microsoft.Isam.Esent.Interop.ColumnStream.Position
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnStream.Position property

Gets or sets the current position in the stream.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Property Position As Long
    Get
    Set
'Usage
Dim instance As ColumnStream
Dim value As Long

value = instance.Position

instance.Position = value
```

``` csharp
public override long Position { get; set; }
```

#### Property value

Type: [System.Int64](/dotnet/api/system.int64)  

## See also

#### Reference

[ColumnStream class](./columnstream-class.md)

[ColumnStream members](./columnstream-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
