---
title: Server2003Grbits.ForwardOnly field (Microsoft.Isam.Esent.Interop.Server2003)
TOCTitle: ForwardOnly field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.ForwardOnly
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.server2003.server2003grbits.forwardonly(v=EXCHG.10)
ms:contentKeyID: 55104214
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.ForwardOnly
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.ForwardOnly
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Server2003Grbits.ForwardOnly field

This option requests that the temporary table only be created if the temporary table manager can use the implementation optimized for intermediate query results. If any characteristic of the temporary table would prevent the use of this optimization then the operation will fail with JET\_errCannotMaterializeForwardOnlySort. A side effect of this option is to allow the temporary table to contain records with duplicate index keys. See [Unique](hh558517\(v=exchg.10\).md) for more information.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Server2003](hh557147\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const ForwardOnly As TempTableGrbit
'Usage
Dim value As TempTableGrbit

value = Server2003Grbits.ForwardOnly
```

``` csharp
public const TempTableGrbit ForwardOnly
```

## See also

#### Reference

[Server2003Grbits class](dn351281\(v=exchg.10\).md)

[Server2003Grbits members](dn351200\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Server2003 namespace](hh557147\(v=exchg.10\).md)

