---
description: "Learn more about: InstanceParameters.WaypointLatency property"
title: InstanceParameters.WaypointLatency property 
TOCTitle: 'WaypointLatency property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.WaypointLatency
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.waypointlatency(v=EXCHG.10)
ms:contentKeyID: 55103325
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.WaypointLatency
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_WaypointLatency
- Microsoft.Isam.Esent.Interop.InstanceParameters.WaypointLatency
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_WaypointLatency
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.WaypointLatency property

Gets or sets a the number of logs that esent will defer database flushes for. This can be used to increase database recoverability if failures cause logfiles to be lost. Supported on Windows 7 and up. Ignored on Windows XP, Windows Server 2003, Windows Vista and Windows Server 2008.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property WaypointLatency As Integer
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Integer

value = instance.WaypointLatency

instance.WaypointLatency = value
```

``` csharp
public int WaypointLatency { get; set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[InstanceParameters class](./instanceparameters-class.md)

[InstanceParameters members](./instanceparameters-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
