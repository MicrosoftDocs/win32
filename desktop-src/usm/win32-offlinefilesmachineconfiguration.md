---
title: Win32\_OfflineFilesMachineConfiguration class
description: Represents the Offline Files configuration for a computer.
ms.assetid: 6a8b4c5e-12c9-490d-be7c-afa0dade714a
keywords:
- Win32_OfflineFilesMachineConfiguration class User State Manageability API
- Win32_OfflineFilesMachineConfiguration class User State Manageability API , described
topic_type:
- apiref
api_name:
- Win32_OfflineFilesMachineConfiguration
- Win32_OfflineFilesMachineConfiguration.IsEffective
- Win32_OfflineFilesMachineConfiguration.OfflineFilesCacheEncrypted
- Win32_OfflineFilesMachineConfiguration.Enabled
- Win32_OfflineFilesMachineConfiguration.SyncOnCostedNetworkEnabled
- Win32_OfflineFilesMachineConfiguration.SlowLinkEnabled
- Win32_OfflineFilesMachineConfiguration.SlowLinkParams
- Win32_OfflineFilesMachineConfiguration.BackgroundSyncEnabled
- Win32_OfflineFilesMachineConfiguration.BackgroundSyncParams
- Win32_OfflineFilesMachineConfiguration.EconomicalAdminPinningEnabled
- Win32_OfflineFilesMachineConfiguration.ExcludedFileTypes
- Win32_OfflineFilesMachineConfiguration.DiskSpaceLimitEnabled
- Win32_OfflineFilesMachineConfiguration.DiskSpaceLimitParams
- Win32_OfflineFilesMachineConfiguration.WorkOfflineButtonRemoved
- Win32_OfflineFilesMachineConfiguration.MakeAvailableOfflineButtonRemoved
- Win32_OfflineFilesMachineConfiguration.TransparentCachingLatencyThreshold
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

# Win32\_OfflineFilesMachineConfiguration class

Represents the Offline Files configuration for a computer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_OfflineFilesMachineConfiguration
{
  boolean                          IsEffective;
  boolean                          OfflineFilesCacheEncrypted;
  boolean                          Enabled;
  boolean                          SyncOnCostedNetworkEnabled;
  boolean                          SlowLinkEnabled;
  string                           SlowLinkParams[];
  boolean                          BackgroundSyncEnabled;
  Win32_OfflineFilesBackgroundSync BackgroundSyncParams;
  boolean                          EconomicalAdminPinningEnabled;
  string                           ExcludedFileTypes[];
  boolean                          DiskSpaceLimitEnabled;
  Win32_OfflineFilesDiskSpaceLimit DiskSpaceLimitParams;
  boolean                          WorkOfflineButtonRemoved;
  boolean                          MakeAvailableOfflineButtonRemoved;
  uint32                           TransparentCachingLatencyThreshold;
};
```

## Members

The **Win32\_OfflineFilesMachineConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesMachineConfiguration** class has these properties.

<dl> <dt>

**BackgroundSyncEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, background synchronization is enabled as specified in the **BackgroundSyncParams** property.

</dd> <dt>

**BackgroundSyncParams**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesBackgroundSync**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If the **BackgroundSyncEnabled** property is **true**, this property is a [**Win32\_OfflineFilesBackgroundSync**](win32-offlinefilesbackgroundsync.md) object whose properties are the background synchronization parameters.

</dd> <dt>

**DiskSpaceLimitEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the disk space used by offline files is limited. The **DiskSpaceLimitParams** property determines how the disk space is managed.

</dd> <dt>

**DiskSpaceLimitParams**
</dt> <dd> <dl> <dt>

Data type: **Win32\_OfflineFilesDiskSpaceLimit**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If the **DiskSpaceLimitEnabled** property is **true**, this property is a [**Win32\_OfflineFilesDiskSpaceLimit**](win32-offlinefilesdiskspacelimit.md) object whose properties determine how the disk space is managed.

</dd> <dt>

**EconomicalAdminPinningEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, only administratively assigned offline files are synchronized when the user logs on. Files and folders that are already available offline (cached) are skipped and are synchronized later.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the Offline Files feature is enabled.

</dd> <dt>

**ExcludedFileTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array strings that specify the types of files that are excluded from being cached. Each string contains a file extension, for example ".reg". Wildcards are allowed. The array size is not fixed; the caller can specify as many file extensions as needed.

</dd> <dt>

**IsEffective**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **true**, these configuration settings are in effect.

</dd> <dt>

**MakeAvailableOfflineButtonRemoved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the **Make Available Offline** button is removed.

</dd> <dt>

**OfflineFilesCacheEncrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the Offline Files cache will be encrypted.

</dd> <dt>

**SlowLinkEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, slow-link mode is enabled as specified in the **SlowLinkParams** property.

</dd> <dt>

**SlowLinkParams**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

If the **SlowLinkEnabled** property is **true**, this property is an array of strings that contain the slow-link mode parameters.

</dd> <dt>

**SyncOnCostedNetworkEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, allow syncing to occur on a costed network where the user is charged by usage.

</dd> <dt>

**TransparentCachingLatencyThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (100000000)
</dt> </dl>

The transparent caching latency, in milliseconds. Transparent caching allows the optimization of network files reads by caching them. Subsequent reads of the same files are satisfied from the cache after verifying the integrity of the cached copy.

This property specifies the latency value that triggers transparent caching.

</dd> <dt>

**WorkOfflineButtonRemoved**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **true**, the **Work Offline** button is removed.

</dd> </dl>

## Remarks

This class requires a context object to be passed as the *pCtx* parameter to the [**IWbemServices::GetObject**](https://msdn.microsoft.com/library/aa392109) method. This context object has the following properties, which should be set to the following values:



| Property Name                                 | Type     | Specify This Value               |
|-----------------------------------------------|----------|----------------------------------|
| PolicyPlatformContext\_PrincipalContext\_Type | VT\_BSTR | "PolicyPlatform\_MachineContext" |
| PolicyPlatformContext\_PrincipalContext\_Id   | VT\_BSTR | "SYSTEM"                         |



 

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                              |
| MOF<br/>                      | <dl> <dt>OfflineFilesConfigurationWmiProvider.mof</dt> </dl> |



 

 





