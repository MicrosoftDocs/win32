---
description: "Learn more about: Api.JetRetrieveColumns method"
title: Api.JetRetrieveColumns method 
TOCTitle: 'JetRetrieveColumns method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetRetrieveColumns(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,Microsoft.Isam.Esent.Interop.JET_RETRIEVECOLUMN[],System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetretrievecolumns(v=EXCHG.10)
ms:contentKeyID: 55100797
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetRetrieveColumns
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetRetrieveColumns
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetRetrieveColumns method

Retrieves multiple column values from the current record in a single operation. An array of JET_RETRIEVECOLUMN structures is used to describe the set of column values to be retrieved, and to describe output buffers for each column value to be retrieved.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function JetRetrieveColumns ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    retrievecolumns As JET_RETRIEVECOLUMN(), _
    numColumns As Integer _
) As JET_wrn
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim retrievecolumns As JET_RETRIEVECOLUMN()
Dim numColumns As Integer
Dim returnValue As JET_wrn

returnValue = Api.JetRetrieveColumns(sesid, _
    tableid, retrievecolumns, numColumns)
```

``` csharp
public static JET_wrn JetRetrieveColumns(
    JET_SESID sesid,
    JET_TABLEID tableid,
    JET_RETRIEVECOLUMN[] retrievecolumns,
    int numColumns
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to retrieve the data from.

<!-- end list -->

  - retrievecolumns  
    Type: \[\]  
    
    An array of one or more [JET_RETRIEVECOLUMN](./jet-retrievecolumn-class.md) objects describing the data to be retrieved.

<!-- end list -->

  - numColumns  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The number of entries in the columns array.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_wrn](./jet-wrn-enumeration.md)  
If any column retrieved is truncated due to an insufficient length buffer, then the API will return [BufferTruncated](./jet-wrn-enumeration.md). However other errors JET_wrnColumnNull are returned only in the error field of the [JET_RETRIEVECOLUMN](./jet-retrievecolumn-class.md) object.  

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
