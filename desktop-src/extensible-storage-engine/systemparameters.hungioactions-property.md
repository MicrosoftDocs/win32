---
description: "Learn more about: SystemParameters.HungIOActions property"
title: SystemParameters.HungIOActions property 
TOCTitle: 'HungIOActions property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.HungIOActions
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.hungioactions(v=EXCHG.10)
ms:contentKeyID: 55104126
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.HungIOActions
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.get_HungIOActions
- Microsoft.Isam.Esent.Interop.SystemParameters.HungIOActions
- Microsoft.Isam.Esent.Interop.SystemParameters.set_HungIOActions
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.HungIOActions property

Gets or sets the set of actions to be taken on IOs that appear hung.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property HungIOActions As Integer
    Get
    Set
'Usage
Dim value As Integer

value = SystemParameters.HungIOActions

SystemParameters.HungIOActions = value
```

``` csharp
public static int HungIOActions { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
