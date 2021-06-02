---
description: "Learn more about: InstanceParameters.CachePriority property"
title: InstanceParameters.CachePriority property 
TOCTitle: 'CachePriority property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.CachePriority
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.cachepriority(v=EXCHG.10)
ms:contentKeyID: 55107435
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.CachePriority
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.CachePriority
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_CachePriority
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_CachePriority
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.CachePriority property

Gets or sets the per-instance property for relative cache priorities (default = 100).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property CachePriority As Integer
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Integer

value = instance.CachePriority

instance.CachePriority = value
```

``` csharp
public int CachePriority { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
