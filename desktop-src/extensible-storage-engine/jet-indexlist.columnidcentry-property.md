---
title: JET_INDEXLIST.columnidcEntry property 
TOCTitle: 'columnidcEntry property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcEntry
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexlist.columnidcentry(v=EXCHG.10)
ms:contentKeyID: 55103597
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcEntry
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidcEntry
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcEntry
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidcEntry
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST.columnidcEntry property

Gets the columnid of the column in the temporary table which stores the number of entries in the index. This value is not current and is only is updated by "Api.JetComputeStats". The column is of type [Long](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidcEntry As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidcEntry
```

``` csharp
public JET_COLUMNID columnidcEntry { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  

## See also

#### Reference

[JET_INDEXLIST class](dn335123\(v=exchg.10\).md)

[JET_INDEXLIST members](dn335164\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

