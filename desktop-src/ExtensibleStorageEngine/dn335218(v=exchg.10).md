---
title: JET_OBJECTLIST.tableid property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'tableid property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.tableid
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_objectlist.tableid(v=EXCHG.10)
ms:contentKeyID: 55103778
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.tableid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.set_tableid
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.tableid
- Microsoft.Isam.Esent.Interop.JET_OBJECTLIST.get_tableid
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_OBJECTLIST.tableid property

Gets tableid of the temporary table. This should be closed when the table is no longer needed.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property tableid As JET_TABLEID
    Get
    Friend Set
'Usage
Dim instance As JET_OBJECTLIST
Dim value As JET_TABLEID

value = instance.tableid
```

``` csharp
public JET_TABLEID tableid { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET\_TABLEID](hh566310\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_OBJECTLIST class](dn335206\(v=exchg.10\).md)

[JET\_OBJECTLIST members](dn335204\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

