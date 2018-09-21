---
title: Api.JetOpenFileInstance method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetOpenFileInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetOpenFileInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE,System.String,Microsoft.Isam.Esent.Interop.JET_HANDLE@,System.Int64@,System.Int64@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetopenfileinstance(v=EXCHG.10)
ms:contentKeyID: 55100767
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetOpenFileInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetOpenFileInstance
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetOpenFileInstance method

Opens an attached database, database patch file, or transaction log file of an active instance for the purpose of performing a streaming fuzzy backup. The data from these files can subsequently be read through the returned handle using JetReadFileInstance. The returned handle must be closed using JetCloseFileInstance. An external backup of the instance must have been previously initiated using JetBeginExternalBackupInstance.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetOpenFileInstance ( _
    instance As JET_INSTANCE, _
    file As String, _
    <OutAttribute> ByRef handle As JET_HANDLE, _
    <OutAttribute> ByRef fileSizeLow As Long, _
    <OutAttribute> ByRef fileSizeHigh As Long _
)
'Usage
Dim instance As JET_INSTANCE
Dim file As String
Dim handle As JET_HANDLE
Dim fileSizeLow As Long
Dim fileSizeHigh As LongApi.JetOpenFileInstance(instance, _
    file, handle, fileSizeLow, fileSizeHigh)
```

``` csharp
public static void JetOpenFileInstance(
    JET_INSTANCE instance,
    string file,
    out JET_HANDLE handle,
    out long fileSizeLow,
    out long fileSizeHigh
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET\_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to use.

<!-- end list -->

  - file  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    The file to open.

<!-- end list -->

  - handle  
    Type: [Microsoft.Isam.Esent.Interop.JET\_HANDLE](hh558081\(v=exchg.10\).md)  
    
    Returns a handle to the file.

<!-- end list -->

  - fileSizeLow  
    Type: [System.Int64](http://msdn2.microsoft.com/en-us/library/6yy583ek)  
    
    Returns the least significant 32 bits of the file size.

<!-- end list -->

  - fileSizeHigh  
    Type: [System.Int64](http://msdn2.microsoft.com/en-us/library/6yy583ek)  
    
    Returns the most significant 32 bits of the file size.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

