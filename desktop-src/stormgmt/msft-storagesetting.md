---
title: MSFT\_StorageSetting class
description: Represents various operating system-wide settings related to storage management.
ms.assetid: 5F956BBF-8FAB-44B2-A2C0-F234813D979B
keywords:
- MSFT_StorageSetting class Windows Storage Management API
- MSFT_StorageSetting class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSetting
- MSFT_StorageSetting.NewDiskPolicy
- MSFT_StorageSetting.ScrubPolicy
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSetting class

Represents various operating system-wide settings related to storage management.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageSetting
{
  UInt16 NewDiskPolicy;
  UInt32 ScrubPolicy;
};
```

## Members

The **MSFT\_StorageSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageSetting** class has these methods.



| Method                                                                       | Description                                                                                                              |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**Get**](msft-storagesetting-get.md)                                       | Retrieves the current state of all storage settings for the computer.<br/>                                         |
| [**Set**](msft-storagesetting-set.md)                                       | Sets the state of various storage settings on this computer.<br/>                                                  |
| [**UpdateHostStorageCache**](msft-storagesetting-updatehoststoragecache.md) | Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting.<br/> |



 

### Properties

The **MSFT\_StorageSetting** class has these properties.

<dl> <dt>

**NewDiskPolicy**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the action the operating system will take when a new disk is discovered on the system. When a disk is offline, the disk layout can be read, but no volume devices are surfaced through Plug and Play (PnP). This means that no file system can be mounted on the disk. When a disk is online, one or more volume devices are installed for the disk.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                     | The disk policy is not specified.<br/>                                                                     |
| <span id="Online_All"></span><span id="online_all"></span><span id="ONLINE_ALL"></span><dl> <dt>**Online All**</dt> <dt>1</dt> </dl>                         | All newly discovered disks are brought online and made read/write.<br/>                                    |
| <span id="Offline_Shared"></span><span id="offline_shared"></span><span id="OFFLINE_SHARED"></span><dl> <dt>**Offline Shared**</dt> <dt>2</dt> </dl>         | All newly discovered disks that do not reside on a shared bus are brought online and made read/write.<br/> |
| <span id="Offline_All"></span><span id="offline_all"></span><span id="OFFLINE_ALL"></span><dl> <dt>**Offline All**</dt> <dt>3</dt> </dl>                     | All newly discovered disks remain offline and read-only.<br/>                                              |
| <span id="Offline_Internal"></span><span id="offline_internal"></span><span id="OFFLINE_INTERNAL"></span><dl> <dt>**Offline Internal**</dt> <dt>4</dt> </dl> | All newly discovered disks that do not reside on a shared bus remain offline and read-only.<br/>           |



 

</dd> <dt>

**ScrubPolicy**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the policy for the files that the automatic data integrity scanner will scrub.

<dl> <dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>**Off** (0)
</dt> <dt>

<span id="Integrity_Streams"></span><span id="integrity_streams"></span><span id="INTEGRITY_STREAMS"></span>**Integrity Streams** (1)
</dt> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>**All** (2)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





