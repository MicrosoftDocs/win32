---
description: "Learn more about: EsentDeleteBackupFileFailException class"
title: EsentDeleteBackupFileFailException class
TOCTitle: EsentDeleteBackupFileFailException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentdeletebackupfilefailexception(v=EXCHG.10)
ms:contentKeyID: 55101602
ms.date: 07/30/2014
ms.topic: reference
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

Base class for JET_err.DeleteBackupFileFail exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentOperationException](./esentoperationexception-class.md)  
          [Microsoft.Isam.Esent.Interop.EsentIOException](./esentioexception-class.md)  
            Microsoft.Isam.Esent.Interop.EsentDeleteBackupFileFailException  

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

[EsentDeleteBackupFileFailException members](./esentdeletebackupfilefailexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
