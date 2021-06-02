---
description: "Learn more about: SystemParameters.LegacyFileNames property"
title: SystemParameters.LegacyFileNames property 
TOCTitle: 'LegacyFileNames property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.LegacyFileNames
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.legacyfilenames(v=EXCHG.10)
ms:contentKeyID: 55104128
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.LegacyFileNames
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.get_LegacyFileNames
- Microsoft.Isam.Esent.Interop.SystemParameters.LegacyFileNames
- Microsoft.Isam.Esent.Interop.SystemParameters.set_LegacyFileNames
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.LegacyFileNames property

Gets or sets backwards compatibility with the file naming conventions of earlier releases of the database engine.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property LegacyFileNames As Integer
    Get
    Set
'Usage
Dim value As Integer

value = SystemParameters.LegacyFileNames

SystemParameters.LegacyFileNames = value
```

``` csharp
public static int LegacyFileNames { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
