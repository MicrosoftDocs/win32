---
title: ColumnValueOfStruct(T).Length property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Length property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.Length
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Dn334225(v=EXCHG.10)
ms:contentKeyID: 55101009
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.Length
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.get_Length
- Microsoft.Isam.Esent.Interop.ColumnValueOfStruct`1.Length
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# ColumnValueOfStruct\<T\>.Length property

Gets the byte length of a column value, which is zero if column is null, otherwise it matches the Size for this fixed-size column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides ReadOnly Property Length As Integer
    Get
'Usage
Dim instance As ColumnValueOfStruct
Dim value As Integer

value = instance.Length
```

``` csharp
public override int Length { get; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[ColumnValueOfStruct\<T\> class](dn334171\(v=exchg.10\).md)

[ColumnValueOfStruct\<T\> members](dn334217\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

