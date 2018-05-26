---
title: Win32\_OfflineFilesBackgroundSync class
description: Represents a background synchronization operation.
ms.assetid: 8bbee4fa-5858-40e0-8533-1c4794655716
keywords:
- Win32_OfflineFilesBackgroundSync class User State Manageability API
- Win32_OfflineFilesBackgroundSync class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_OfflineFilesBackgroundSync
- Win32_OfflineFilesBackgroundSync.SyncInterval
- Win32_OfflineFilesBackgroundSync.SyncVariance
- Win32_OfflineFilesBackgroundSync.MaxTimeBetweenSyncs
- Win32_OfflineFilesBackgroundSync.BlockOutStartTimeHoursMinutes
- Win32_OfflineFilesBackgroundSync.BlockOutDurationMin
- Win32_OfflineFilesBackgroundSync.BackgroundSyncWorkOfflineSharesEnabled
api_location:
- Root\CIMv2
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_OfflineFilesBackgroundSync class

Represents a background synchronization operation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_OfflineFilesBackgroundSync
{
  uint16  SyncInterval;
  uint16  SyncVariance;
  uint16  MaxTimeBetweenSyncs;
  uint16  BlockOutStartTimeHoursMinutes;
  uint16  BlockOutDurationMin;
  boolean BackgroundSyncWorkOfflineSharesEnabled;
};
```

## Members

The **Win32\_OfflineFilesBackgroundSync** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesBackgroundSync** class has these properties.

<dl> <dt>

**BackgroundSyncWorkOfflineSharesEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, enable background synchronization for shares that the user has forced into "work offline" mode.

</dd> <dt>

**BlockOutDurationMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (1440)
</dt> </dl>

The length of time, in minutes, when background synchronization is disabled. This property is used together with the **BlockOutStartTimeHoursMinutes** property.

</dd> <dt>

**BlockOutStartTimeHoursMinutes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (2400)
</dt> </dl>

The time of the day when background synchronization is disabled. This property is used together with the **BlockOutDurationMin** property. The format of this property is: *HHMM*. The first two digits of this **uint16** value are hours (00-24) and the third and fourth digits are minutes (00-59).

</dd> <dt>

**MaxTimeBetweenSyncs**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum time, in minutes, until a synchronization operation must start.

</dd> <dt>

**SyncInterval**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (1440)
</dt> </dl>

The synchronization interval, in minutes. This property is used together with the **SyncVariance** property. Together, these properties specify how often the synchronization operation is performed.

</dd> <dt>

**SyncVariance**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (3600)
</dt> </dl>

The amount of time, in minutes, by which the synchronization interval can vary. This property is used together with the **SyncInterval** property. For example, if the value of the **SyncInterval** property is 60 and the value of the **SyncVariance** property is 10, the synchronization operation can start any time between 60 and 70 minutes after the beginning of the previous synchronization operation.

</dd> </dl>

## Remarks

For redirected folders in offline (slow-link) mode, a synchronization operation is initiated in the background on a regular basis, according to these settings. This operation synchronizes the files in the redirected folders on the client with the copies on the server.

By default, network folders in offline mode will be synchronized with the server every 360 minutes with the start of the sync varying between 0 and 60 additional minutes.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                              |
| MOF<br/>                      | <dl> <dt>OfflineFilesConfigurationWmiProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_RoamingProfileMachineConfiguration**](win32-roamingprofilemachineconfiguration.md)
</dt> </dl>

 

 





