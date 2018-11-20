---
title: Api.JetGetAttachInfoInstance method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetGetAttachInfoInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetGetAttachInfoInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE,System.String@,System.Int32,System.Int32@)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetgetattachinfoinstance(v=EXCHG.10)
ms:contentKeyID: 55100704
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetGetAttachInfoInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetGetAttachInfoInstance
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetGetAttachInfoInstance method

Used during a backup initiated by [JetBeginExternalBackupInstance(JET\_INSTANCE, BeginExternalBackupGrbit)](dn292104\(v=exchg.10\).md) to query an instance for the names of database files that should become part of the backup file set. Only databases that are currently attached to the instance using [JetAttachDatabase(JET\_SESID, String, AttachDatabaseGrbit)](dn292096\(v=exchg.10\).md) will be considered. These files may subsequently be opened using [JetOpenFileInstance(JET\_INSTANCE, String, JET\_HANDLE, Int64, Int64)](dn292230\(v=exchg.10\).md) and read using [JetReadFileInstance(JET\_INSTANCE, JET\_HANDLE, \[\], Int32, Int32)](dn332987\(v=exchg.10\).md).

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetGetAttachInfoInstance ( _
    instance As JET_INSTANCE, _
    <OutAttribute> ByRef files As String, _
    maxChars As Integer, _
    <OutAttribute> ByRef actualChars As Integer _
)
'Usage
Dim instance As JET_INSTANCE
Dim files As String
Dim maxChars As Integer
Dim actualChars As IntegerApi.JetGetAttachInfoInstance(instance, _
    files, maxChars, actualChars)
```

``` csharp
public static void JetGetAttachInfoInstance(
    JET_INSTANCE instance,
    out string files,
    int maxChars,
    out int actualChars
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET\_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to get the information for.

<!-- end list -->

  - files  
    Type: [System.String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)  
    
    Returns a list of null terminated strings describing the set of database files that should be a part of the backup file set. The list of strings returned in this buffer is in the same format as a multi-string used by the registry. Each null-terminated string is returned in sequence followed by a final null terminator.

<!-- end list -->

  - maxChars  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    Maximum number of characters to retrieve.

<!-- end list -->

  - actualChars  
    Type: [System.Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)  
    
    Actual size of the file list. If this is greater than maxChars then the list has been truncated.

## Remarks

It is important to note that this API does not return an error or warning if the output buffer is too small to accept the full list of files that should be part of the backup file set.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

