---
title: EsentOutOfAutoincrementValuesException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentOutOfAutoincrementValuesException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOutOfAutoincrementValuesException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentoutofautoincrementvaluesexception(v=EXCHG.10)
ms:contentKeyID: 55102440
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOutOfAutoincrementValuesException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOutOfAutoincrementValuesException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOutOfAutoincrementValuesException class

Base class for JET\_err.OutOfAutoincrementValues exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentFragmentationException](dn350462\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentOutOfAutoincrementValuesException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOutOfAutoincrementValuesException _
    Inherits EsentFragmentationException
'Usage
Dim instance As EsentOutOfAutoincrementValuesException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOutOfAutoincrementValuesException : EsentFragmentationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOutOfAutoincrementValuesException members](dn319754\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

