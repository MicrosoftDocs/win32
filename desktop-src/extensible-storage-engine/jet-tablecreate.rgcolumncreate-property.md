---
description: "Learn more about: JET_TABLECREATE.rgcolumncreate property"
title: JET_TABLECREATE.rgcolumncreate property 
TOCTitle: 'rgcolumncreate property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgcolumncreate
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_tablecreate.rgcolumncreate(v=EXCHG.10)
ms:contentKeyID: 55103965
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgcolumncreate
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.get_rgcolumncreate
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgcolumncreate
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.set_rgcolumncreate
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_TABLECREATE.rgcolumncreate property

Gets or sets an array of column creation info, of type [JET_COLUMNCREATE](./jet-columncreate-class.md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property rgcolumncreate As JET_COLUMNCREATE()
    Get
    Set
'Usage
Dim instance As JET_TABLECREATE
Dim value As JET_COLUMNCREATE()

value = instance.rgcolumncreate

instance.rgcolumncreate = value
```

``` csharp
public JET_COLUMNCREATE[] rgcolumncreate { get; set; }
```

#### Property value

Type: \[\]  

## See also

#### Reference

[JET_TABLECREATE class](./jet-tablecreate-class.md)

[JET_TABLECREATE members](./jet-tablecreate-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
