---
title: StringColumnValue.Value property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'Value property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.StringColumnValue.Value
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.stringcolumnvalue.value(v=EXCHG.10)
ms:contentKeyID: 55104098
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.StringColumnValue.Value
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.StringColumnValue.get_Value
- Microsoft.Isam.Esent.Interop.StringColumnValue.set_Value
- Microsoft.Isam.Esent.Interop.StringColumnValue.Value
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# StringColumnValue.Value property

Gets or sets the value of the column. Use [SetColumns(JET\_SESID, JET\_TABLEID, \[\])](dn334138\(v=exchg.10\).md) to update a record with the column value.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property Value As String
    Get
    Set
'Usage
Dim instance As StringColumnValue
Dim value As String

value = instance.Value

instance.Value = value
```

``` csharp
public string Value { get; set; }
```

#### Property value

Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  

## See also

#### Reference

[StringColumnValue class](dn351135\(v=exchg.10\).md)

[StringColumnValue members](dn351145\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

