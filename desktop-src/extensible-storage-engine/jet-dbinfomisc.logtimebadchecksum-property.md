---
description: "Learn more about: JET_DBINFOMISC.logtimeBadChecksum property"
title: JET_DBINFOMISC.logtimeBadChecksum property 
TOCTitle: 'logtimeBadChecksum property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeBadChecksum
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.logtimebadchecksum(v=EXCHG.10)
ms:contentKeyID: 39516801
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeBadChecksum
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_logtimeBadChecksum
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeBadChecksum
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_logtimeBadChecksum
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.logtimeBadChecksum property

Gets the last time a non-correctable checksum error was found.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property logtimeBadChecksum As JET_LOGTIME
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_LOGTIME

value = instance.logtimeBadChecksum
```

``` csharp
public JET_LOGTIME logtimeBadChecksum { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_LOGTIME](./jet-logtime-structure2.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
