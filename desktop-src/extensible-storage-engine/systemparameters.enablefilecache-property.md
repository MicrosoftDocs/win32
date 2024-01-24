---
description: "Learn more about: SystemParameters.EnableFileCache property"
title: SystemParameters.EnableFileCache property 
TOCTitle: 'EnableFileCache property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.EnableFileCache
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.enablefilecache(v=EXCHG.10)
ms:contentKeyID: 55104039
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableFileCache
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableFileCache
- Microsoft.Isam.Esent.Interop.SystemParameters.set_EnableFileCache
- Microsoft.Isam.Esent.Interop.SystemParameters.get_EnableFileCache
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.EnableFileCache property

Gets or sets a value indicating whether the database engine should use the OS file cache for all managed files.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property EnableFileCache As Boolean
    Get
    Set
'Usage
Dim value As Boolean

value = SystemParameters.EnableFileCache

SystemParameters.EnableFileCache = value
```

``` csharp
public static bool EnableFileCache { get; set; }
```

#### Property value

Type: [System.Boolean](/dotnet/api/system.boolean)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
