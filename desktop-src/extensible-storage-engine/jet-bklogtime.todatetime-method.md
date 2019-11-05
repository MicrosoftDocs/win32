---
title: JET_BKLOGTIME.ToDateTime method 
TOCTitle: 'ToDateTime method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.JET_BKLOGTIME.ToDateTime
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_bklogtime.todatetime(v=EXCHG.10)
ms:contentKeyID: 39515201
ms.date: 07/30/2014
ms.topic: reference
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

# JET_BKLOGTIME.ToDateTime method

Generate a DateTime representation of this JET_BKLOGTIME.

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

Type: [System.Nullable](https://docs.microsoft.com/dotnet/api/system.nullable-1?redirectedfrom=MSDN)\<[DateTime](https://docs.microsoft.com/dotnet/api/system.datetime?redirectedfrom=MSDN)\>  
A DateTime representing the JET_BKLOGTIME. If the JET_BKLOGTIME is null then null is returned.  

#### Implements

[IJET_LOGTIME.ToDateTime()](hh577639\(v=exchg.10\).md)  

## See also

#### Reference

[JET_BKLOGTIME structure](hh557662\(v=exchg.10\).md)

[JET_BKLOGTIME members](hh565503\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

