---
title: ColumnValueOfStruct(T) class
TOCTitle: ColumnValueOfStruct(T) class
ms:assetid: T:Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1
ms:mtpsurl: https://msdn.microsoft.com/library/Dn334171(v=EXCHG.10)
ms:contentKeyID: 55100962
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnValueOfStruct\<T\> class

Set a column of a struct type (e.g. Int32/Guid).

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [Microsoft.Isam.Esent.Interop.ColumnValue](dn334206\(v=exchg.10\).md)  
    Microsoft.Isam.Esent.Interop.ColumnValueOfStruct\<T\>  
      

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public MustInherit Class ColumnValueOfStruct(Of T As {Structure, New, IEquatable(Of T)}) _
    Inherits ColumnValue
'Usage
Dim instance As ColumnValueOfStruct(Of T)
```

``` csharp
public abstract class ColumnValueOfStruct<T> : ColumnValue
where T : struct, new(), IEquatable<T>
```

#### Type parameters

  - T  
    Type to set.

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[ColumnValueOfStruct\<T\> members](dn334217\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [Microsoft.Isam.Esent.Interop.ColumnValue](dn334206\(v=exchg.10\).md)  
    Microsoft.Isam.Esent.Interop.ColumnValueOfStruct\<T\>  
      [Microsoft.Isam.Esent.Interop.BoolColumnValue](dn334148\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.ByteColumnValue](dn334109\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.DateTimeColumnValue](dn334238\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.DoubleColumnValue](dn273972\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.FloatColumnValue](dn350880\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.GuidColumnValue](dn350902\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.Int16ColumnValue](dn351017\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.Int32ColumnValue](dn350992\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.Int64ColumnValue](dn351016\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.UInt16ColumnValue](dn351247\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.UInt32ColumnValue](dn351251\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.UInt64ColumnValue](dn351190\(v=exchg.10\).md)