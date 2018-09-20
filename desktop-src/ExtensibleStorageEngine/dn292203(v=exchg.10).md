---
title: Api.JetGetVersion method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetGetVersion method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetVersion(Microsoft.Isam.Esent.Interop.JET_SESID,System.UInt32@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetversion(v=EXCHG.10)
ms:contentKeyID: 55100744
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetGetVersion
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetVersion
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetVersion method

Retrieves the version of the database engine.

This API is not CLS-compliant. 

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<CLSCompliantAttribute(False)> _
Public Shared Sub JetGetVersion ( _
    sesid As JET_SESID, _
    <OutAttribute> ByRef version As UInteger _
)
'Usage
Dim sesid As JET_SESID
Dim version As UIntegerApi.JetGetVersion(sesid, version)
```

``` csharp
[CLSCompliantAttribute(false)]
public static void JetGetVersion(
    JET_SESID sesid,
    out uint version
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - version  
    Type: [System.UInt32](http://msdn2.microsoft.com/en-us/library/ctys3981)  
    
    Returns the version number of the database engine.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

