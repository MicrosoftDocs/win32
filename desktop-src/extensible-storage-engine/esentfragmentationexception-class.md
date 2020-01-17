---
title: EsentFragmentationException class
TOCTitle: EsentFragmentationException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentFragmentationException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentfragmentationexception(v=EXCHG.10)
ms:contentKeyID: 55101771
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentFragmentationException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentFragmentationException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentFragmentationException class

Base class for Fragmentation exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentFragmentationException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentFragmentationException _
    Inherits EsentDataException
'Usage
Dim instance As EsentFragmentationException
```

``` csharp
[SerializableAttribute]
public abstract class EsentFragmentationException : EsentDataException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentFragmentationException members](dn350419\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentFragmentationException  
            [Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchException](dn334646\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogSequenceEndDatabasesConsistentException](dn334651\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogSequenceEndException](dn334652\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOutOfAutoincrementValuesException](dn319752\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOutOfDbtimeValuesException](dn319775\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOutOfLongValueIDsException](dn319790\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOutOfObjectIDsException](dn319746\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOutOfSequentialIndexValuesException](dn319807\(v=exchg.10\).md)

