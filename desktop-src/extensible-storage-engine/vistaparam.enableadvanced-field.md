---
description: "Learn more about: VistaParam.EnableAdvanced field"
title: VistaParam.EnableAdvanced field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: EnableAdvanced field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaParam.EnableAdvanced
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.vistaparam.enableadvanced(v=EXCHG.10)
ms:contentKeyID: 55104335
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.EnableAdvanced
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.EnableAdvanced
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# VistaParam.EnableAdvanced field

This parameter is used to control when the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with [Configuration](./vistaparam.configuration-field.md) to prevent some system parameters from being set away from the selected configuration's defaults.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const EnableAdvanced As JET_param
'Usage
Dim value As JET_param

value = VistaParam.EnableAdvanced
```

``` csharp
public const JET_param EnableAdvanced
```

## See also

#### Reference

[VistaParam class](./vistaparam-class.md)

[VistaParam members](./vistaparam-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
