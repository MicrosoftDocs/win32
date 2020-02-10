---
title: Api.JetResetSessionContext method 
TOCTitle: 'JetResetSessionContext method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetResetSessionContext(Microsoft.Isam.Esent.Interop.JET_SESID)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetresetsessioncontext(v=EXCHG.10)
ms:contentKeyID: 55100785
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetResetSessionContext
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetResetSessionContext
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetResetSessionContext method

Disassociates a session from the current thread. This should be used in conjunction with [JetSetSessionContext(JET_SESID, IntPtr)](dn334027\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetResetSessionContext ( _
    sesid As JET_SESID _
)
'Usage
Dim sesid As JET_SESIDApi.JetResetSessionContext(sesid)
```

``` csharp
public static void JetResetSessionContext(
    JET_SESID sesid
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

