---
title: Instance constructor (String) (Microsoft.Isam.Esent.Interop)
TOCTitle: Instance constructor (String)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Instance.#ctor(System.String)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.instance.instance(v=EXCHG.10)
ms:contentKeyID: 55103263
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Instance..ctor
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance constructor (String)

Initializes a new instance of the Instance class. The underlying JET\_INSTANCE is allocated, but not initialized.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub New ( _
    name As String _
)
'Usage
Dim name As String

Dim instance As New Instance(name)
```

``` csharp
public Instance(
    string name
)
```

#### Parameters

  - name  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The name of the instance. This string must be unique within a given process hosting the database engine.

## See also

#### Reference

[Instance class](dn350923\(v=exchg.10\).md)

[Instance members](dn350944\(v=exchg.10\).md)

[Instance overload](dn350946\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

