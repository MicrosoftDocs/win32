---
description: "Learn more about: IndexInfo.Keys property"
title: IndexInfo.Keys property 
TOCTitle: 'Keys property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.IndexInfo.Keys
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.indexinfo.keys(v=EXCHG.10)
ms:contentKeyID: 55103265
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IndexInfo.Keys
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IndexInfo.Keys
- Microsoft.Isam.Esent.Interop.IndexInfo.get_Keys
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IndexInfo.Keys property

Gets the number of unique keys in the index. This value is not current and is only is updated by Api.JetComputeStats.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property Keys As Integer
    Get
'Usage
Dim instance As IndexInfo
Dim value As Integer

value = instance.Keys
```

``` csharp
public int Keys { get; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[IndexInfo class](./indexinfo-class.md)

[IndexInfo members](./indexinfo-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
