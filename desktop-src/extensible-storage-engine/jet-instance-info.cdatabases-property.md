---
description: "Learn more about: JET_INSTANCE_INFO.cDatabases property"
title: JET_INSTANCE_INFO.cDatabases property 
TOCTitle: 'cDatabases property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.cDatabases
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_instance_info.cdatabases(v=EXCHG.10)
ms:contentKeyID: 55103699
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.cDatabases
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.set_cDatabases
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.get_cDatabases
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.cDatabases
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INSTANCE_INFO.cDatabases property

Gets the number of databases that are attached to the database instance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cDatabases As Integer
    Get
    Private Set
'Usage
Dim instance As JET_INSTANCE_INFO
Dim value As Integer

value = instance.cDatabases
```

``` csharp
public int cDatabases { get; private set; }
```

#### Property value

Type: [System.Int32](/dotnet/api/system.int32)  

## See also

#### Reference

[JET_INSTANCE_INFO class](./jet-instance-info-class.md)

[JET_INSTANCE_INFO members](./jet-instance-info-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
