---
title: Instance.Init method (JET_RSTINFO, InitGrbit)
TOCTitle: Init method (JET_RSTINFO, InitGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Instance.Init(Microsoft.Isam.Esent.Interop.JET_RSTINFO,Microsoft.Isam.Esent.Interop.InitGrbit)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.instance.init(v=EXCHG.10)
ms:contentKeyID: 55103274
ms.date: 07/30/2014
ms.topic: article
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Instance.Init
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance.Init method (JET_RSTINFO, InitGrbit)

Initialize the JET_INSTANCE. This API requires at least the Vista version of ESENT.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SecurityPermissionAttribute(SecurityAction.LinkDemand)> _
Public Sub Init ( _
    recoveryOptions As JET_RSTINFO, _
    grbit As InitGrbit _
)
'Usage
Dim instance As Instance
Dim recoveryOptions As JET_RSTINFO
Dim grbit As InitGrbit

instance.Init(recoveryOptions, grbit)
```

``` csharp
[SecurityPermissionAttribute(SecurityAction.LinkDemand)]
public void Init(
    JET_RSTINFO recoveryOptions,
    InitGrbit grbit
)
```

#### Parameters

  - recoveryOptions  
    Type: [Microsoft.Isam.Esent.Interop.JET_RSTINFO](dn335235\(v=exchg.10\).md)  
    
    Additional recovery parameters for remapping databases during recovery, position where to stop recovery at, or recovery status.

<!-- end list -->

  - grbit  
    Type: [Microsoft.Isam.Esent.Interop.InitGrbit](hh596658\(v=exchg.10\).md)  
    
    Initialization options.

## See also

#### Reference

[Instance class](dn350923\(v=exchg.10\).md)

[Instance members](dn350944\(v=exchg.10\).md)

[Init overload](dn350952\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

