---
description: "Learn more about: InstanceParameters.PrereadIOMax property"
title: InstanceParameters.PrereadIOMax property 
TOCTitle: 'PrereadIOMax property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.PrereadIOMax
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.prereadiomax(v=EXCHG.10)
ms:contentKeyID: 55103559
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.PrereadIOMax
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.PrereadIOMax
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_PrereadIOMax
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_PrereadIOMax
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.PrereadIOMax property

Gets or sets the maximum number of I/O operations dispatched for a given purpose.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property PrereadIOMax As Integer
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Integer

value = instance.PrereadIOMax

instance.PrereadIOMax = value
```

``` csharp
public int PrereadIOMax { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
