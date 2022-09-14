---
description: "Learn more about: DurableCommitCallback.ReleaseResource method"
title: DurableCommitCallback.ReleaseResource method  (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: 'ReleaseResource method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Windows8.DurableCommitCallback.ReleaseResource
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.durablecommitcallback.releaseresource(v=EXCHG.10)
ms:contentKeyID: 55104293
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.DurableCommitCallback.ReleaseResource
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.DurableCommitCallback.ReleaseResource
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# DurableCommitCallback.ReleaseResource method

Frees the durable commit session.

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Protected Overrides Sub ReleaseResource
'Usage

Me.ReleaseResource()
```

``` csharp
protected override void ReleaseResource()
```

## Remarks

Do not try to set the instance parameter to null, because the callback is disposed after JetTerm and the callback cannot be set after JetTerm.

## See also

#### Reference

[DurableCommitCallback class](./durablecommitcallback-class.md)

[DurableCommitCallback members](./durablecommitcallback-members.md)

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
