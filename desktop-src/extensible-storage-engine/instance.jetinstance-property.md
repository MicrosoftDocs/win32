---
description: "Learn more about: Instance.JetInstance property"
title: Instance.JetInstance property 
TOCTitle: 'JetInstance property '
ms:assetid: P:Microsoft.Isam.Esent.Interop.Instance.JetInstance
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instance.jetinstance(v=EXCHG.10)
ms:contentKeyID: 55103279
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Instance.JetInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Instance.JetInstance
- Microsoft.Isam.Esent.Interop.Instance.get_JetInstance
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance.JetInstance property

Gets the JET_INSTANCE that this instance contains.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public ReadOnly Property JetInstance As JET_INSTANCE
    Get
'Usage
Dim instance As Instance
Dim value As JET_INSTANCE

value = instance.JetInstance
```

``` csharp
public JET_INSTANCE JetInstance { get; }
```

#### Property value

Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](./jet-instance-structure.md)  

## See also

#### Reference

[Instance class](./instance-class.md)

[Instance members](./instance-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
