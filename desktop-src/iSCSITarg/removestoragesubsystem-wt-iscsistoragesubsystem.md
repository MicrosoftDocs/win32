---
title: RemoveStorageSubsystem method of the WT\_iSCSIStorageSubsystem class
description: Removes an iSCSI Target Server from the list of subsystems maintained by the VDS provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a541928f-4ab2-4ec8-ad3a-17c37241775a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveStorageSubsystem method iSCSI Software Target API
- RemoveStorageSubsystem method iSCSI Software Target API , WT_iSCSIStorageSubsystem class
- WT_iSCSIStorageSubsystem class iSCSI Software Target API , RemoveStorageSubsystem method
topic_type:
- apiref
api_name:
- WT_iSCSIStorageSubsystem.RemoveStorageSubsystem
api_location:
- StrgPrvdMgmt.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveStorageSubsystem method of the WT\_iSCSIStorageSubsystem class

Removes an iSCSI Target Server from the list of subsystems maintained by the VDS provider. This is a static method.

## Syntax


```mof
uint32 RemoveStorageSubsystem(
  [in] string iSCSITargetServer
);
```



## Parameters

<dl> <dt>

*iSCSITargetServer* \[in\]
</dt> <dd>

Name of the iSCSI Target Server.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Wmi<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>StrgPrvdMgmt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StrgPrvdMgmt.dll</dt> </dl> |



## See also

<dl> <dt>

[**WT\_iSCSIStorageSubsystem**](wt-iscsistoragesubsystem.md)
</dt> </dl>

 

 





