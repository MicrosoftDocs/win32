---
description: "Learn more about: JET_OPENTEMPORARYTABLE.tableid property"
title: JET_OPENTEMPORARYTABLE.tableid property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'tableid property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.tableid
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_opentemporarytable.tableid(v=EXCHG.10)
ms:contentKeyID: 55104232
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.tableid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.tableid
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.get_tableid
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.set_tableid
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_OPENTEMPORARYTABLE.tableid property

Gets the table handle for the temporary table created as a result of a successful call to JetOpenTemporaryTable.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property tableid As JET_TABLEID
    Get
    Friend Set
'Usage
Dim instance As JET_OPENTEMPORARYTABLE
Dim value As JET_TABLEID

value = instance.tableid
```

``` csharp
public JET_TABLEID tableid { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  

## See also

#### Reference

[JET_OPENTEMPORARYTABLE class](./jet-opentemporarytable-class.md)

[JET_OPENTEMPORARYTABLE members](./jet-opentemporarytable-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
