---
description: "Learn more about: EsentOutOfDbtimeValuesException class"
title: EsentOutOfDbtimeValuesException class
TOCTitle: EsentOutOfDbtimeValuesException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentOutOfDbtimeValuesException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentoutofdbtimevaluesexception(v=EXCHG.10)
ms:contentKeyID: 55102463
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentOutOfDbtimeValuesException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentOutOfDbtimeValuesException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentOutOfDbtimeValuesException class

Base class for JET_err.OutOfDbtimeValues exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentFragmentationException](./esentfragmentationexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentOutOfDbtimeValuesException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentOutOfDbtimeValuesException _
    Inherits EsentFragmentationException
'Usage
Dim instance As EsentOutOfDbtimeValuesException
```

``` csharp
[SerializableAttribute]
public sealed class EsentOutOfDbtimeValuesException : EsentFragmentationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentOutOfDbtimeValuesException members](./esentoutofdbtimevaluesexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
