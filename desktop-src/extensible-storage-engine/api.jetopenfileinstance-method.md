---
description: "Learn more about: Api.JetOpenFileInstance method"
title: Api.JetOpenFileInstance method 
TOCTitle: 'JetOpenFileInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetOpenFileInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE,System.String,Microsoft.Isam.Esent.Interop.JET_HANDLE@,System.Int64@,System.Int64@)
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.jetopenfileinstance(v=EXCHG.10)
ms:contentKeyID: 55100767
ms.date: 07/30/2014
ms.topic: reference
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

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](./jet-instance-structure.md)  
    
    The instance to use.

<!-- end list -->

  - file  
    Type: [System.String](/dotnet/api/system.string)  
    
    The file to open.

<!-- end list -->

  - handle  
    Type: [Microsoft.Isam.Esent.Interop.JET_HANDLE](./jet-handle-structure.md)  
    
    Returns a handle to the file.

<!-- end list -->

  - fileSizeLow  
    Type: [System.Int64](/dotnet/api/system.int64)  
    
    Returns the least significant 32 bits of the file size.

<!-- end list -->

  - fileSizeHigh  
    Type: [System.Int64](/dotnet/api/system.int64)  
    
    Returns the most significant 32 bits of the file size.

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
