---
description: "Learn more about: VistaParam.CachedClosedTables field"
title: VistaParam.CachedClosedTables field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: CachedClosedTables field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaParam.CachedClosedTables
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.vistaparam.cachedclosedtables(v=EXCHG.10)
ms:contentKeyID: 55104337
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.CachedClosedTables
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.CachedClosedTables
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# VistaParam.CachedClosedTables field

This parameter controls the number of B+ Tree resources cached by the instance after the tables they represent have been closed by the application. Large values for this parameter will cause the database engine to use more memory but will increase the speed with which a large number of tables can be opened randomly by the application. This is useful for applications that have a schema with a very large number of tables.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const CachedClosedTables As JET_param
'Usage
Dim value As JET_param

value = VistaParam.CachedClosedTables
```

``` csharp
public const JET_param CachedClosedTables
```

## See also

#### Reference

[VistaParam class](./vistaparam-class.md)

[VistaParam members](./vistaparam-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
