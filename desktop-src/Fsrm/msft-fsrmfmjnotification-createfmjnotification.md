---
title: CreateFMJNotification method of the MSFT\_FSRMFMJNotification class
description: Creates an instance of the MSFT\_FSRMFMJNotification class representing a file management job notification.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0c1bafe2-db1a-4325-8ce9-24b22b30a2d4
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateFMJNotification method File Server Resource Manager
- CreateFMJNotification method File Server Resource Manager , MSFT_FSRMFMJNotification class
- MSFT_FSRMFMJNotification class File Server Resource Manager , CreateFMJNotification method
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJNotification.CreateFMJNotification
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateFMJNotification method of the MSFT\_FSRMFMJNotification class

Creates an instance of the [**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md) class representing a file management job notification.

## Syntax


```mof
uint64 CreateFMJNotification(
  [in]  uint32                         Days,
  [in]  MSFT_FSRMFMJNotificationAction Action[],
  [out] MSFT_FSRMFMJNotification       Notification
);
```



## Parameters

<dl> <dt>

*Days* \[in\]
</dt> <dd>

A unique notification value to add. The value cannot be less than zero.

The *Days* parameter specifies the number of days before the file is to expire. If the appropriate conditions set in the job are met, notification will be sent to the user to let them know that the file is about to expire. FSRM uses the actions associated with the notification value to determine how the user is notified.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

An array of [**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md) instance that represent the actions that the file management job will perform when the notification happens.

</dd> <dt>

*Notification* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md) class representing the created file management job notification.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md)
</dt> <dt>

[**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md)
</dt> <dt>

[**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md)
</dt> </dl>

 

 





