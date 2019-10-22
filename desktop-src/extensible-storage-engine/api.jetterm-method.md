---
title: Api.JetTerm method 
TOCTitle: 'JetTerm method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetTerm(Microsoft.Isam.Esent.Interop.JET_INSTANCE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetterm(v=EXCHG.10)
ms:contentKeyID: 55100813
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetTerm
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetTerm
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetTerm method

Terminate an instance that was created with [JetInit(JET_INSTANCE)](dn292210\(v=exchg.10\).md) or [JetCreateInstance(JET_INSTANCE, String)](dn292122\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetTerm ( _
    instance As JET_INSTANCE _
)
'Usage
Dim instance As JET_INSTANCEApi.JetTerm(instance)
```

``` csharp
public static void JetTerm(
    JET_INSTANCE instance
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to terminate.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

