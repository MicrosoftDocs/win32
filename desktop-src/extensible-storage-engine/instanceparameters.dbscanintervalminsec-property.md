---
description: "Learn more about: InstanceParameters.DbScanIntervalMinSec property"
title: InstanceParameters.DbScanIntervalMinSec property 
TOCTitle: 'DbScanIntervalMinSec property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.DbScanIntervalMinSec
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.dbscanintervalminsec(v=EXCHG.10)
ms:contentKeyID: 55107436
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.DbScanIntervalMinSec
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_DbScanIntervalMinSec
- Microsoft.Isam.Esent.Interop.InstanceParameters.DbScanIntervalMinSec
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_DbScanIntervalMinSec
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.DbScanIntervalMinSec property

Gets or sets the minimum interval to repeat the database scan, in seconds.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property DbScanIntervalMinSec As Integer
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Integer

value = instance.DbScanIntervalMinSec

instance.DbScanIntervalMinSec = value
```

``` csharp
public int DbScanIntervalMinSec { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
