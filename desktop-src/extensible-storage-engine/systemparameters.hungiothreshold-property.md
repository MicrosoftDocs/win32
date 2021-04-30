---
description: "Learn more about: SystemParameters.HungIOThreshold property"
title: SystemParameters.HungIOThreshold property 
TOCTitle: 'HungIOThreshold property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.HungIOThreshold
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.hungiothreshold(v=EXCHG.10)
ms:contentKeyID: 55104041
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.HungIOThreshold
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.set_HungIOThreshold
- Microsoft.Isam.Esent.Interop.SystemParameters.HungIOThreshold
- Microsoft.Isam.Esent.Interop.SystemParameters.get_HungIOThreshold
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.HungIOThreshold property

Gets or sets the threshold for what is considered a hung IO that should be acted upon.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property HungIOThreshold As Integer
    Get
    Set
'Usage
Dim value As Integer

value = SystemParameters.HungIOThreshold

SystemParameters.HungIOThreshold = value
```

``` csharp
public static int HungIOThreshold { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
