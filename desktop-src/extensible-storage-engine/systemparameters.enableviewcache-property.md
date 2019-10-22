---
title: SystemParameters.EnableViewCache property 
TOCTitle: 'EnableViewCache property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.EnableViewCache
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.systemparameters.enableviewcache(v=EXCHG.10)
ms:contentKeyID: 55104120
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableViewCache
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableViewCache
- Microsoft.Isam.Esent.Interop.SystemParameters.set_EnableViewCache
- Microsoft.Isam.Esent.Interop.SystemParameters.get_EnableViewCache
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.EnableViewCache property

Gets or sets a value indicating whether the database engine should use memory mapped file I/O for database files.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property EnableViewCache As Boolean
    Get
    Set
'Usage
Dim value As Boolean

value = SystemParameters.EnableViewCache

SystemParameters.EnableViewCache = value
```

``` csharp
public static bool EnableViewCache { get; set; }
```

#### Property value

Type: [System.Boolean](https://docs.microsoft.com/dotnet/api/system.boolean?redirectedfrom=MSDN)  

## See also

#### Reference

[SystemParameters class](dn351139\(v=exchg.10\).md)

[SystemParameters members](dn351207\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

