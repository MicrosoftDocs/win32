---
description: "Learn more about: Instance.Init method (InitGrbit)"
title: Instance.Init method (InitGrbit)
TOCTitle: Init method (InitGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Instance.Init(Microsoft.Isam.Esent.Interop.InitGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instance.init(v=EXCHG.10)
ms:contentKeyID: 55103295
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Instance.Init
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance.Init method (InitGrbit)

Initialize the JET_INSTANCE.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SecurityPermissionAttribute(SecurityAction.LinkDemand)> _
Public Sub Init ( _
    grbit As InitGrbit _
)
'Usage
Dim instance As Instance
Dim grbit As InitGrbit

instance.Init(grbit)
```

``` csharp
[SecurityPermissionAttribute(SecurityAction.LinkDemand)]
public void Init(
    InitGrbit grbit
)
```

#### Parameters

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.InitGrbit](./initgrbit-enumeration.md)  
    
    Initialization options.

## See also

#### Reference

[Instance class](./instance-class.md)

[Instance members](./instance-members.md)

[Init overload](./instance.init-method2.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
