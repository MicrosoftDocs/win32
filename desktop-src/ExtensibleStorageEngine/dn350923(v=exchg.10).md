---
title: Instance class (Microsoft.Isam.Esent.Interop)
TOCTitle: Instance class
ms:assetid: T:Microsoft.Isam.Esent.Interop.Instance
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.instance(v=EXCHG.10)
ms:contentKeyID: 55103260
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Instance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Instance
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Instance class

A class that encapsulates a [JET\_INSTANCE](hh564593\(v=exchg.10\).md) in a disposable object. The instance must be closed last and closing the instance releases all other resources for the instance.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Runtime.ConstrainedExecution.CriticalFinalizerObject](http://msdn2.microsoft.com/en-us/library/9tcc8a46)  
    [System.Runtime.InteropServices.SafeHandle](http://msdn2.microsoft.com/en-us/library/7s3yckbh)  
      [Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid](http://msdn2.microsoft.com/en-us/library/s07831kw)  
        Microsoft.Isam.Esent.Interop.Instance  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Class Instance _
    Inherits SafeHandleZeroOrMinusOneIsInvalid
'Usage
Dim instance As Instance
```

``` csharp
public class Instance : SafeHandleZeroOrMinusOneIsInvalid
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[Instance members](dn350944\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

