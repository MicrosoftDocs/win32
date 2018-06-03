---
title: WT\_Volume class
description: Represents the volumes that are suitable to host iSCSI virtual disks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89c120be-2b6d-468b-9e7c-9cc1634bcb28
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_Volume class iSCSI Software Target API
- WT_Volume class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_Volume
- WT_Volume.DeviceID
- WT_Volume.ResourceGroup
- WT_Volume.MountPoint
- WT_Volume.FileSystem
- WT_Volume.IsOnDynamicDisk
- WT_Volume.TotalSize
api_location:
- WtWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WT\_Volume class

Represents the volumes that are suitable to host iSCSI virtual disks.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_Volume
{
  string  DeviceID;
  string  ResourceGroup;
  string  MountPoint;
  string  FileSystem;
  boolean IsOnDynamicDisk;
  uint64  TotalSize;
};
```

## Members

The **WT\_Volume** class has these types of members:

-   [Properties](#properties)

### Properties

The **WT\_Volume** class has these properties.

<dl> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A string that uniquely identifies the volume on the computer.

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file system that is mounted on the volume.

</dd> <dt>

**IsOnDynamicDisk**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Deprecated; do not use.

</dd> <dt>

**MountPoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A volume mount point for the volume.

</dd> <dt>

**ResourceGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the cluster group that this volume belongs to. If the Microsoft iSCSI Target Server service is not running on a Microsoft Failover Cluster, this property is an empty string.

</dd> <dt>

**TotalSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total volume size, in megabytes.

</dd> </dl>

## Remarks

In a clustering configuration, only shared storage or volumes can be used for storing iSCSI virtual disks.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



 

 





