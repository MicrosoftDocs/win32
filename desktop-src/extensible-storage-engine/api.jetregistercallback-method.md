---
title: Api.JetRegisterCallback method 
TOCTitle: 'JetRegisterCallback method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetRegisterCallback(Microsoft.Isam.Esent.Interop.JET_SESID,Microsoft.Isam.Esent.Interop.JET_TABLEID,Microsoft.Isam.Esent.Interop.JET_cbtyp,Microsoft.Isam.Esent.Interop.JET_CALLBACK,System.IntPtr,Microsoft.Isam.Esent.Interop.JET_HANDLE@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetregistercallback(v=EXCHG.10)
ms:contentKeyID: 55100784
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetRegisterCallback
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetRegisterCallback
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetRegisterCallback method

Allows the application to configure the database engine to issue notifications to the application for specific events. These notifications are associated with a specific table and remain in effect only until the instance containing the table is shut down using [JetTerm(JET_INSTANCE)](dn334020\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetRegisterCallback ( _
    sesid As JET_SESID, _
    tableid As JET_TABLEID, _
    cbtyp As JET_cbtyp, _
    callback As JET_CALLBACK, _
    context As IntPtr, _
    <OutAttribute> ByRef callbackId As JET_HANDLE _
)
'Usage
Dim sesid As JET_SESID
Dim tableid As JET_TABLEID
Dim cbtyp As JET_cbtyp
Dim callback As JET_CALLBACK
Dim context As IntPtr
Dim callbackId As JET_HANDLEApi.JetRegisterCallback(sesid, _
    tableid, cbtyp, callback, context, _
    callbackId)
```

``` csharp
public static void JetRegisterCallback(
    JET_SESID sesid,
    JET_TABLEID tableid,
    JET_cbtyp cbtyp,
    JET_CALLBACK callback,
    IntPtr context,
    out JET_HANDLE callbackId
)
```

#### Parameters

  - sesid  
    Type: [Microsoft.Isam.Esent.Interop.JET_SESID](hh596745\(v=exchg.10\).md)  
    
    The session to use.

<!-- end list -->

  - tableid  
    Type: [Microsoft.Isam.Esent.Interop.JET_TABLEID](hh566310\(v=exchg.10\).md)  
    
    A cursor opened on the table that the callback should be registered on.

<!-- end list -->

  - cbtyp  
    Type: [Microsoft.Isam.Esent.Interop.JET_cbtyp](hh564847\(v=exchg.10\).md)  
    
    The callback reasons for which the application wishes to receive notifications.

<!-- end list -->

  - callback  
    Type: [Microsoft.Isam.Esent.Interop.JET_CALLBACK](hh566065\(v=exchg.10\).md)  
    
    The callback function.

<!-- end list -->

  - context  
    Type: [System.IntPtr](https://docs.microsoft.com/dotnet/api/system.intptr?redirectedfrom=MSDN)  
    
    A context that will be given to the callback.

<!-- end list -->

  - callbackId  
    Type: [Microsoft.Isam.Esent.Interop.JET_HANDLE](hh558081\(v=exchg.10\).md)  
    
    A handle that can later be used to cancel the registration of the given callback function using [JetUnregisterCallback(JET_SESID, JET_TABLEID, JET_cbtyp, JET_HANDLE)](dn334019\(v=exchg.10\).md).

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

