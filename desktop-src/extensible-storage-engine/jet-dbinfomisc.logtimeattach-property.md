---
description: "Learn more about: JET_DBINFOMISC.logtimeAttach property"
title: JET_DBINFOMISC.logtimeAttach property 
TOCTitle: 'logtimeAttach property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeAttach
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.logtimeattach(v=EXCHG.10)
ms:contentKeyID: 39510861
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeAttach
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_logtimeAttach
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeAttach
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_logtimeAttach
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.logtimeAttach property

Gets the time when the database was attached.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property logtimeAttach As JET_LOGTIME
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_LOGTIME

value = instance.logtimeAttach
```

``` csharp
public JET_LOGTIME logtimeAttach { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_LOGTIME](./jet-logtime-structure2.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
