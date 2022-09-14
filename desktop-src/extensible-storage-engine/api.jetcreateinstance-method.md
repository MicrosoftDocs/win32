---
description: "Learn more about: Api.JetCreateInstance method"
title: Api.JetCreateInstance method 
TOCTitle: 'JetCreateInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetCreateInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE@,System.String)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetcreateinstance(v=EXCHG.10)
ms:contentKeyID: 55100672
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetCreateInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetCreateInstance
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetCreateInstance method

Allocates a new instance of the database engine.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetCreateInstance ( _
    <OutAttribute> ByRef instance As JET_INSTANCE, _
    name As String _
)
'Usage
Dim instance As JET_INSTANCE
Dim name As StringApi.JetCreateInstance(instance, _
    name)
```

``` csharp
public static void JetCreateInstance(
    out JET_INSTANCE instance,
    string name
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](./jet-instance-structure.md)  
    
    Returns the new instance.

<!-- end list -->

  - name  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the instance. Names must be unique.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
