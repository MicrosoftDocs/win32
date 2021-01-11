---
description: "Learn more about: IJET_LOGTIME.ToDateTime method"
title: IJET_LOGTIME.ToDateTime method 
TOCTitle: 'ToDateTime method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.IJET_LOGTIME.ToDateTime
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.ijet_logtime.todatetime(v=EXCHG.10)
ms:contentKeyID: 39510507
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.IJET_LOGTIME.ToDateTime
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.IJET_LOGTIME.ToDateTime
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# IJET_LOGTIME.ToDateTime method

Generate a DateTime representation of this IJET_LOGTIME.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Function ToDateTime As Nullable(Of DateTime)
'Usage
Dim instance As IJET_LOGTIME
Dim returnValue As Nullable(Of DateTime)

returnValue = instance.ToDateTime()
```

``` csharp
Nullable<DateTime> ToDateTime()
```

#### Return value

Type: [System.Nullable](/dotnet/api/system.nullable-1)\<[DateTime](/dotnet/api/system.datetime)\>  
A DateTime representing the IJET_LOGTIME. If the IJET_LOGTIME is null then null is returned.  

## See also

#### Reference

[IJET_LOGTIME interface](./ijet-logtime-interface.md)

[IJET_LOGTIME members](./ijet-logtime-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
