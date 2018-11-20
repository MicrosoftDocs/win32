---
title: JET_DBINFOMISC.lgposConsistent property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'lgposConsistent property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.lgposConsistent
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_dbinfomisc.lgposconsistent(v=EXCHG.10)
ms:contentKeyID: 39516221
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.lgposConsistent
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_lgposConsistent
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.lgposConsistent
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_lgposConsistent
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_DBINFOMISC.lgposConsistent property

Gets the lgpos when the database was made consistent. This value is null if the database is inconsistent.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property lgposConsistent As JET_LGPOS
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_LGPOS

value = instance.lgposConsistent
```

``` csharp
public JET_LGPOS lgposConsistent { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET\_LGPOS](hh578063\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_DBINFOMISC class](hh538867\(v=exchg.10\).md)

[JET\_DBINFOMISC members](hh566148\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

