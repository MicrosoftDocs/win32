---
title: EsentRequiredLogFilesMissingException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentRequiredLogFilesMissingException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentrequiredlogfilesmissingexception(v=EXCHG.10)
ms:contentKeyID: 55102617
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentRequiredLogFilesMissingException class

Base class for JET\_err.RequiredLogFilesMissing exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentInconsistentException](dn350488\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentRequiredLogFilesMissingException _
    Inherits EsentInconsistentException
'Usage
Dim instance As EsentRequiredLogFilesMissingException
```

``` csharp
[SerializableAttribute]
public sealed class EsentRequiredLogFilesMissingException : EsentInconsistentException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentRequiredLogFilesMissingException members](dn350519\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

