---
description: "Learn more about: Windows7Param.WaypointLatency field"
title: Windows7Param.WaypointLatency field (Microsoft.Isam.Esent.Interop.Windows7)
TOCTitle: WaypointLatency field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Windows7.Windows7Param.WaypointLatency
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows7.windows7param.waypointlatency(v=EXCHG.10)
ms:contentKeyID: 55104440
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows7.Windows7Param.WaypointLatency
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows7.Windows7Param.WaypointLatency
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Windows7Param.WaypointLatency field

This parameter sets the number of logs that esent will defer database flushes for. This can be used to increase database recoverability if failures cause logfiles to be lost.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows7](./microsoft.isam.esent.interop.windows7-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const WaypointLatency As JET_param
'Usage
Dim value As JET_param

value = Windows7Param.WaypointLatency
```

``` csharp
public const JET_param WaypointLatency
```

## See also

#### Reference

[Windows7Param class](./windows7param-class.md)

[Windows7Param members](./windows7param-members.md)

[Microsoft.Isam.Esent.Interop.Windows7 namespace](./microsoft.isam.esent.interop.windows7-namespace.md)
