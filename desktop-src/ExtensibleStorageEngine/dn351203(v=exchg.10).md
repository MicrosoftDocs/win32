---
title: Server2003Grbits.EnumerateIgnoreUserDefinedDefault field (Microsoft.Isam.Esent.Interop.Server2003)
TOCTitle: EnumerateIgnoreUserDefinedDefault field
ms:assetid: F:Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.EnumerateIgnoreUserDefinedDefault
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.server2003.server2003grbits.enumerateignoreuserdefineddefault(v=EXCHG.10)
ms:contentKeyID: 55104099
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.EnumerateIgnoreUserDefinedDefault
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Server2003.Server2003Grbits.EnumerateIgnoreUserDefinedDefault
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Server2003Grbits.EnumerateIgnoreUserDefinedDefault field

If a given column is not present in the record and it has a user defined default value then no column value will be returned. This option will prevent the callback that computes the user defined default value for the column from being called when enumerating the values for that column.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Server2003](hh557147\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Const EnumerateIgnoreUserDefinedDefault As EnumerateColumnsGrbit
'Usage
Dim value As EnumerateColumnsGrbit

value = Server2003Grbits.EnumerateIgnoreUserDefinedDefault
```

``` csharp
public const EnumerateColumnsGrbit EnumerateIgnoreUserDefinedDefault
```

## Remarks

This option is only available for Windows Server 2003 SP1 and later operating systems.

## See also

#### Reference

[Server2003Grbits class](dn351281\(v=exchg.10\).md)

[Server2003Grbits members](dn351200\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Server2003 namespace](hh557147\(v=exchg.10\).md)

