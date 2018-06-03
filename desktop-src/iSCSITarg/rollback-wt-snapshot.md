---
title: Rollback method of the WT\_Snapshot class
description: Rolls back the virtual disk to the most recent shadow copy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e3494e46-b264-4a96-935a-d4b7fb06c682
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rollback method iSCSI Software Target API
- Rollback method iSCSI Software Target API , WT_Snapshot class
- WT_Snapshot class iSCSI Software Target API , Rollback method
topic_type:
- apiref
api_name:
- WT_Snapshot.Rollback
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rollback method of the WT\_Snapshot class

Rolls back the virtual disk to the most recent shadow copy.

## Syntax


```mof
void Rollback();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This operation occurs asynchronously.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Snapshot**](wt-snapshot.md)
</dt> </dl>

 

 





