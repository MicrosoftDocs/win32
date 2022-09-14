---
description: "Learn more about: Api.JetGetTableInfo method (JET_SESID, JET_TABLEID, Int32 , JET_TblInfo)"
title: Api.JetGetTableInfo method (JET_SESID, JET_TABLEID, Int32 , JET_TblInfo)
TOCTitle: JetGetTableInfo method (JET_SESID, JET_TABLEID, Int32 , JET_TblInfo)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetTableInfo(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.Int32[],Microsoft.Isam.Esent.Interop.JET_TblInfo)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgettableinfo(v=EXCHG.10)
ms:contentKeyID: 55100746
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetTableInfo
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetTableInfo method (JET_SESID, JET_TABLEID, Int32 , JET_TblInfo)

Retrieves various pieces of information about a table in a database.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetTableInfo ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    result As Integer(), _
    infoLevel As JET_TblInfo _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim result As Integer()
Dim infoLevel As JET_TblInfoApi.JetGetTableInfo(sesid, tableid, _
    result, infoLevel)
```

``` csharp
public static void JetGetTableInfo(
    JET_SESID sesid,
    JET_TABLEID tableid,
    int[] result,
    JET_TblInfo infoLevel
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The table to retrieve information about.

<!-- end list -->

  - result  
    Type: \[\]  
    
    Retrieved information.

<!-- end list -->

  - infoLevel  
    Type: [Microsoft.Isam.Esent.Interop.JET_TblInfo](./jet-tblinfo-enumeration.md)  
    
    The type of information to retrieve.

## Remarks

This overload is used with [SpaceUsage](./jet-tblinfo-enumeration.md) and [SpaceAlloc](./jet-tblinfo-enumeration.md).

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[JetGetTableInfo overload](./api.jetgettableinfo-method.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
