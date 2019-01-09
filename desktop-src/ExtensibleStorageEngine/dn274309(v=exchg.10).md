---
title: EsentEntryPointNotFoundException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentEntryPointNotFoundException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esententrypointnotfoundexception(v=EXCHG.10)
ms:contentKeyID: 55101642
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentEntryPointNotFoundException class

Base class for JET_err.EntryPointNotFound exceptions.

## Inheritance hierarchy

[System.Object](https://msdn.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](https://msdn.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentUsageException](dn350849\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentEntryPointNotFoundException _
    Inherits EsentUsageException
'Usage
Dim instance As EsentEntryPointNotFoundException
```

``` csharp
[SerializableAttribute]
public sealed class EsentEntryPointNotFoundException : EsentUsageException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentEntryPointNotFoundException members](dn274242\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

