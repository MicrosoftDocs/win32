---
description: "Learn more about: SystemParameters.CacheSizeMin property"
title: SystemParameters.CacheSizeMin property 
TOCTitle: 'CacheSizeMin property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.CacheSizeMin
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.cachesizemin(v=EXCHG.10)
ms:contentKeyID: 55104113
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.CacheSizeMin
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.get_CacheSizeMin
- Microsoft.Isam.Esent.Interop.SystemParameters.CacheSizeMin
- Microsoft.Isam.Esent.Interop.SystemParameters.set_CacheSizeMin
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.CacheSizeMin property

Gets or sets the minimum size of the database page cache, in database pages.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property CacheSizeMin As Integer
    Get
    Set
'Usage
Dim value As Integer

value = SystemParameters.CacheSizeMin

SystemParameters.CacheSizeMin = value
```

``` csharp
public static int CacheSizeMin { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
