---
description: "Learn more about: SystemParameters.DatabasePageSize property"
title: SystemParameters.DatabasePageSize property 
TOCTitle: 'DatabasePageSize property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.DatabasePageSize
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters.databasepagesize(v=EXCHG.10)
ms:contentKeyID: 55104038
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.DatabasePageSize
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.get_DatabasePageSize
- Microsoft.Isam.Esent.Interop.SystemParameters.set_DatabasePageSize
- Microsoft.Isam.Esent.Interop.SystemParameters.DatabasePageSize
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.DatabasePageSize property

Gets or sets the size of the database pages, in bytes.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property DatabasePageSize As Integer
    Get
    Set
'Usage
Dim value As Integer

value = SystemParameters.DatabasePageSize

SystemParameters.DatabasePageSize = value
```

``` csharp
public static int DatabasePageSize { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[SystemParameters members](./systemparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
