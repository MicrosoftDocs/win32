---
description: "Learn more about: JET_COLUMNCREATE.cp property"
title: JET_COLUMNCREATE.cp property 
TOCTitle: 'cp property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cp
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_columncreate.cp(v=EXCHG.10)
ms:contentKeyID: 55103400
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cp
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.get_cp
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.set_cp
- Microsoft.Isam.Esent.Interop.JET_COLUMNCREATE.cp
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_COLUMNCREATE.cp property

Gets or sets code page of the column. This is only meaningful for columns of type [Text](./jet-coltyp-enumeration.md) and [LongText](./jet-coltyp-enumeration.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property cp As JET_CP
    Get
    Set
'Usage
Dim instance As JET_COLUMNCREATE
Dim value As JET_CP

value = instance.cp

instance.cp = value
```

``` csharp
public JET_CP cp { get; set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_CP](./jet-cp-enumeration.md)  

## See also

#### Reference

[JET_COLUMNCREATE class](./jet-columncreate-class.md)

[JET_COLUMNCREATE members](./jet-columncreate-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
