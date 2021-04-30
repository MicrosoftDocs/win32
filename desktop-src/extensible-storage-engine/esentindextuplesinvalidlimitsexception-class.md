---
description: "Learn more about: EsentIndexTuplesInvalidLimitsException class"
title: EsentIndexTuplesInvalidLimitsException class
TOCTitle: EsentIndexTuplesInvalidLimitsException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentindextuplesinvalidlimitsexception(v=EXCHG.10)
ms:contentKeyID: 55101849
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentIndexTuplesInvalidLimitsException class

Base class for JET_err.IndexTuplesInvalidLimits exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](./esentusageexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentIndexTuplesInvalidLimitsException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentIndexTuplesInvalidLimitsException
```

``` csharp
[SerializableAttribute]
public sealed class EsentIndexTuplesInvalidLimitsException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentIndexTuplesInvalidLimitsException members](./esentindextuplesinvalidlimitsexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
