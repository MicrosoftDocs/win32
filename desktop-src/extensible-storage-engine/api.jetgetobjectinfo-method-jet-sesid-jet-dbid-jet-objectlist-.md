---
description: "Learn more about: Api.JetGetObjectInfo method (JET_SESID, JET_DBID, JET_OBJECTLIST)"
title: Api.JetGetObjectInfo method (JET_SESID, JET_DBID, JET_OBJECTLIST)
TOCTitle: JetGetObjectInfo method (JET_SESID, JET_DBID, JET_OBJECTLIST)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetObjectInfo(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,Microsoft.Isam.Esent.Interop.JET_OBJECTLIST@)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgetobjectinfo(v=EXCHG.10)
ms:contentKeyID: 55100728
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetObjectInfo
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetObjectInfo method (JET_SESID, JET_DBID, JET_OBJECTLIST)

Retrieves information about database objects.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetObjectInfo ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    <OutAttribute> ByRef objectlist As JET_OBJECTLIST _
)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim objectlist As JET_OBJECTLISTApi.JetGetObjectInfo(sesid, dbid, _
    objectlist)
```

``` csharp
public static void JetGetObjectInfo(
    JET_SESID sesid,
    JET_DBID dbid,
    out JET_OBJECTLIST objectlist
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](./jet-dbid-structure.md)  
    
    The database to use.

<!-- end list -->

  - objectlist  
    Type: [Microsoft.Isam.Esent.Interop.JET_OBJECTLIST](./jet-objectlist-class.md)  
    
    Filled in with information about the objects in the database.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[JetGetObjectInfo overload](./api.jetgetobjectinfo-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
