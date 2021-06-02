---
description: "Learn more about: EsentClientRequestToStopJetServiceException class"
title: EsentClientRequestToStopJetServiceException class
TOCTitle: EsentClientRequestToStopJetServiceException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentClientRequestToStopJetServiceException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentclientrequesttostopjetserviceexception(v=EXCHG.10)
ms:contentKeyID: 55101272
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentClientRequestToStopJetServiceException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentClientRequestToStopJetServiceException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentClientRequestToStopJetServiceException class

Base class for JET_err.ClientRequestToStopJetService exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentClientRequestToStopJetServiceException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentClientRequestToStopJetServiceException _
    Inherits EsentOperationException
'Usage
Dim instance As EsentClientRequestToStopJetServiceException
```

``` csharp
[SerializableAttribute]
public sealed class EsentClientRequestToStopJetServiceException : EsentOperationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentClientRequestToStopJetServiceException members](./esentclientrequesttostopjetserviceexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
