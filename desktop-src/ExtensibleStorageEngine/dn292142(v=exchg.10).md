---
title: Api.JetEndExternalBackupInstance method  (Microsoft.Isam.Esent.Interop)
TOCTitle: 'JetEndExternalBackupInstance method '
ms:assetid: M:Microsoft.Isam.Esent.Interop.Api.JetEndExternalBackupInstance(Microsoft.Isam.Esent.Interop.JET_INSTANCE)
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.api.jetendexternalbackupinstance(v=EXCHG.10)
ms:contentKeyID: 55100691
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.JetEndExternalBackupInstance
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Api.JetEndExternalBackupInstance
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# Api.JetEndExternalBackupInstance method

Ends an external backup session. This API is the last API in a series of APIs that must be called to execute a successful online (non-VSS based) backup.

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Shared Sub JetEndExternalBackupInstance ( _
    instance As JET_INSTANCE _
)
'Usage
Dim instance As JET_INSTANCEApi.JetEndExternalBackupInstance(instance)
```

``` csharp
public static void JetEndExternalBackupInstance(
    JET_INSTANCE instance
)
```

#### Parameters

  - instance  
    Type: [Microsoft.Isam.Esent.Interop.JET\_INSTANCE](hh564593\(v=exchg.10\).md)  
    
    The instance to end the backup for.

## See also

#### Reference

[Api class](dn292211\(v=exchg.10\).md)

[Api members](dn292213\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

