---
title: EsentStopwatch.ThreadStats property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'ThreadStats property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.EsentStopwatch.ThreadStats
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentstopwatch.threadstats(v=EXCHG.10)
ms:contentKeyID: 55102996
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentStopwatch.ThreadStats
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentStopwatch.get_ThreadStats
- Microsoft.Isam.Esent.Interop.EsentStopwatch.set_ThreadStats
- Microsoft.Isam.Esent.Interop.EsentStopwatch.ThreadStats
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentStopwatch.ThreadStats property

Gets the total ESENT work stats measured by the current instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property ThreadStats As JET_THREADSTATS
    Get
    Private Set
'Usage
Dim instance As EsentStopwatch
Dim value As JET_THREADSTATS

value = instance.ThreadStats
```

``` csharp
public JET_THREADSTATS ThreadStats { get; private set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.Vista.JET\_THREADSTATS](hh578565\(v=exchg.10\).md)  

## See also

#### Reference

[EsentStopwatch class](dn334867\(v=exchg.10\).md)

[EsentStopwatch members](dn334924\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

