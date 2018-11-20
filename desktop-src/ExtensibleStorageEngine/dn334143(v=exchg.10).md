---
title: ColumnStream class (Microsoft.Isam.Esent.Interop)
TOCTitle: ColumnStream class
ms:assetid: T:Microsoft.Isam.Esent.Interop.ColumnStream
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.columnstream(v=EXCHG.10)
ms:contentKeyID: 55100939
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnStream
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnStream
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnStream class

This class provides a streaming interface to a long-value column (i.e. a column of type [LongBinary](hh577895\(v=exchg.10\).md) or [LongText](hh577895\(v=exchg.10\).md)).

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.MarshalByRefObject](http://msdn2.microsoft.com/en-us/library/w4302s1f)  
    [System.IO.Stream](http://msdn2.microsoft.com/en-us/library/8f86tw9e)  
      Microsoft.Isam.Esent.Interop.ColumnStream  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Class ColumnStream _
    Inherits Stream
'Usage
Dim instance As ColumnStream
```

``` csharp
public class ColumnStream : Stream
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[ColumnStream members](dn334190\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

