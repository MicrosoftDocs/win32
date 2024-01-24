---
description: "Learn more about: SystemParameters.KeyMost property"
title: SystemParameters.KeyMost property 
TOCTitle: 'KeyMost property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.KeyMost
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.keymost(v=EXCHG.10)
ms:contentKeyID: 55104043
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.KeyMost
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.get_KeyMost
- Microsoft.Isam.Esent.Interop.SystemParameters.KeyMost
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.KeyMost property

Gets the maximum key size. This depends on the Esent version and database page size.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared ReadOnly Property KeyMost As Integer
    Get
'Usage
Dim value As Integer

value = SystemParameters.KeyMost
```

``` csharp
public static int KeyMost { get; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
