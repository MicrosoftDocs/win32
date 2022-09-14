---
description: "Learn more about: JET_TABLECREATE.pSeqSpacehints property"
title: JET_TABLECREATE.pSeqSpacehints property 
TOCTitle: 'pSeqSpacehints property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_TABLECREATE.pSeqSpacehints
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_tablecreate.pseqspacehints(v=EXCHG.10)
ms:contentKeyID: 55103967
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.pSeqSpacehints
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.pSeqSpacehints
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.set_pSeqSpacehints
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.get_pSeqSpacehints
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_TABLECREATE.pSeqSpacehints property

Gets or sets space allocation, maintenance, and usage hints for default sequential index.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property pSeqSpacehints As JET_SPACEHINTS
    Get
    Set
'Usage
Dim instance As JET_TABLECREATE
Dim value As JET_SPACEHINTS

value = instance.pSeqSpacehints

instance.pSeqSpacehints = value
```

``` csharp
public JET_SPACEHINTS pSeqSpacehints { get; set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_SPACEHINTS](./jet-spacehints-class.md)  

## See also

#### Reference

[JET_TABLECREATE class](./jet-tablecreate-class.md)

[JET_TABLECREATE members](./jet-tablecreate-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
