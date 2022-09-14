---
description: "Learn more about: Api.RetrieveColumnSize method (JET_SESID, JET_TABLEID, JET_COLUMNID, Int32, RetrieveColumnGrbit)"
title: Api.RetrieveColumnSize method (JET_SESID, JET_TABLEID, JET_COLUMNID, Int32, RetrieveColumnGrbit)
TOCTitle: RetrieveColumnSize method (JET_SESID, JET_TABLEID, JET_COLUMNID, Int32, RetrieveColumnGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.RetrieveColumnSize(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,Microsoft.Isam.Esent.Interop.JET_COLUMNID,System.Int32,Microsoft.Isam.Esent.Interop.RetrieveColumnGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.retrievecolumnsize(v=EXCHG.10)
ms:contentKeyID: 55100912
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.RetrieveColumnSize
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.RetrieveColumnSize method (JET_SESID, JET_TABLEID, JET_COLUMNID, Int32, RetrieveColumnGrbit)

Retrieves the size of a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Function RetrieveColumnSize ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    columnid As JET_COLUMNID, _
    itagSequence As Integer, _
    grbit As RetrieveColumnGrbit _
) As Nullable(Of Integer)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim columnid As JET_COLUMNID
Dim itagSequence As Integer
Dim grbit As RetrieveColumnGrbit
Dim returnValue As Nullable(Of Integer)

returnValue = Api.RetrieveColumnSize(sesid, _
    tableid, columnid, itagSequence, _
    grbit)
```

``` csharp
public static Nullable<int> RetrieveColumnSize(
    JET_SESID sesid,
    JET_TABLEID tableid,
    JET_COLUMNID columnid,
    int itagSequence,
    RetrieveColumnGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to retrieve the column from.

<!-- end list -->

  - columnid  
    Type: [Microsoft.Isam.Esent.Interop.JET_COLUMNID](./jet-columnid-structure.md)  
    
    The columnid to retrieve.

<!-- end list -->

  - itagSequence  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The sequence number of value in a multi-valued column. The array of values is one-based. The first value is sequence 1, not 0. If the record column has only one value then 1 should be passed as the itagSequence.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.RetrieveColumnGrbit](./retrievecolumngrbit-enumeration.md)  
    
    Retrieve column options.

#### Return value

Type: [System.Nullable](/dotnet/api/system.nullable-1)\<[Int32](/dotnet/api/system.int32)\>  
The size of the column. 0 if the column is null.  

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[RetrieveColumnSize overload](./api.retrievecolumnsize-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
