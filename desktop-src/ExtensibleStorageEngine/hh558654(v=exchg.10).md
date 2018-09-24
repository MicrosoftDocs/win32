---
title: JET_BKLOGTIME.ToDateTime method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'ToDateTime method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_BKLOGTIME.ToDateTime
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_bklogtime.todatetime(v=EXCHG.10)
ms:contentKeyID: 39515201
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_BKLOGTIME.ToDateTime
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_BKLOGTIME.ToDateTime
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_BKLOGTIME.ToDateTime method

Generate a DateTime representation of this JET\_BKLOGTIME.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Function ToDateTime As Nullable(Of DateTime)
'Usage
Dim instance As JET_BKLOGTIME
Dim returnValue As Nullable(Of DateTime)

returnValue = instance.ToDateTime()
```

``` csharp
public Nullable<DateTime> ToDateTime()
```

#### Return value

Type: [System.Nullable](http://msdn2.microsoft.com/en-us/library/b3h38hb0)\<[DateTime](http://msdn2.microsoft.com/en-us/library/03ybds8y)\>  
A DateTime representing the JET\_BKLOGTIME. If the JET\_BKLOGTIME is null then null is returned.  

#### Implements

[IJET\_LOGTIME.ToDateTime()](hh577639\(v=exchg.10\).md)  

## See also

#### Reference

[JET\_BKLOGTIME structure](hh557662\(v=exchg.10\).md)

[JET\_BKLOGTIME members](hh565503\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

