---
title: EsentIOException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentIOException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentIOException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentioexception(v=EXCHG.10)
ms:contentKeyID: 55102033
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentIOException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentIOException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentIOException class

Base class for IO exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentIOException  
            [Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException](dn274267\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDiskIOException](dn274289\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileAccessDeniedException](dn274324\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogWriteFailException](dn334607\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMakeBackupDirectoryFailException](dn334692\(v=exchg.10\).md)  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentIOException _
    Inherits EsentOperationException
'Usage
Dim instance As EsentIOException
```

``` csharp
[SerializableAttribute]
public abstract class EsentIOException : EsentOperationException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentIOException members](dn334537\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

