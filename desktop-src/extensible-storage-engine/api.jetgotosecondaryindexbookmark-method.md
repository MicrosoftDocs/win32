---
description: "Learn more about: Api.JetGotoSecondaryIndexBookmark method"
title: Api.JetGotoSecondaryIndexBookmark method 
TOCTitle: 'JetGotoSecondaryIndexBookmark method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGotoSecondaryIndexBookmark(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Byte[],System.Int32,System.Byte[],System.Int32,Microsoft.Isam.Esent.Interop.GotoSecondaryIndexBookmarkGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgotosecondaryindexbookmark(v=EXCHG.10)
ms:contentKeyID: 55100755
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetGotoSecondaryIndexBookmark
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGotoSecondaryIndexBookmark
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGotoSecondaryIndexBookmark method

Positions a cursor to an index entry that is associated with the specified secondary index bookmark. The secondary index bookmark must be used with the same index over the same table from which it was originally retrieved. The secondary index bookmark for an index entry can be retrieved using JetGotoSecondaryIndexBookmark(JET_SESID, JET_TABLEID, \[\], Int32, \[\], Int32, GotoSecondaryIndexBookmarkGrbit).

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGotoSecondaryIndexBookmark ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    secondaryKey As Byte(), _
    secondaryKeySize As Integer, _
    primaryKey As Byte(), _
    primaryKeySize As Integer, _
    grbit As GotoSecondaryIndexBookmarkGrbit _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim secondaryKey As Byte()
Dim secondaryKeySize As Integer
Dim primaryKey As Byte()
Dim primaryKeySize As Integer
Dim grbit As GotoSecondaryIndexBookmarkGrbitApi.JetGotoSecondaryIndexBookmark(sesid, _
    tableid, secondaryKey, secondaryKeySize, _
    primaryKey, primaryKeySize, grbit)
```

``` csharp
public static void JetGotoSecondaryIndexBookmark(
    JET_SESID sesid,
    JET_TABLEID tableid,
    byte[] secondaryKey,
    int secondaryKeySize,
    byte[] primaryKey,
    int primaryKeySize,
    GotoSecondaryIndexBookmarkGrbit grbit
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The table cursor to position.

<!-- end list -->

  - secondaryKey  
    Type: \[\]  
    
    The buffer that contains the secondary key.

<!-- end list -->

  - secondaryKeySize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The size of the secondary key.

<!-- end list -->

  - primaryKey  
    Type: \[\]  
    
    The buffer that contains the primary key.

<!-- end list -->

  - primaryKeySize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The size of the primary key.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.GotoSecondaryIndexBookmarkGrbit](./gotosecondaryindexbookmarkgrbit-enumeration.md)  
    
    Options for positioning the bookmark.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
