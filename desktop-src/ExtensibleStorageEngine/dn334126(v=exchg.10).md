---
title: BytesColumnValue.Length property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Length property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.BytesColumnValue.Length
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.bytescolumnvalue.length(v=EXCHG.10)
ms:contentKeyID: 55107234
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.BytesColumnValue.Length
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.BytesColumnValue.Length
- Microsoft.Isam.Esent.Interop.BytesColumnValue.get_Length
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# BytesColumnValue.Length property

Gets the byte length of a column value, which is zero if column is null, otherwise matches the actual length of the byte array.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Overrides ReadOnly Property Length As Integer
    Get
'Usage
Dim instance As BytesColumnValue
Dim value As Integer

value = instance.Length
```

``` csharp
public override int Length { get; }
```

#### Property value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[BytesColumnValue class](dn334170\(v=exchg.10\).md)

[BytesColumnValue members](dn334118\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

