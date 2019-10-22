---
title: Api.JetAddColumn method 
TOCTitle: 'JetAddColumn method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetAddColumn(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.String,Microsoft.Isam.Esent.Interop.JET_COLUMNDEF,System.Byte[],System.Int32,Microsoft.Isam.Esent.Interop.JET_COLUMNID@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetaddcolumn(v=EXCHG.10)
ms:contentKeyID: 55100651
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetAddColumn
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetAddColumn
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetAddColumn method

Add a new column to an existing table.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetAddColumn ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    column As String, _
    columndef As JET_COLUMNDEF, _
    defaultValue As Byte(), _
    defaultValueSize As Integer, _
    <OutAttribute> ByRef columnid As JET_COLUMNID _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim column As String
Dim columndef As JET_COLUMNDEF
Dim defaultValue As Byte()
Dim defaultValueSize As Integer
Dim columnid As JET_COLUMNIDApi.JetAddColumn(sesid, tableid, _
    column, columndef, defaultValue, _
    defaultValueSize, columnid)
```

``` csharp
public static void JetAddColumn(
    JET_SESID sesid,
    JET_TABLEID tableid,
    string column,
    JET_COLUMNDEF columndef,
    byte[] defaultValue,
    int defaultValueSize,
    out JET_COLUMNID columnid
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The table to add the column to.

<!-- end list -->

  - column  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    The name of the column.

<!-- end list -->

  - columndef  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNDEF](dn335038\(v=exchg.10\).md)  
    
    The definition of the column.

<!-- end list -->

  - defaultValue  
    Type: \[\]  
    
    The default value of the column.

<!-- end list -->

  - defaultValueSize  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    The size of the default value.

<!-- end list -->

  - columnid  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](hh564510\(v=exchg.10\).md)  
    
    Returns the columnid of the new column.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

