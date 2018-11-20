---
title: EsentDeleteBackupFileFailException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentDeleteBackupFileFailException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentdeletebackupfilefailexception(v=EXCHG.10)
ms:contentKeyID: 55101602
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentDeleteBackupFileFailException class

Base class for JET\_err.DeleteBackupFileFail exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](dn319727\(v=exchg.10\).md)  
          [Microsoft.Isam.Esent.Interop.EsentIOException](dn319595\(v=exchg.10\).md)  
            Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public NotInheritable Class EsentDeleteBackupFileFailException _
    Inherits EsentIOException
'Usage
Dim instance As EsentDeleteBackupFileFailException
```

``` csharp
[SerializableAttribute]
public sealed class EsentDeleteBackupFileFailException : EsentIOException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentDeleteBackupFileFailException members](dn334434\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

