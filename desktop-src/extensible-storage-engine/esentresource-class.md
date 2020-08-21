---
title: EsentResource class
TOCTitle: EsentResource class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentResource
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentresource(v=EXCHG.10)
ms:contentKeyID: 55102575
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentResource
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentResource
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentResource class

This is the base class for all esent resource objects. Subclasses of this class can allocate and release unmanaged resources.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  Microsoft.Isam.Esent.Interop.EsentResource  
    [Microsoft.Isam.Esent.Interop.Session](dn351164\(v=exchg.10\).md)  
    [Microsoft.Isam.Esent.Interop.Table](dn351163\(v=exchg.10\).md)  
    [Microsoft.Isam.Esent.Interop.Transaction](dn351174\(v=exchg.10\).md)  
    [Microsoft.Isam.Esent.Interop.Update](dn351191\(v=exchg.10\).md)  
    [Microsoft.Isam.Esent.Interop.Windows8.DurableCommitCallback](dn335323\(v=exchg.10\).md)  

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public MustInherit Class EsentResource _
    Implements IDisposable
'Usage
Dim instance As EsentResource
```

``` csharp
public abstract class EsentResource : IDisposable
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentResource members](dn350521\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)