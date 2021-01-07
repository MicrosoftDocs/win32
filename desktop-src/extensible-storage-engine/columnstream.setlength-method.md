---
description: "Learn more about: ColumnStream.SetLength method"
title: ColumnStream.SetLength method 
TOCTitle: 'SetLength method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.ColumnStream.SetLength(System.Int64)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columnstream.setlength(v=EXCHG.10)
ms:contentKeyID: 55100986
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnStream.SetLength
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnStream.SetLength
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnStream.SetLength method

Sets the length of the stream.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Sub SetLength ( _
    value As Long _
)
'Usage
Dim instance As ColumnStream
Dim value As Long

instance.SetLength(value)
```

``` csharp
public override void SetLength(
    long value
)
```

#### Parameters

  - value  
    Type: [System.Int64](/dotnet/api/system.int64)  
    
    The desired length, in bytes.

## See also

#### Reference

[ColumnStream class](./columnstream-class.md)

[ColumnStream members](./columnstream-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
