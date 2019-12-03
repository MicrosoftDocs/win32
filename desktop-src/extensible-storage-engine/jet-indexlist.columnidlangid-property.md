---
title: JET_INDEXLIST.columnidLangid property 
TOCTitle: 'columnidLangid property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidLangid
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_indexlist.columnidlangid(v=EXCHG.10)
ms:contentKeyID: 55103666
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidLangid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.set_columnidLangid
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.columnidLangid
- Microsoft.Isam.Esent.Interop.JET_INDEXLIST.get_columnidLangid
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST.columnidLangid property

Gets the columnid of the column in the temporary table which stores the language id (LCID) of the index. The column is of type [Short](hh577895\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property columnidLangid As JET_COLUMNID
    Get
    Friend Set
'Usage
Dim instance As JET_INDEXLIST
Dim value As JET_COLUMNID

value = instance.columnidLangid
```

``` csharp
public JET_COLUMNID columnidLangid { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  

## See also

#### Reference

[JET_INDEXLIST class](dn335123\(v=exchg.10\).md)

[JET_INDEXLIST members](dn335164\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

