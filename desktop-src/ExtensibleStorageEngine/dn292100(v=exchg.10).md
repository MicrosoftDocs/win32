---
title: Api.JetAttachDatabase2 method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetAttachDatabase2 method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetAttachDatabase2(Microsoft.Isam.Esent.Interop.JET_SESID,System.String,System.Int32,Microsoft.Isam.Esent.Interop.AttachDatabaseGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetattachdatabase2(v=EXCHG.10)
ms:contentKeyID: 55107224
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetAttachDatabase2
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetAttachDatabase2
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetAttachDatabase2 method

Attaches a database file for use with a database instance. In order to use the database, it will need to be subsequently opened with [JetOpenDatabase(JET\_SESID, String, String, JET\_DBID, OpenDatabaseGrbit)](dn292219\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function JetAttachDatabase2 ( _
    sesid As JET_SESID, _
    database As String, _
    maxPages As Integer, _
    grbit As AttachDatabaseGrbit _
) As JET_wrn
'Usage
Dim sesid As JET_SESID
Dim database As String
Dim maxPages As Integer
Dim grbit As AttachDatabaseGrbit
Dim returnValue As JET_wrn

returnValue = Api.JetAttachDatabase2(sesid, _
    database, maxPages, grbit)
```

``` csharp
public static JET_wrn JetAttachDatabase2(
    JET_SESID sesid,
    string database,
    int maxPages,
    AttachDatabaseGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - database  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The database to attach.

<!-- end list -->

  - maxPages  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    The maximum size, in database pages, of the database. Passing 0 means there is no enforced maximum.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.AttachDatabaseGrbit](hh579378\(v=exchg.10\).md)  
    
    Attach options.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET\_wrn](hh557250\(v=exchg.10\).md)  
An ESENT warning code.  

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

