---
description: "Learn more about: JET_OPENTEMPORARYTABLE.pidxunicode property"
title: JET_OPENTEMPORARYTABLE.pidxunicode property  (Microsoft.Isam.Esent.Interop.Vista)
TOCTitle: 'pidxunicode property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.pidxunicode
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.vista.jet_opentemporarytable.pidxunicode(v=EXCHG.10)
ms:contentKeyID: 55104227
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.pidxunicode
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.set_pidxunicode
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.get_pidxunicode
- Microsoft.Isam.Esent.Interop.Vista.JET_OPENTEMPORARYTABLE.pidxunicode
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_OPENTEMPORARYTABLE.pidxunicode property

Gets or sets the locale ID and normalization flags to use to compare any Unicode key column data in the temporary table. When this parameter is null, then the default LCID will be used to compare any Unicode key columns in the temporary table. The default LCID is the U.S. English locale. When this parameter is null, then the default normalization flags will be used to compare any Unicode key column data in the temp table. The default normalization flags are: NORM_IGNORECASE, NORM_IGNOREKANATYPE, and NORM_IGNOREWIDTH.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property pidxunicode As JET_UNICODEINDEX
    Get
    Set
'Usage
Dim instance As JET_OPENTEMPORARYTABLE
Dim value As JET_UNICODEINDEX

value = instance.pidxunicode

instance.pidxunicode = value
```

``` csharp
public JET_UNICODEINDEX pidxunicode { get; set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_UNICODEINDEX](./jet-unicodeindex-class.md)  

## See also

#### Reference

[JET_OPENTEMPORARYTABLE class](./jet-opentemporarytable-class.md)

[JET_OPENTEMPORARYTABLE members](./jet-opentemporarytable-members.md)

[Microsoft.Isam.Esent.Interop.Vista namespace](./microsoft.isam.esent.interop.vista-namespace.md)
