---
title: JET_OPENTEMPORARYTABLE.prgcolumndef property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'prgcolumndef property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.prgcolumndef
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.vista.jet_opentemporarytable.prgcolumndef(v=EXCHG.10)
ms:contentKeyID: 55104129
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.prgcolumndef
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.set_prgcolumndef
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.get_prgcolumndef
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.prgcolumndef
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_OPENTEMPORARYTABLE.prgcolumndef property

Gets or sets the column definitions for the columns created in the temporary table.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](hh558039\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property prgcolumndef As JET_COLUMNDEF()
    Get
    Set
'Usage
Dim instance As JET_OPENTEMPORARYTABLE
Dim value As JET_COLUMNDEF()

value = instance.prgcolumndef

instance.prgcolumndef = value
```

``` csharp
public JET_COLUMNDEF[] prgcolumndef { get; set; }
```

#### Property value

Type: \[\]  

## See also

#### Reference

[JET\_OPENTEMPORARYTABLE class](dn351217\(v=exchg.10\).md)

[JET\_OPENTEMPORARYTABLE members](dn335285\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop.Vista namespace](hh558039\(v=exchg.10\).md)

