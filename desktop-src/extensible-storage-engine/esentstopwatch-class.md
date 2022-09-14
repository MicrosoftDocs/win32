---
description: "Learn more about: EsentStopwatch class"
title: EsentStopwatch class
TOCTitle: EsentStopwatch class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentStopwatch
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentstopwatch(v=EXCHG.10)
ms:contentKeyID: 55102933
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentStopwatch
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentStopwatch
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentStopwatch class

Provides a set of methods and properties that you can use to measure ESENT work statistics for a thread. If the current version of ESENT doesn't support [JetGetThreadStats(JET_THREADSTATS)](./vistaapi.jetgetthreadstats-method.md) then all ESENT statistics will be 0.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  Microsoft.Isam.Esent.Interop.EsentStopwatch  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Class EsentStopwatch
'Usage
Dim instance As EsentStopwatch
```

``` csharp
public class EsentStopwatch
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentStopwatch members](./esentstopwatch-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
