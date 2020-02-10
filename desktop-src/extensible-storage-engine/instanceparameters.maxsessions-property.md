---
title: InstanceParameters.MaxSessions property 
TOCTitle: 'MaxSessions property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.InstanceParameters.MaxSessions
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instanceparameters.maxsessions(v=EXCHG.10)
ms:contentKeyID: 55103557
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.InstanceParameters.MaxSessions
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.InstanceParameters.MaxSessions
- Microsoft.Isam.Esent.Interop.InstanceParameters.get_MaxSessions
- Microsoft.Isam.Esent.Interop.InstanceParameters.set_MaxSessions
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# InstanceParameters.MaxSessions property

Gets or sets the number of sessions resources reserved for this instance. A session resource directly corresponds to a JET_SESID.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property MaxSessions As Integer
    Get
    Set
'Usage
Dim instance As InstanceParameters
Dim value As Integer

value = instance.MaxSessions

instance.MaxSessions = value
```

``` csharp
public int MaxSessions { get; set; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[InstanceParameters class](dn350942\(v=exchg.10\).md)

[InstanceParameters members](dn350943\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

