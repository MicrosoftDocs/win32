---
title: EsentException class (Microsoft.Isam.Esent)
TOCTitle: EsentException class
ms:assetid: T:Microsoft.Isam.Esent.EsentException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.esentexception(v=EXCHG.10)
ms:contentKeyID: 55100645
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.EsentException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.EsentException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentException class

Base class for ESENT exceptions.

## Inheritance hierarchy

[System.Object](https://msdn.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](https://msdn.microsoft.com/en-us/library/c18k6c59)  
    Microsoft.Isam.Esent.EsentException  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentInvalidColumnException](dn319487\(v=exchg.10\).md)  

**Namespace:**  [Microsoft.Isam.Esent](dn292085\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentException _
    Inherits Exception
'Usage
Dim instance As EsentException
```

``` csharp
[SerializableAttribute]
public abstract class EsentException : Exception
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentException members](dn292086\(v=exchg.10\).md)

[Microsoft.Isam.Esent namespace](dn292085\(v=exchg.10\).md)

