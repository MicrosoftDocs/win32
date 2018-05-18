---
Description: 'Resets the Work Folders sync share metadata for the specified user.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3110fc41-eec4-4624-abf4-524a8ed9cf48'
ms.prod: 'windows-server-dev'
ms.technology:
- 'work-folders'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Repair method of the Msft\_SyncShare class'
---

# Repair method of the Msft\_SyncShare class

Resets the Work Folders sync share metadata for the specified user.

## Syntax


```mof
uint64 Repair(
  [in] string User
);
```



## Parameters

<dl> <dt>

*User* \[in\]
</dt> <dd>

The user name in "Domain\\User" format.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                           |
| Namespace<br/>                | Root\\Microsoft\\Windows\\SyncShareServer<br/>                                        |
| MOF<br/>                      | <dl> <dt>ECSServer.Mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>SyncShareSvc.dll</dt> </dl> |



## See also

<dl> <dt>

[**Msft\_SyncShare**](msft-syncshare.md)
</dt> </dl>

 

 




