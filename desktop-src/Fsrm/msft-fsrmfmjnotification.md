---
title: MSFT\_FSRMFMJNotification class
description: Represents a file management job notification.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a9fedf6-afe3-4be3-8d93-4766f7453bec
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMFMJNotification class File Server Resource Manager
- MSFT_FSRMFMJNotification class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJNotification
- MSFT_FSRMFMJNotification.Days
- MSFT_FSRMFMJNotification.Action
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_FSRMFMJNotification class

Represents a file management job notification.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFMJNotification
{
  uint32                         Days;
  MSFT_FSRMFMJNotificationAction Action[];
};
```

## Members

The **MSFT\_FSRMFMJNotification** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFMJNotification** class has these methods.



| Method                                                                          | Description                                                                                                                |
|:--------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**CreateFMJNotification**](msft-fsrmfmjnotification-createfmjnotification.md) | Creates an instance of the **MSFT\_FSRMFMJNotification** class representing a file management job notification.<br/> |



 

### Properties

The **MSFT\_FSRMFMJNotification** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMFMJNotificationAction** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md)")
</dt> </dl>

An array of [**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md) instances that represent the actions that the file management job will perform when the notification happens.

</dd> <dt>

**Days**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A unique notification value to add. The value cannot be less than zero.

The **Days** property specifies the number of days before the file is to expire. If the appropriate conditions set in the job are met, notification will be sent to the user to let them know that the file is about to expire. FSRM uses the actions associated with the notification value to determine how the user is notified.

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

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 





