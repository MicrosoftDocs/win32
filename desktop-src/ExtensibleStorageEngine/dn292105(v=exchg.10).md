---
title: Api.JetBeginTransaction method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetBeginTransaction method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetBeginTransaction(Microsoft.Isam.Esent.Interop.JET_SESID)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetbegintransaction(v=EXCHG.10)
ms:contentKeyID: 55107225
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetBeginTransaction
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetBeginTransaction
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetBeginTransaction method

Causes a session to enter a transaction or create a new save point in an existing transaction.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetBeginTransaction ( _
    sesid As JET_SESID _
)
'Usage
Dim sesid As JET_SESIDApi.JetBeginTransaction(sesid)
```

``` csharp
public static void JetBeginTransaction(
    JET_SESID sesid
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to begin the transaction for.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

