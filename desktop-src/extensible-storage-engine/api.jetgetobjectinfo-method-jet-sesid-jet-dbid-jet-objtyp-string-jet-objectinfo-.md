---
title: Api.JetGetObjectInfo method (JET_SESID, JET_DBID, JET_objtyp, String, JET_OBJECTINFO)
TOCTitle: JetGetObjectInfo method (JET_SESID, JET_DBID, JET_objtyp, String, JET_OBJECTINFO)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetObjectInfo(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_DBID,Microsoft.Isam.Esent.Interop.JET_objtyp,System.String,Microsoft.Isam.Esent.Interop.JET_OBJECTINFO@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetobjectinfo(v=EXCHG.10)
ms:contentKeyID: 55100733
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

# Api.JetGetObjectInfo method (JET_SESID, JET_DBID, JET_objtyp, String, JET_OBJECTINFO)

Retrieves information about database objects.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetObjectInfo ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    objtyp As JET_objtyp, _
    objectName As String, _
    <OutAttribute> ByRef objectinfo As JET_OBJECTINFO _
)
'Usage
Dim sesid As JET_SESID
Dim dbid As JET_DBID
Dim objtyp As JET_objtyp
Dim objectName As String
Dim objectinfo As JET_OBJECTINFOApi.JetGetObjectInfo(sesid, dbid, _
    objtyp, objectName, objectinfo)
```

``` csharp
public static void JetGetObjectInfo(
    JET_SESID sesid,
    JET_DBID dbid,
    JET_objtyp objtyp,
    string objectName,
    out JET_OBJECTINFO objectinfo
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](hh596176\(v=exchg.10\).md)  
    
    The database to use.

<!-- end list -->

  - objtyp  
    Type: [Microsoft.Isam.Esent.Interop.JET_objtyp](hh565069\(v=exchg.10\).md)  
    
    The type of the object.

<!-- end list -->

  - objectName  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    The object name about which to retrieve information.

<!-- end list -->

  - objectinfo  
    Type: [Microsoft.Isam.Esent.Interop.JET_OBJECTINFO](dn335219\(v=exchg.10\).md)  
    
    Filled in with information about the objects in the database.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[JetGetObjectInfo overload](dn292176\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

