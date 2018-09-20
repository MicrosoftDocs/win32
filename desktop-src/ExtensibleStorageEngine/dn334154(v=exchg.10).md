---
title: ColumnStream.Seek method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Seek method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.ColumnStream.Seek(System.Int64,System.IO.SeekOrigin)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.columnstream.seek(v=EXCHG.10)
ms:contentKeyID: 55100949
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnStream.Seek
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnStream.Seek
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnStream.Seek method

Sets the position in the current stream.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides Function Seek ( _
    offset As Long, _
    origin As SeekOrigin _
) As Long
'Usage
Dim instance As ColumnStream
Dim offset As Long
Dim origin As SeekOrigin
Dim returnValue As Long

returnValue = instance.Seek(offset, origin)
```

``` csharp
public override long Seek(
    long offset,
    SeekOrigin origin
)
```

#### Parameters

  - offset  
    Type: [System.Int64](http://msdn2.microsoft.com/en-us/library/6yy583ek)  
    
    Byte offset relative to the origin parameter.

<!-- end list -->

  - origin  
    Type: [System.IO.SeekOrigin](http://msdn2.microsoft.com/en-us/library/883dhyx0)  
    
    A SeekOrigin indicating the reference point for the new position.

#### Return value

Type: [System.Int64](http://msdn2.microsoft.com/en-us/library/6yy583ek)  
The new position in the current stream.  

## See also

#### Reference

[ColumnStream class](dn334143\(v=exchg.10\).md)

[ColumnStream members](dn334190\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

