---
title: JET_INDEXLIST.columnidcolumnid property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'columnidcolumnid property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcolumnid
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexlist.columnidcolumnid(v=EXCHG.10)
ms:contentKeyID: 55103608
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcolumnid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidcolumnid
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidcolumnid
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcolumnid
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST.columnidcolumnid property

Gets the columnid of the column in the temporary table which stores the columnid of the column being indexed. The column is of type [Long](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidcolumnid As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidcolumnid
```

``` csharp
public JET_COLUMNID columnidcolumnid { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  

## See also

#### Reference

[JET_INDEXLIST class](dn335123\(v=exchg.10\).md)

[JET_INDEXLIST members](dn335164\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

