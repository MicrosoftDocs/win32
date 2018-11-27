---
title: JET_INDEXLIST.columnidcoltyp property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'columnidcoltyp property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcoltyp
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexlist.columnidcoltyp(v=EXCHG.10)
ms:contentKeyID: 55103600
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcoltyp
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidcoltyp
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidcoltyp
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidcoltyp
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_INDEXLIST.columnidcoltyp property

Gets the columnid of the column in the temporary table which stores the column type of the column being indexed. The column is of type [Long](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidcoltyp As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidcoltyp
```

``` csharp
public JET_COLUMNID columnidcoltyp { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET\_COLUMNID](hh564510\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_INDEXLIST class](dn335123\(v=exchg.10\).md)

[JET\_INDEXLIST members](dn335164\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

