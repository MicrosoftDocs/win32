---
title: VistaGrbits.RecoveryWithoutUndo field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: RecoveryWithoutUndo field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.RecoveryWithoutUndo
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.vistagrbits.recoverywithoutundo(v=EXCHG.10)
ms:contentKeyID: 55104427
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.RecoveryWithoutUndo
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.VistaGrbits.RecoveryWithoutUndo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# VistaGrbits.RecoveryWithoutUndo field

Perform recovery, but halt at the Undo phase. Allows whatever logs are present to be replayed, then later additional logs can be copied and replayed.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const RecoveryWithoutUndo As InitGrbit
'Usage
Dim value As InitGrbit

value = VistaGrbits.RecoveryWithoutUndo
```

``` csharp
public const InitGrbit RecoveryWithoutUndo
```

## See also

#### Reference

[VistaGrbits class](dn335350\(v=exchg.10\).md)

[VistaGrbits members](dn351282\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

