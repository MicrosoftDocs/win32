---
title: JET_TABLECREATE.rgindexcreate property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'rgindexcreate property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgindexcreate
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_tablecreate.rgindexcreate(v=EXCHG.10)
ms:contentKeyID: 55103970
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgindexcreate
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.rgindexcreate
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.set_rgindexcreate
- Microsoft.Isam.Esent.Interop.JET_TABLECREATE.get_rgindexcreate
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_TABLECREATE.rgindexcreate property

Gets or sets an array of indices to create, of type [JET_INDEXCREATE](dn335112\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property rgindexcreate As JET_INDEXCREATE()
    Get
    Set
'Usage
Dim instance As JET_TABLECREATE
Dim value As JET_INDEXCREATE()

value = instance.rgindexcreate

instance.rgindexcreate = value
```

``` csharp
public JET_INDEXCREATE[] rgindexcreate { get; set; }
```

#### Property value

Type: \[\]  

## See also

#### Reference

[JET_TABLECREATE class](dn351072\(v=exchg.10\).md)

[JET_TABLECREATE members](dn351073\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

