---
title: EsentOutOfThreadsException class
TOCTitle: EsentOutOfThreadsException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOutOfThreadsException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentoutofthreadsexception(v=EXCHG.10)
ms:contentKeyID: 55102450
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOutOfThreadsException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOutOfThreadsException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOutOfThreadsException class

Base class for JET_err.OutOfThreads exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](dn350557\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMemoryException](dn334636\(v=exchg.10\).md)  
              Microsoft.Isam.Esent.Interop.EsentOutOfThreadsException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOutOfThreadsException _
    Inherits EsentMemoryException
'Usage
Dim instance As EsentOutOfThreadsException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOutOfThreadsException : EsentMemoryException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOutOfThreadsException members](dn319816\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

