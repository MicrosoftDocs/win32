---
title: Api.JetSetSessionContext method 
TOCTitle: 'JetSetSessionContext method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetSetSessionContext(Microsoft.Isam.Esent.Interop.JET_SESID,System.IntPtr)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetsetsessioncontext(v=EXCHG.10)
ms:contentKeyID: 55100820
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetSetSessionContext
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetSetSessionContext
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetSetSessionContext method

Associates a session with the current thread using the given context handle. This association overrides the default engine requirement that a transaction for a given session must occur entirely on the same thread. Use [JetResetSessionContext(JET_SESID)](dn332991\(v=exchg.10\).md) to remove the association.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetSetSessionContext ( _
    sesid As JET_SESID, _
    context As IntPtr _
)
'Usage
Dim sesid As JET_SESID
Dim context As IntPtrApi.JetSetSessionContext(sesid, _
    context)
```

``` csharp
public static void JetSetSessionContext(
    JET_SESID sesid,
    IntPtr context
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to set the context on.

<!-- end list -->

  - context  
    Type: [System.IntPtr](https://docs.microsoft.com/dotnet/api/system.intptr?redirectedfrom=MSDN)  
    
    The context to set.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

