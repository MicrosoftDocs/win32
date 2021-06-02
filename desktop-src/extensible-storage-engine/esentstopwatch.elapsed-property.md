---
description: "Learn more about: EsentStopwatch.Elapsed property"
title: EsentStopwatch.Elapsed property 
TOCTitle: 'Elapsed property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.EsentStopwatch.Elapsed
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentstopwatch.elapsed(v=EXCHG.10)
ms:contentKeyID: 55102997
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentStopwatch.Elapsed
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentStopwatch.Elapsed
- Microsoft.Isam.Esent.Interop.EsentStopwatch.set_Elapsed
- Microsoft.Isam.Esent.Interop.EsentStopwatch.get_Elapsed
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentStopwatch.Elapsed property

Gets the total elapsed time measured by the current instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property Elapsed As TimeSpan
    Get
    Private Set
'Usage
Dim instance As EsentStopwatch
Dim value As TimeSpan

value = instance.Elapsed
```

``` csharp
public TimeSpan Elapsed { get; private set; }
```

#### Property value

Type: [System.TimeSpan](/dotnet/api/system.timespan)  

## See also

#### Reference

[EsentStopwatch class](./esentstopwatch-class.md)

[EsentStopwatch members](./esentstopwatch-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
