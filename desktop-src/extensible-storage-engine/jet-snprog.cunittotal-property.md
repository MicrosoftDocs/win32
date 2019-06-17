---
title: JET_SNPROG.cunitTotal property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'cunitTotal property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_SNPROG.cunitTotal
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_snprog.cunittotal(v=EXCHG.10)
ms:contentKeyID: 55103955
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_SNPROG.cunitTotal
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SNPROG.set_cunitTotal
- Microsoft.Isam.Esent.Interop.JET_SNPROG.cunitTotal
- Microsoft.Isam.Esent.Interop.JET_SNPROG.get_cunitTotal
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SNPROG.cunitTotal property

Gets the number of work units that need to be completed. This value will always be bigger than or equal to cunitDone.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cunitTotal As Integer
    Get
    Friend Set
'Usage
Dim instance As JET_SNPROG
Dim value As Integer

value = instance.cunitTotal
```

``` csharp
public int cunitTotal { get; internal set; }
```

#### Property value

Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  

## See also

#### Reference

[JET_SNPROG class](dn351044\(v=exchg.10\).md)

[JET_SNPROG members](dn351084\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

