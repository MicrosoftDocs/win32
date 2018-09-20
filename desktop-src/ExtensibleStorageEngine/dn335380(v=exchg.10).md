---
title: VistaParam.EnableAdvanced field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: EnableAdvanced field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaParam.EnableAdvanced
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.vistaparam.enableadvanced(v=EXCHG.10)
ms:contentKeyID: 55104335
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
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

This parameter is used to control when the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with [Configuration](dn335289\(v=exchg.10\).md) to prevent some system parameters from being set away from the selected configuration's defaults.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
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

[VistaParam class](dn335284\(v=exchg.10\).md)

[VistaParam members](dn335372\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

