---
description: "Learn more about: Api.JetGetCurrentIndex method"
title: Api.JetGetCurrentIndex method 
TOCTitle: 'JetGetCurrentIndex method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetCurrentIndex(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,System.String@,System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetgetcurrentindex(v=EXCHG.10)
ms:contentKeyID: 55100699
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetGetCurrentIndex
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetCurrentIndex
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetCurrentIndex method

Ddetermines the name of the current index of a given cursor. This name is also used to later re-select that index as the current index using [JetSetCurrentIndex(JET_SESID, JET_TABLEID, String)](./api.jetsetcurrentindex-method.md). It can also be used to discover the properties of that index using JetGetTableIndexInfo.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetCurrentIndex ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    <OutAttribute> ByRef indexName As String, _
    maxNameLength As Integer _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim indexName As String
Dim maxNameLength As IntegerApi.JetGetCurrentIndex(sesid, tableid, _
    indexName, maxNameLength)
```

``` csharp
public static void JetGetCurrentIndex(
    JET_SESID sesid,
    JET_TABLEID tableid,
    out string indexName,
    int maxNameLength
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](./jet-tableid-structure.md)  
    
    The cursor to get the index name for.

<!-- end list -->

  - indexName  
    Type: [System.String](/dotnet/api/system.string)  
    
    Returns the name of the index.

<!-- end list -->

  - maxNameLength  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    The maximum length of the index name. Index names are no more than [NameMost](./systemparameters.namemost-field.md) characters.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
