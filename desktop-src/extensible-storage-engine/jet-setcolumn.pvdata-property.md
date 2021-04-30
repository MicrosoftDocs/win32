---
description: "Learn more about: JET_SETCOLUMN.pvData property"
title: JET_SETCOLUMN.pvData property 
TOCTitle: 'pvData property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.pvData
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_setcolumn.pvdata(v=EXCHG.10)
ms:contentKeyID: 55103932
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.pvData
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.set_pvData
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.get_pvData
- Microsoft.Isam.Esent.Interop.JET_SETCOLUMN.pvData
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_SETCOLUMN.pvData property

Gets or sets a pointer to the data to set.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property pvData As Byte()
    Get
    Set
'Usage
Dim instance As JET_SETCOLUMN
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

[JET_SETCOLUMN class](./jet-setcolumn-class.md)

[JET_SETCOLUMN members](./jet-setcolumn-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
