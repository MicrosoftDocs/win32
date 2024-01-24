---
description: "Learn more about: ColumnValueOfStruct<T>.CheckDataCount method"
title: ColumnValueOfStruct(T).CheckDataCount method 
TOCTitle: 'CheckDataCount method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.CheckDataCount(System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/Dn334178(v=EXCHG.10)
ms:contentKeyID: 55100977
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.CheckDataCount
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.CheckDataCount
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnValueOfStruct\<T\>.CheckDataCount method

Make sure the retrieved data is exactly the size needed for the structure. An exception is thrown if there is a mismatch.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected Sub CheckDataCount ( _
    count As Integer _
)
'Usage
Dim count As Integer

Me.CheckDataCount(count)
```

``` csharp
protected void CheckDataCount(
    int count
)
```

#### Parameters

  - count  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The size of the retrieved data.

## See also

#### Reference

[ColumnValueOfStruct\<T\> class](./columnvalueofstruct-t-class.md)

[ColumnValueOfStruct\<T\> members](./columnvalueofstruct-t-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
