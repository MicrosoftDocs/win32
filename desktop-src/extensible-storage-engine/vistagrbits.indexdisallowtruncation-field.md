---
title: VistaGrbits.IndexDisallowTruncation field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: IndexDisallowTruncation field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.IndexDisallowTruncation
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.vistagrbits.indexdisallowtruncation(v=EXCHG.10)
ms:contentKeyID: 55104424
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.IndexDisallowTruncation
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.IndexDisallowTruncation
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# VistaGrbits.IndexDisallowTruncation field

Specifying this flag will cause any update to the index that would result in a truncated key to fail with [KeyTruncated](hh564840\(v=exchg.10\).md). Otherwise, keys will be silently truncated.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const IndexDisallowTruncation As CreateIndexGrbit
'Usage
Dim value As CreateIndexGrbit

value = VistaGrbits.IndexDisallowTruncation
```

``` csharp
public const CreateIndexGrbit IndexDisallowTruncation
```

## See also

#### Reference

[VistaGrbits class](dn335350\(v=exchg.10\).md)

[VistaGrbits members](dn351282\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

