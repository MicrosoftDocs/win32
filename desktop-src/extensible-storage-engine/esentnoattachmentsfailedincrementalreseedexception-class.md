---
description: "Learn more about: EsentNoAttachmentsFailedIncrementalReseedException class"
title: EsentNoAttachmentsFailedIncrementalReseedException class
TOCTitle: EsentNoAttachmentsFailedIncrementalReseedException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentnoattachmentsfailedincrementalreseedexception(v=EXCHG.10)
ms:contentKeyID: 55107301
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentNoAttachmentsFailedIncrementalReseedException class

Base class for JET_err.NoAttachmentsFailedIncrementalReseed exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentStateException](./esentstateexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentNoAttachmentsFailedIncrementalReseedException _
    Inherits EsentStateException
'Usage
Dim instance As EsentNoAttachmentsFailedIncrementalReseedException
```

``` csharp
[SerializableAttribute]
public sealed class EsentNoAttachmentsFailedIncrementalReseedException : EsentStateException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentNoAttachmentsFailedIncrementalReseedException members](./esentnoattachmentsfailedincrementalreseedexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
