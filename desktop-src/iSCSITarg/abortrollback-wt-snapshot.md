---
title: AbortRollback method of the WT\_Snapshot class
description: Aborts the rollback of the virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a155892-5c79-4ffc-89a3-c440e76f7bde
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AbortRollback method iSCSI Software Target API
- AbortRollback method iSCSI Software Target API , WT_Snapshot class
- WT_Snapshot class iSCSI Software Target API , AbortRollback method
topic_type:
- apiref
api_name:
- WT_Snapshot.AbortRollback
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AbortRollback method of the WT\_Snapshot class

Aborts the rollback of the virtual disk.

## Syntax


```mof
void AbortRollback();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Aborting rollback does not restore the virtual disk to the pre-rollback state. The virtual disk state will be indeterminate.

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

 

 





