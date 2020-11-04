---
title: EsentMemoryException class
TOCTitle: EsentMemoryException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentMemoryException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentmemoryexception(v=EXCHG.10)
ms:contentKeyID: 55102197
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentMemoryException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentMemoryException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentMemoryException class

Base class for Memory exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](dn350557\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentMemoryException  
              

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentMemoryException _
    Inherits EsentResourceException
'Usage
Dim instance As EsentMemoryException
```

``` csharp
[SerializableAttribute]
public abstract class EsentMemoryException : EsentResourceException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentMemoryException members](dn334695\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](dn350557\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentMemoryException  
              [Microsoft.Isam.Esent.Interop.EsentOutOfBuffersException](dn319715\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentOutOfCursorsException](dn319764\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentOutOfFileHandlesException](dn319728\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentOutOfMemoryException](dn319786\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentOutOfSessionsException](dn319800\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentOutOfThreadsException](dn319762\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentTooManyMempoolEntriesException](dn350776\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentTooManyOpenIndexesException](dn350784\(v=exchg.10\).md)  
              [Microsoft.Isam.Esent.Interop.EsentTooManySortsException](dn350779\(v=exchg.10\).md)
