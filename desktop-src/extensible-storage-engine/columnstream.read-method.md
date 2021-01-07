---
description: "Learn more about: ColumnStream.Read method"
title: ColumnStream.Read method 
TOCTitle: 'Read method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.ColumnStream.Read(System.Byte[],System.Int32,System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.columnstream.read(v=EXCHG.10)
ms:contentKeyID: 55100988
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnStream.Read
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnStream.Read
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnStream.Read method

Reads a sequence of bytes from the current stream and advances the position within the stream by the number of bytes read.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Function Read ( _
    buffer As Byte(), _
    offset As Integer, _
    count As Integer _
) As Integer
'Usage
Dim instance As ColumnStream
Dim buffer As Byte()
Dim offset As Integer
Dim count As Integer
Dim returnValue As Integer

returnValue = instance.Read(buffer, offset, _
    count)
```

``` csharp
public override int Read(
    byte[] buffer,
    int offset,
    int count
)
```

#### Parameters

  - buffer  
    Type: \[\]  
    
    The buffer to read into.

<!-- end list -->

  - offset  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The offset in the buffer to read into.

<!-- end list -->

  - count  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The number of bytes to read.

#### Return value

Type: [System.Int32](/dotnet/api/system.int32)  
The number of bytes read into the buffer.  

## See also

#### Reference

[ColumnStream class](./columnstream-class.md)

[ColumnStream members](./columnstream-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
