---
description: "Learn more about: InstanceParameters.EnableDBScanSerialization property"
title: InstanceParameters.EnableDBScanSerialization property 
TOCTitle: 'EnableDBScanSerialization property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.EnableDBScanSerialization
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.enabledbscanserialization(v=EXCHG.10)
ms:contentKeyID: 55103555
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.EnableDBScanSerialization
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_EnableDBScanSerialization
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_EnableDBScanSerialization
- Microsoft.Isam.Esent.Interop.InstanceParameters.EnableDBScanSerialization
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.EnableDBScanSerialization property

Gets or sets a value indicating whether database Maintenance serialization is enabled for databases sharing the same disk.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property EnableDBScanSerialization As Boolean
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Boolean

value = instance.EnableDBScanSerialization

instance.EnableDBScanSerialization = value
```

``` csharp
public bool EnableDBScanSerialization { get; set; }
```

#### Property value

Type: [System.Boolean](/dotnet/api/system.boolean)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
