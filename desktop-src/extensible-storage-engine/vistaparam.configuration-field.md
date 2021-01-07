---
description: "Learn more about: VistaParam.Configuration field"
title: VistaParam.Configuration field (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: Configuration field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Vista.VistaParam.Configuration
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.vistaparam.configuration(v=EXCHG.10)
ms:contentKeyID: 55104229
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.Configuration
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.VistaParam.Configuration
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# VistaParam.Configuration field

This parameter exposes multiple sets of default values for the entire set of system parameters. When this parameter is set to a specific configuration, all system parameter values are reset to their default values for that configuration. If the configuration is set for a specific instance then global system parameters will not be reset to their default values. Small Configuration (0): The database engine is optimized for memory use. Legacy Configuration (1): The database engine has its traditional defaults.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const Configuration As JET_param
'Usage
Dim value As JET_param

value = VistaParam.Configuration
```

``` csharp
public const JET_param Configuration
```

## See also

#### Reference

[VistaParam class](./vistaparam-class.md)

[VistaParam members](./vistaparam-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
