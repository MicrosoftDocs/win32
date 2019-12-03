---
title: Api.JetGetTruncateLogInfoInstance method 
TOCTitle: 'JetGetTruncateLogInfoInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetTruncateLogInfoInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE,System.String@,System.Int32,System.Int32@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgettruncateloginfoinstance(v=EXCHG.10)
ms:contentKeyID: 55100743
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetGetTruncateLogInfoInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetTruncateLogInfoInstance
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetTruncateLogInfoInstance method

Used during a backup initiated by [JetBeginExternalBackupInstance(JET_INSTANCE, BeginExternalBackupGrbit)](dn292104\(v=exchg.10\).md) to query an instance for the names of the transaction log files that can be safely deleted after the backup has successfully completed.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetTruncateLogInfoInstance ( _
    instance As JET_INSTANCE, _
    <OutAttribute> ByRef files As String, _
    maxChars As Integer, _
    <OutAttribute> ByRef actualChars As Integer _
)
'Usage
Dim instance As JET_INSTANCE
Dim files As String
Dim maxChars As Integer
Dim actualChars As IntegerApi.JetGetTruncateLogInfoInstance(instance, _
    files, maxChars, actualChars)
```

``` csharp
public static void JetGetTruncateLogInfoInstance(
    JET_INSTANCE instance,
    out string files,
    int maxChars,
    out int actualChars
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to get the information for.

<!-- end list -->

  - files  
    Type: [System.String](https://docs.microsoft.com/dotnet/api/system.string?redirectedfrom=MSDN)  
    
    Returns a list of null terminated strings describing the set of database log files that can be safely deleted after the backup completes. The list of strings returned in this buffer is in the same format as a multi-string used by the registry. Each null-terminated string is returned in sequence followed by a final null terminator.

<!-- end list -->

  - maxChars  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    Maximum number of characters to retrieve.

<!-- end list -->

  - actualChars  
    Type: [System.Int32](https://docs.microsoft.com/dotnet/api/system.int32?redirectedfrom=MSDN)  
    
    Actual size of the file list. If this is greater than maxChars then the list has been truncated.

## Remarks

It is important to note that this API does not return an error or warning if the output buffer is too small to accept the full list of files that should be part of the backup file set.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

