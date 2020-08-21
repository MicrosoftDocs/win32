---
title: EsentTooManyOpenTablesException class
TOCTitle: EsentTooManyOpenTablesException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esenttoomanyopentablesexception(v=EXCHG.10)
ms:contentKeyID: 55107362
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentTooManyOpenTablesException class

Base class for JET_err.TooManyOpenTables exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentResourceException](dn350557\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentQuotaException](dn319806\(v=exchg.10\).md)  
              Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentTooManyOpenTablesException _
    Inherits EsentQuotaException
'Usage
Dim instance As EsentTooManyOpenTablesException
```

``` csharp
[SerializableAttribute]
public sealed class EsentTooManyOpenTablesException : EsentQuotaException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentTooManyOpenTablesException members](dn350775\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)