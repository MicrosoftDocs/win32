---
title: EsentBadDbSignatureException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentBadDbSignatureException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentbaddbsignatureexception(v=EXCHG.10)
ms:contentKeyID: 55107255
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentBadDbSignatureException class

Base class for JET\_err.BadDbSignature exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentObsoleteException](dn319668\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentBadDbSignatureException _
    Inherits EsentObsoleteException
'Usage
Dim instance As EsentBadDbSignatureException
```

``` csharp
[SerializableAttribute]
public sealed class EsentBadDbSignatureException : EsentObsoleteException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentBadDbSignatureException members](dn274012\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

