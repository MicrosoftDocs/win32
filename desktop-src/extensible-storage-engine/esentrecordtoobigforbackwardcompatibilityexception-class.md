---
title: EsentRecordTooBigForBackwardCompatibilityException class
TOCTitle: EsentRecordTooBigForBackwardCompatibilityException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentrecordtoobigforbackwardcompatibilityexception(v=EXCHG.10)
ms:contentKeyID: 55102602
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentRecordTooBigForBackwardCompatibilityException class

Base class for JET_err.RecordTooBigForBackwardCompatibility exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentStateException](dn334920\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentRecordTooBigForBackwardCompatibilityException _
    Inherits EsentStateException
'Usage
Dim instance As EsentRecordTooBigForBackwardCompatibilityException
```

``` csharp
[SerializableAttribute]
public sealed class EsentRecordTooBigForBackwardCompatibilityException : EsentStateException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentRecordTooBigForBackwardCompatibilityException members](dn350532\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)