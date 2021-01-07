---
description: "Learn more about: JET_DBINFOMISC.logtimeGenMaxCreate property"
title: JET_DBINFOMISC.logtimeGenMaxCreate property 
TOCTitle: 'logtimeGenMaxCreate property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeGenMaxCreate
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_dbinfomisc.logtimegenmaxcreate(v=EXCHG.10)
ms:contentKeyID: 39510493
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeGenMaxCreate
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.logtimeGenMaxCreate
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.set_logtimeGenMaxCreate
- Microsoft.Isam.Esent.Interop.JET_DBINFOMISC.get_logtimeGenMaxCreate
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_DBINFOMISC.logtimeGenMaxCreate property

Gets the creation time of the [genMaxRequired](./jet-dbinfomisc.genmaxrequired-property.md) logfile.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property logtimeGenMaxCreate As JET_LOGTIME
    Get
    Friend Set
'Usage
Dim instance As JET_DBINFOMISC
Dim value As JET_LOGTIME

value = instance.logtimeGenMaxCreate
```

``` csharp
public JET_LOGTIME logtimeGenMaxCreate { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_LOGTIME](./jet-logtime-structure2.md)  

## See also

#### Reference

[JET_DBINFOMISC class](./jet-dbinfomisc-class.md)

[JET_DBINFOMISC members](./jet-dbinfomisc-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
