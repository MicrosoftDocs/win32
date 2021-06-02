---
description: "Learn more about: Instance constructor (String, String, TermGrbit)"
title: Instance constructor (String, String, TermGrbit)
TOCTitle: Instance constructor (String, String, TermGrbit)
ms:assetid: M:Microsoft.Isam.Esent.Interop.Instance.#ctor(System.String,System.String,Microsoft.Isam.Esent.Interop.TermGrbit)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.instance.instance(v=EXCHG.10)
ms:contentKeyID: 55103289
ms.date: 07/30/2014
ms.topic: reference
dev_langs:
- vb
- csharp
api_name: 
- Microsoft.Isam.Esent.Interop.Instance..ctor
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance constructor (String, String, TermGrbit)

Initializes a new instance of the Instance class. The underlying JET_INSTANCE is allocated, but not initialized.

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Sub New ( _
    name As String, _
    displayName As String, _
    termGrbit As TermGrbit _
)
'Usage
Dim name As String
Dim displayName As String
Dim termGrbit As TermGrbit

Dim instance As New Instance(name, displayName, _
    termGrbit)
```

``` csharp
public Instance(
    string name,
    string displayName,
    TermGrbit termGrbit
)
```

#### Parameters

  - name  
    Type: [System.String](/dotnet/api/system.string)  
    
    The name of the instance. This string must be unique within a given process hosting the database engine.

<!-- end list -->

  - displayName  
    Type: [System.String](/dotnet/api/system.string)  
    
    A display name for the instance. This will be used in eventlog entries.

<!-- end list -->

  - termGrbit  
    Type: [Microsoft.Isam.Esent.Interop.TermGrbit](./termgrbit-enumeration.md)  
    
    The TermGrbit to be used at JetTerm time.

## See also

#### Reference

[Instance class](./instance-class.md)

[Instance members](./instance-members.md)

[Instance overload](./instance-constructor.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
