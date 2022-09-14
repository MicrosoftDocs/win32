---
description: "Learn more about: JET_RETRIEVECOLUMN.pvData property"
title: JET_RETRIEVECOLUMN.pvData property 
TOCTitle: 'pvData property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.pvData
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_retrievecolumn.pvdata(v=EXCHG.10)
ms:contentKeyID: 55103883
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.pvData
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.get_pvData
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.set_pvData
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.pvData
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_RETRIEVECOLUMN.pvData property

Gets or sets the buffer that will store data that is retrieved from the column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property pvData As Byte()
    Get
    Set
'Usage
Dim instance As JET_RETRIEVECOLUMN
Dim value As Byte()

value = instance.pvData

instance.pvData = value
```

``` csharp
public byte[] pvData { get; set; }
```

#### Property value

Type: \[\]  

## See also

#### Reference

[JET_RETRIEVECOLUMN class](./jet-retrievecolumn-class.md)

[JET_RETRIEVECOLUMN members](./jet-retrievecolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
