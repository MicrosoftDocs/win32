---
title: EsentOutOfLongValueIDsException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentOutOfLongValueIDsException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOutOfLongValueIDsException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentoutoflongvalueidsexception(v=EXCHG.10)
ms:contentKeyID: 55102476
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOutOfLongValueIDsException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOutOfLongValueIDsException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOutOfLongValueIDsException class

Base class for JET\_err.OutOfLongValueIDs exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentFragmentationException](dn350462\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentOutOfLongValueIDsException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOutOfLongValueIDsException _
    Inherits EsentFragmentationException
'Usage
Dim instance As EsentOutOfLongValueIDsException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOutOfLongValueIDsException : EsentFragmentationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOutOfLongValueIDsException members](dn319797\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

