---
title: JET_RETRIEVECOLUMN.itagSequence property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'itagSequence property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.itagSequence
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_retrievecolumn.itagsequence(v=EXCHG.10)
ms:contentKeyID: 55103882
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.itagSequence
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.get_itagSequence
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.itagSequence
- Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN.set_itagSequence
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_RETRIEVECOLUMN.itagSequence property

Gets or sets the sequence number of the values that are contained in a multi-valued column. If the itagSequence is 0 then the number of instances of a multi-valued column are returned instead of any column data.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Property itagSequence As Integer
    Get
    Set
'Usage
Dim instance As JET_RETRIEVECOLUMN
Dim value As Integer

value = instance.itagSequence

instance.itagSequence = value
```

``` csharp
public int itagSequence { get; set; }
```

#### Property value

Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  

## See also

#### Reference

[JET\_RETRIEVECOLUMN class](dn351033\(v=exchg.10\).md)

[JET\_RETRIEVECOLUMN members](dn351034\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

