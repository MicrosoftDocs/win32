---
title: JET_INDEXLIST.columnidcColumn property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'columnidcColumn property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcColumn
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexlist.columnidccolumn(v=EXCHG.10)
ms:contentKeyID: 55103595
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcColumn
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidcColumn
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidcColumn
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcColumn
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_INDEXLIST.columnidcColumn property

Gets the columnid of the column in the temporary table which stores the number of columns in the index key. The column is of type [Long](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidcColumn As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidcColumn
```

``` csharp
public JET_COLUMNID columnidcColumn { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET\_COLUMNID](hh564510\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_INDEXLIST class](dn335123\(v=exchg.10\).md)

[JET\_INDEXLIST members](dn335164\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

