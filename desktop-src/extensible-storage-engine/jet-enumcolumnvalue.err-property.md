---
title: JET_ENUMCOLUMNVALUE.err property 
TOCTitle: 'err property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE.err
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_enumcolumnvalue.err(v=EXCHG.10)
ms:contentKeyID: 55103626
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE.err
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE.get_err
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE.err
- Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNVALUE.set_err
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_ENUMCOLUMNVALUE.err property

Gets the column status code resulting from the enumeration of the column value.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property err As JET_wrn
    Get
    Friend Set
'Usage
Dim instance As JET_ENUMCOLUMNVALUE
Dim value As JET_wrn

value = instance.err
```

``` csharp
public JET_wrn err { get; internal set; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_wrn](hh557250\(v=exchg.10\).md)  

## See also

#### Reference

[JET_ENUMCOLUMNVALUE class](dn335142\(v=exchg.10\).md)

[JET_ENUMCOLUMNVALUE members](dn335094\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

[ColumnNull](hh557250\(v=exchg.10\).md)

[ColumnSkipped](hh557250\(v=exchg.10\).md)

[ColumnTruncated](hh557250\(v=exchg.10\).md)

