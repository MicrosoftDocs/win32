---
title: JET_PFNSTATUS delegate (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_PFNSTATUS delegate
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_PFNSTATUS
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_pfnstatus(v=EXCHG.10)
ms:contentKeyID: 39515654
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS..ctor
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS.EndInvoke
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS.Invoke
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS
- Microsoft.Isam.Esent.Interop.JET_PFNSTATUS.BeginInvoke
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET\_PFNSTATUS delegate

Receives information about the progress of long-running operations, such as defragmentation, backup, or restore operations. During such operations, the database engine calls this callback function to give an update on the progress of the operation.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Delegate Function JET_PFNSTATUS ( _
    sesid As JET_SESID, _
    snp As JET_SNP, _
    snt As JET_SNT, _
    data As Object _
) As JET_err
'Usage
Dim instance As New JET_PFNSTATUS(AddressOf HandlerMethod)
```

``` csharp
public delegate JET_err JET_PFNSTATUS(
    JET_SESID sesid,
    JET_SNP snp,
    JET_SNT snt,
    Object data
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SESID](hh596745\(v=exchg.10\).md)  
    
    The session with which the long running operation was called.

<!-- end list -->

  - snp  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SNP](hh577944\(v=exchg.10\).md)  
    
    The type of operation.

<!-- end list -->

  - snt  
    Type: [Microsoft.Isam.Esent.Interop.JET\_SNT](hh577987\(v=exchg.10\).md)  
    
    The status of the operation.

<!-- end list -->

  - data  
    Type: [System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
    
    Optional data. May be a [JET\_SNPROG](dn351044\(v=exchg.10\).md).

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET\_err](hh564840\(v=exchg.10\).md)  

## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

