---
description: "Learn more about: Api.JetEnumerateColumns method"
title: Api.JetEnumerateColumns method 
TOCTitle: 'JetEnumerateColumns method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetEnumerateColumns(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Int32,Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMNID[],System.Int32@,Microsoft.Isam.Esent.Interop.JET_ENUMCOLUMN[]@,Microsoft.Isam.Esent.Interop.JET_PFNREALLOC,System.IntPtr,System.Int32,Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetenumeratecolumns(v=EXCHG.10)
ms:contentKeyID: 55100695
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetEnumerateColumns
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetEnumerateColumns
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetEnumerateColumns method

Efficiently retrieves a set of columns and their values from the current record of a cursor or the copy buffer of that cursor. The columns and values retrieved can be restricted by a list of column IDs, itagSequence numbers, and other characteristics. This column retrieval API is unique in that it returns information in dynamically allocated memory that is obtained using a user-provided realloc compatible callback. This new flexibility permits the efficient retrieval of column data with specific characteristics (such as size and multiplicity) that are unknown to the caller. This eliminates the need for the use of the discovery modes of JetRetrieveColumn to determine those characteristics in order to setup a final call to JetRetrieveColumn that will successfully retrieve the desired data.

This API is not CLS-compliant. 

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<CLSCompliantAttribute(False)> _
Public Shared Function JetEnumerateColumns ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    numColumnids As Integer, _
    columnids As JET_ENUMCOLUMNID(), _
    <OutAttribute> ByRef numColumnValues As Integer, _
    <OutAttribute> ByRef columnValues As JET_ENUMCOLUMN(), _
    allocator As JET_PFNREALLOC, _
    allocatorContext As IntPtr, _
    maxDataSize As Integer, _
    grbit As EnumerateColumnsGrbit _
) As JET_wrn
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim numColumnids As Integer
Dim columnids As JET_ENUMCOLUMNID()
Dim numColumnValues As Integer
Dim columnValues As JET_ENUMCOLUMN()
Dim allocator As JET_PFNREALLOC
Dim allocatorContext As IntPtr
Dim maxDataSize As Integer
Dim grbit As EnumerateColumnsGrbit
Dim returnValue As JET_wrn

returnValue = Api.JetEnumerateColumns(sesid, _
    tableid, numColumnids, columnids, _
    numColumnValues, columnValues, allocator, _
    allocatorContext, maxDataSize, grbit)
```

``` csharp
[CLSCompliantAttribute(false)]
public static JET_wrn JetEnumerateColumns(
    JET_SESID sesid,
    JET_TABLEID tableid,
    int numColumnids,
    JET_ENUMCOLUMNID[] columnids,
    out int numColumnValues,
    out JET_ENUMCOLUMN[] columnValues,
    JET_PFNREALLOC allocator,
    IntPtr allocatorContext,
    int maxDataSize,
    EnumerateColumnsGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to retrieve data from.

<!-- end list -->

  - numColumnids  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The numbers of JET_ENUMCOLUMNIDS.

<!-- end list -->

  - columnids  
    Type: \[\]  
    
    An optional array of column IDs, each with an optional array of itagSequence numbers to enumerate.

<!-- end list -->

  - numColumnValues  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Returns the number of column values retrieved.

<!-- end list -->

  - columnValues  
    Type: \[\]  
    
    Returns the enumerated column values.

<!-- end list -->

  - allocator  
    Type: [Microsoft.Isam.Esent.Interop.JET_PFNREALLOC](./jet-pfnrealloc-delegate.md)  
    
    Callback used to allocate memory.

<!-- end list -->

  - allocatorContext  
    Type: [System.IntPtr](/dotnet/api/system.intptr)  
    
    Context for the allocation callback.

<!-- end list -->

  - maxDataSize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Sets a cap on the amount of data to return from a long text or long binary column. This parameter can be used to prevent the enumeration of an extremely large column value.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.EnumerateColumnsGrbit](./enumeratecolumnsgrbit-enumeration.md)  
    
    Retrieve options.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_wrn](./jet-wrn-enumeration.md)  
A warning or success.  

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
