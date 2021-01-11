---
description: "Learn more about: EsentVersion.SupportsUnicodePaths property"
title: EsentVersion.SupportsUnicodePaths property 
TOCTitle: 'SupportsUnicodePaths property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.EsentVersion.SupportsUnicodePaths
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentversion.supportsunicodepaths(v=EXCHG.10)
ms:contentKeyID: 55103182
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentVersion.SupportsUnicodePaths
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentVersion.get_SupportsUnicodePaths
- Microsoft.Isam.Esent.Interop.EsentVersion.SupportsUnicodePaths
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentVersion.SupportsUnicodePaths property

Gets a value that indicates whether the current version of ESENT can use non-ASCII paths to access databases.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared ReadOnly Property SupportsUnicodePaths As Boolean
    Get
'Usage
Dim value As Boolean

value = EsentVersion.SupportsUnicodePaths
```

``` csharp
public static bool SupportsUnicodePaths { get; }
```

#### Property value

Type: [System.Boolean](/dotnet/api/system.boolean)  

## See also

#### Reference

[EsentVersion class](./esentversion-class.md)

[EsentVersion members](./esentversion-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
