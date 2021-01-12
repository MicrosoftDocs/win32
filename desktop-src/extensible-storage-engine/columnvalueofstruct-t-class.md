---
description: "Learn more about: ColumnValueOfStruct<T> class"
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
  [Microsoft.Isam.Esent.Interop.ColumnValue](./columnvalue-class.md)  
    Microsoft.Isam.Esent.Interop.ColumnValueOfStruct\<T\>  
      

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

[ColumnValueOfStruct\<T\> members](./columnvalueofstruct-t-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [Microsoft.Isam.Esent.Interop.ColumnValue](./columnvalue-class.md)  
    Microsoft.Isam.Esent.Interop.ColumnValueOfStruct\<T\>  
      [Microsoft.Isam.Esent.Interop.BoolColumnValue](./boolcolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.ByteColumnValue](./bytecolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.DateTimeColumnValue](./datetimecolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.DoubleColumnValue](./doublecolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.FloatColumnValue](./floatcolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.GuidColumnValue](./guidcolumnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.Int16ColumnValue](./int16columnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.Int32ColumnValue](./int32columnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.Int64ColumnValue](./int64columnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.UInt16ColumnValue](./uint16columnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.UInt32ColumnValue](./uint32columnvalue-class.md)  
      [Microsoft.Isam.Esent.Interop.UInt64ColumnValue](./uint64columnvalue-class.md)