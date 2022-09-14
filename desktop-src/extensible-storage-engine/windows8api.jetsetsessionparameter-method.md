---
description: "Learn more about: Windows8Api.JetSetSessionParameter method"
title: Windows8Api.JetSetSessionParameter method  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'JetSetSessionParameter method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.Windows8Api.JetSetSessionParameter(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.Windows8.JET_sesparam,System.Byte[],System.Int32)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.windows8api.jetsetsessionparameter(v=EXCHG.10)
ms:contentKeyID: 55104461
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.Windows8Api.JetSetSessionParameter
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.Windows8Api.JetSetSessionParameter
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Windows8Api.JetSetSessionParameter method

Sets a parameter on the provided session state, used for the lifetime of this session or until reset.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetSetSessionParameter ( _
    sesid As JET_SESID, _
    sesparamid As JET_sesparam, _
    data As Byte(), _
    dataSize As Integer _
)
'Usage
Dim sesid As JET_SESID
Dim sesparamid As JET_sesparam
Dim data As Byte()
Dim dataSize As IntegerWindows8Api.JetSetSessionParameter(sesid, _
    sesparamid, data, dataSize)
```

``` csharp
public static void JetSetSessionParameter(
    JET_SESID sesid,
    JET_sesparam sesparamid,
    byte[] data,
    int dataSize
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](./jet-sesid-structure.md)  
    
    The session to set the parameter on.

<!-- end list -->

  - sesparamid  
    Type: [Microsoft.Isam.Esent.Interop.Windows8.JET_sesparam](./jet-sesparam-enumeration.md)  
    
    The ID of the session parameter to set.

<!-- end list -->

  - data  
    Type: \[\]  
    
    Data to set in this session parameter.

<!-- end list -->

  - dataSize  
    Type: [System.Int32](/dotnet/api/system.int32)  
    
    Size of the data provided.

## See also

#### Reference

[Windows8Api class](./windows8api-class.md)

[Windows8Api members](./windows8api-members.md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
