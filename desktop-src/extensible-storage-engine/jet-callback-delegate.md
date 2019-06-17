---
title: JET_CALLBACK delegate (Microsoft.Isam.Esent.Interop)
TOCTitle: JET_CALLBACK delegate
ms:assetid: T:Microsoft.Isam.Esent.Interop.JET_CALLBACK
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.jet_callback(v=EXCHG.10)
ms:contentKeyID: 39515752
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.JET_CALLBACK
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.JET_CALLBACK.BeginInvoke
- Microsoft.Isam.Esent.Interop.JET_CALLBACK
- Microsoft.Isam.Esent.Interop.JET_CALLBACK.EndInvoke
- Microsoft.Isam.Esent.Interop.JET_CALLBACK..ctor
- Microsoft.Isam.Esent.Interop.JET_CALLBACK.Invoke
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_CALLBACK delegate

A multi-purpose callback function used by the database engine to inform the application of an event involving online defragmentation and cursor state notifications.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Delegate Function JET_CALLBACK ( _
    sesid As JET_SESID, _
    dbid As JET_DBID, _
    tableid As JET_TABLEID, _
    cbtyp As JET_cbtyp, _
    arg1 As Object, _
    arg2 As Object, _
    context As IntPtr, _
    unused As IntPtr _
) As JET_err
'Usage
Dim instance As New JET_CALLBACK(AddressOf HandlerMethod)
```

``` csharp
public delegate JET_err JET_CALLBACK(
    JET_SESID sesid,
    JET_DBID dbid,
    JET_TABLEID tableid,
    JET_cbtyp cbtyp,
    Object arg1,
    Object arg2,
    IntPtr context,
    IntPtr unused
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session for which the callback is being made.

<!-- end list -->

  - dbid  
    Type: [Microsoft.Isam.Esent.Interop.JET_DBID](hh596176\(v=exchg.10\).md)  
    
    The database for which the callback is being made.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    The cursor for which the callback is being made.

<!-- end list -->

  - cbtyp  
    Type: [Microsoft.Isam.Esent.Interop.JET_cbtyp](hh564847\(v=exchg.10\).md)  
    
    The operation for which the callback is being made.

<!-- end list -->

  - arg1  
    Type: [System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
    
    First callback-specific argument.

<!-- end list -->

  - arg2  
    Type: [System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
    
    Second callback-specific argument.

<!-- end list -->

  - context  
    Type: [System.IntPtr](https://docs.microsoft.com/dotnet/api/system.intptr?redirectedfrom=MSDN)  
    
    Callback context.

<!-- end list -->

  - unused  
    Type: [System.IntPtr](https://docs.microsoft.com/dotnet/api/system.intptr?redirectedfrom=MSDN)  
    
    This parameter is not used.

#### Return value

Type: [Microsoft.Isam.Esent.Interop.JET_err](hh564840\(v=exchg.10\).md)  

## See also

#### Reference

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

