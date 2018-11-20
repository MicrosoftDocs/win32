---
title: SystemParameters.EnableAdvanced property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'EnableAdvanced property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.SystemParameters.EnableAdvanced
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.systemparameters.enableadvanced(v=EXCHG.10)
ms:contentKeyID: 55104116
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableAdvanced
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.SystemParameters.set_EnableAdvanced
- Microsoft.Isam.Esent.Interop.SystemParameters.get_EnableAdvanced
- Microsoft.Isam.Esent.Interop.SystemParameters.EnableAdvanced
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# SystemParameters.EnableAdvanced property

Gets or sets a value indicating whether the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with [Configuration](dn351218\(v=exchg.10\).md) to prevent some system parameters from being set away from the selected configuration's defaults. Supported on Windows Vista and up. Ignored on Windows XP and Windows Server 2003.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Property EnableAdvanced As Boolean
    Get
    Set
'Usage
Dim value As Boolean

value = SystemParameters.EnableAdvanced

SystemParameters.EnableAdvanced = value
```

``` csharp
public static bool EnableAdvanced { get; set; }
```

#### Property value

Type: [System.Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)  

## See also

#### Reference

[SystemParameters class](dn351139\(v=exchg.10\).md)

[SystemParameters members](dn351207\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

