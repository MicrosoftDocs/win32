---
title: ColumnStream.Position property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Position property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnStream.Position
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.columnstream.position(v=EXCHG.10)
ms:contentKeyID: 55100958
ms.date: 07/30/2014
ms.topic: article
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

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
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

Type: [System.Int64](https://msdn.microsoft.com/en-us/library/6yy583ek)  

## See also

#### Reference

[ColumnStream class](dn334143\(v=exchg.10\).md)

[ColumnStream members](dn334190\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

