---
title: Api.GetTableColumnid method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'GetTableColumnid method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.GetTableColumnid(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.String)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.gettablecolumnid(v=EXCHG.10)
ms:contentKeyID: 55107215
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.GetTableColumnid
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.GetTableColumnid
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.GetTableColumnid method

Get the columnid of the specified column.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function GetTableColumnid ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    columnName As String _
) As JET_COLUMNID
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim columnName As String
Dim returnValue As JET_COLUMNID

returnValue = Api.GetTableColumnid(sesid, _
    tableid, columnName)
```

``` csharp
public static JET_COLUMNID GetTableColumnid(
    JET_SESID sesid,
    JET_TABLEID tableid,
    string columnName
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The table containing the column.

<!-- end list -->

  - columnName  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    The name of the column.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  
The id of the column.  

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

