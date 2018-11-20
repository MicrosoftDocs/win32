---
title: JET_INSTANCE_INFO.szDatabaseFileName property  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'szDatabaseFileName property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.szDatabaseFileName
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_instance_info.szdatabasefilename(v=EXCHG.10)
ms:contentKeyID: 55103711
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.szDatabaseFileName
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.szDatabaseFileName
- Microsoft.Isam.Esent.Interop.JET_INSTANCE_INFO.get_szDatabaseFileName
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_INSTANCE\_INFO.szDatabaseFileName property

Gets a collection of strings, each holding the file name of a database that is attached to the database instance. The array has cDatabases elements.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property szDatabaseFileName As IList(Of String)
    Get
'Usage
Dim instance As JET_INSTANCE_INFO
Dim value As IList(Of String)

value = instance.szDatabaseFileName
```

``` csharp
public IList<string> szDatabaseFileName { get; }
```

#### Property value

Type: [System.Collections.Generic.IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)\<[String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)\>  

## See also

#### Reference

[JET\_INSTANCE\_INFO class](dn335182\(v=exchg.10\).md)

[JET\_INSTANCE\_INFO members](dn335183\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

