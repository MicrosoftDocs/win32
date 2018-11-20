---
title: EsentRollbackErrorException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentRollbackErrorException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentRollbackErrorException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentrollbackerrorexception(v=EXCHG.10)
ms:contentKeyID: 55102663
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentRollbackErrorException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentRollbackErrorException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentRollbackErrorException class

Base class for JET\_err.RollbackError exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentFatalException](dn274321\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentRollbackErrorException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentRollbackErrorException _
    Inherits EsentFatalException
'Usage
Dim instance As EsentRollbackErrorException
```

``` csharp
[SerializableAttribute]
public sealed class EsentRollbackErrorException : EsentFatalException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentRollbackErrorException members](dn350570\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

