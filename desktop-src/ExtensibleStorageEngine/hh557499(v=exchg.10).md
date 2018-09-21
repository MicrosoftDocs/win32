---
title: JET_LS structure (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_LS structure
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_LS
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_ls(v=EXCHG.10)
ms:contentKeyID: 39510760
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_LS
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_LS
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_LS structure

Local storage for an ESENT handle. Used by [JetGetLS(JET\_SESID, JET\_TABLEID, JET\_LS, LsGrbit)](dn292177\(v=exchg.10\).md) and [JetSetLS(JET\_SESID, JET\_TABLEID, JET\_LS, LsGrbit)](dn334015\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Structure JET_LS _
    Implements IEquatable(Of JET_LS), IFormattable
'Usage
Dim instance As JET_LS
```

``` csharp
public struct JET_LS : IEquatable<JET_LS>, 
    IFormattable
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[JET\_LS members](hh596466\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

