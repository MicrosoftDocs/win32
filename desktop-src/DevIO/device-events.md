---
description: Applications, including services, can register to receive notification of device events.
ms.assetid: c89da4ac-57dd-4d95-ac86-3eb137dee0bc
title: Device Events (IoEvent.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Device Events (IoEvent.h)

Applications, including services, can register to receive notification of device events. For example, a catalog service can receive notice of volumes being mounted or dismounted so it can adjust the paths to files on the volume. The system notifies an application that a device event has occurred by sending the application a [**WM\_DEVICECHANGE**](wm-devicechange.md) message. The system notifies a service that a device event has occurred by invoking the service's event handler function, [**HandlerEx**](/windows/desktop/api/winsvc/nc-winsvc-lphandler_function_ex).

To receive device event notices, call the [**RegisterDeviceNotification**](/windows/desktop/api/Winuser/nf-winuser-registerdevicenotificationa) function with a [**DEV\_BROADCAST\_HANDLE**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_handle) structure. Be sure to set the **dbch\_handle** member to the device handle obtained from the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function. Also, set the **dbch\_devicetype** member to **DBT\_DEVTYP\_HANDLE**. The function returns a device notification handle. Note that this is not the same as the volume handle.

When your application receives notification, if the event type is [DBT\_CUSTOMEVENT](dbt-customevent.md), you may have received one of the device events defined in IoEvent.h. To determine if one of these events has occurred, use the following steps.

1.  Treat the event data as a [**DEV\_BROADCAST\_HDR**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_hdr) structure. Verify that the **dbch\_devicetype** member is set to **DBT\_DEVTYP\_HANDLE**.
2.  If **dbch\_devicetype** is **DBT\_DEVTYP\_HANDLE**, the event data is really a pointer to a [**DEV\_BROADCAST\_HANDLE**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_handle) structure.
3.  Compare the **dbch\_eventguid** member to the **GUID**s listed in the following table using the [**IsEqualGUID**](/windows/win32/api/guiddef/nf-guiddef-isequalguid) function.

<dl> <dt>

<span id="GUID_IO_CDROM_EXCLUSIVE_LOCK"></span><span id="guid_io_cdrom_exclusive_lock"></span>**GUID\_IO\_CDROM\_EXCLUSIVE\_LOCK**
</dt> <dd> <dl> <dt>

bc56c139-7a10-47ee-a294-4c6a38f0149a
</dt> <dt>



The CD-ROM device has been locked for exclusive access.

**Windows Server 2003 and Windows XP:** Support for this value requires IMAPI 2.0. For more information, see [Image Mastering API](/windows/desktop/imapi/portal).


</dt> </dl> </dd> <dt>

<span id="GUID_IO_CDROM_EXCLUSIVE_UNLOCK"></span><span id="guid_io_cdrom_exclusive_unlock"></span>**GUID\_IO\_CDROM\_EXCLUSIVE\_UNLOCK**
</dt> <dd> <dl> <dt>

a3b6d27d-5e35-4885-81e5-ee18c00ed779
</dt> <dt>



A CD-ROM device that was locked for exclusive access has been unlocked.

**Windows Server 2003 and Windows XP:** Support for this value requires IMAPI 2.0. For more information, see [Image Mastering API](/windows/desktop/imapi/portal).


</dt> </dl> </dd> <dt>

<span id="GUID_IO_DEVICE_BECOMING_READY"></span><span id="guid_io_device_becoming_ready"></span>**GUID\_IO\_DEVICE\_BECOMING\_READY**
</dt> <dd> <dl> <dt>

d07433f0-a98e-11d2-917a-00a0c9068ff3
</dt> <dt>



Media spin-up is in progress.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_DEVICE_EXTERNAL_REQUEST"></span><span id="guid_io_device_external_request"></span>**GUID\_IO\_DEVICE\_EXTERNAL\_REQUEST**
</dt> <dd> <dl> <dt>

d07433d0-a98e-11d2-917a-00a0c9068ff3
</dt> <dt>



There are several possible causes for this event; for more information, refer to the T10 MMC specification of the GET EVENT STATUS NOTIFICATION Command.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_MEDIA_ARRIVAL"></span><span id="guid_io_media_arrival"></span>**GUID\_IO\_MEDIA\_ARRIVAL**
</dt> <dd> <dl> <dt>

d07433c0-a98e-11d2-917a-00a0c9068ff3
</dt> <dt>



Removable media has been added to the device. The **dbch\_data** member is a pointer to a [**CLASS\_MEDIA\_CHANGE\_CONTEXT**](/windows/desktop/api/WinIoCtl/ns-winioctl-class_media_change_context) structure. The **NewState** member provides status information. For example, a value of **MediaUnavailable** indicates that the media is not available (for example, due to an active recording session).

**Windows XP:** The **dbch\_data** member is a **ULONG** value that represents the number of times that media has been changed since system startup.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_MEDIA_EJECT_REQUEST"></span><span id="guid_io_media_eject_request"></span>**GUID\_IO\_MEDIA\_EJECT\_REQUEST**
</dt> <dd> <dl> <dt>

d07433d1-a98e-11d2-917a-00a0c9068ff3
</dt> <dt>



The removable media's drive has received a request from the user to eject the specified slot or media.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_MEDIA_REMOVAL"></span><span id="guid_io_media_removal"></span>**GUID\_IO\_MEDIA\_REMOVAL**
</dt> <dd> <dl> <dt>

d07433c1-a98e-11d2-917a-00a0c9068ff3
</dt> <dt>



Removable media has been removed from the device or is unavailable. The **dbch\_data** member is a pointer to a [**CLASS\_MEDIA\_CHANGE\_CONTEXT**](/windows/desktop/api/WinIoCtl/ns-winioctl-class_media_change_context) structure. The **NewState** member provides status information. For example, a value of **MediaUnavailable** indicates that the media is not available (for example, due to an active recording session).

**Windows XP:** The **dbch\_data** member is a **ULONG** value that represents the number of times that media has been changed since system startup.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_CHANGE"></span><span id="guid_io_volume_change"></span>**GUID\_IO\_VOLUME\_CHANGE**
</dt> <dd> <dl> <dt>

7373654a-812a-11d0-bec7-08002be2092f
</dt> <dt>



The volume label has changed.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_CHANGE_SIZE"></span><span id="guid_io_volume_change_size"></span>**GUID\_IO\_VOLUME\_CHANGE\_SIZE**
</dt> <dd> <dl> <dt>

3a1625be-ad03-49f1-8ef8-6bbac182d1fd
</dt> <dt>



The size of the file system on the volume has changed.

**Windows Server 2003 and Windows XP:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_DISMOUNT"></span><span id="guid_io_volume_dismount"></span>**GUID\_IO\_VOLUME\_DISMOUNT**
</dt> <dd> <dl> <dt>

d16a55e8-1059-11d2-8ffd-00a0c9a06d32
</dt> <dt>



An attempt to dismount the volume is in progress. You should close all handles to files and directories on the volume. This event will not necessarily be preceded by a **GUID\_IO\_VOLUME\_LOCK** event.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_DISMOUNT_FAILED"></span><span id="guid_io_volume_dismount_failed"></span>**GUID\_IO\_VOLUME\_DISMOUNT\_FAILED**
</dt> <dd> <dl> <dt>

e3c5b178-105d-11d2-8ffd-00a0c9a06d32
</dt> <dt>



An attempt to dismount a volume failed. This often happens because another process failed to respond to a **GUID\_IO\_VOLUME\_DISMOUNT** notice by closing its outstanding handles. Because the dismount failed, you may reopen any handles to the affected volume.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_FVE_STATUS_CHANGE"></span><span id="guid_io_volume_fve_status_change"></span>**GUID\_IO\_VOLUME\_FVE\_STATUS\_CHANGE**
</dt> <dd> <dl> <dt>

062998b2-ee1f-4b6a-b857-e76cbbe9a6da
</dt> <dt>



The volume's BitLocker Drive Encryption status has changed. This event is signaled when BitLocker is enabled or disabled, or when encryption begins, ends, pauses, or resumes.

**Windows Server 2003 and Windows XP:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_LOCK"></span><span id="guid_io_volume_lock"></span>**GUID\_IO\_VOLUME\_LOCK**
</dt> <dd> <dl> <dt>

50708874-c9af-11d1-8fef-00a0c9a06d32
</dt> <dt>



Another process is attempting to lock the volume. You should close all handles to files and directories on the volume.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_LOCK_FAILED"></span><span id="guid_io_volume_lock_failed"></span>**GUID\_IO\_VOLUME\_LOCK\_FAILED**
</dt> <dd> <dl> <dt>

ae2eed10-0ba8-11d2-8ffb-00a0c9a06d32
</dt> <dt>



An attempt to lock a volume failed. This often happens because another process failed to respond to a **GUID\_IO\_VOLUME\_LOCK** event by closing its outstanding handles. Because the lock failed, you may reopen any handles to the affected volume.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_MOUNT"></span><span id="guid_io_volume_mount"></span>**GUID\_IO\_VOLUME\_MOUNT**
</dt> <dd> <dl> <dt>

b5804878-1a96-11d2-8ffd-00a0c9a06d32
</dt> <dt>



The volume has been mounted by another process. You may open one or more handles to it.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_NAME_CHANGE"></span><span id="guid_io_volume_name_change"></span>**GUID\_IO\_VOLUME\_NAME\_CHANGE**
</dt> <dd> <dl> <dt>

2de97f83-4c06-11d2-a532-00609713055a
</dt> <dt>



The volume name has been changed.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_NEED_CHKDSK"></span><span id="guid_io_volume_need_chkdsk"></span>**GUID\_IO\_VOLUME\_NEED\_CHKDSK**
</dt> <dd> <dl> <dt>

799a0960-0a0b-4e03-ad88-2fa7c6ce748a
</dt> <dt>



A file system has detected corruption on the volume. The application should run CHKDSK on the volume or notify the user to do so.

**Windows Server 2003 and Windows XP:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_PHYSICAL_CONFIGURATION_CHANGE"></span><span id="guid_io_volume_physical_configuration_change"></span>**GUID\_IO\_VOLUME\_PHYSICAL\_CONFIGURATION\_CHANGE**
</dt> <dd> <dl> <dt>

2de97f84-4c06-11d2-a532-00609713055a
</dt> <dt>



The physical makeup or current physical state of the volume has changed.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_PREPARING_EJECT"></span><span id="guid_io_volume_preparing_eject"></span>**GUID\_IO\_VOLUME\_PREPARING\_EJECT**
</dt> <dd> <dl> <dt>

c79eb16e-0dac-4e7a-a86c-b25ceeaa88f6
</dt> <dt>



The file system is preparing the disc to be ejected. For example, the file system is stopping a background formatting operation or closing the session on write-once media.

**Windows Server 2003 and Windows XP:** This value is not supported.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_UNIQUE_ID_CHANGE"></span><span id="guid_io_volume_unique_id_change"></span>**GUID\_IO\_VOLUME\_UNIQUE\_ID\_CHANGE**
</dt> <dd> <dl> <dt>

af39da42-6622-41f5-970b-139d092fa3d9
</dt> <dt>



The volume's unique identifier has been changed. For more information about the unique identifier, see [**IOCTL\_MOUNTDEV\_QUERY\_UNIQUE\_ID**](/windows-hardware/drivers/ddi/content/mountdev/ni-mountdev-ioctl_mountdev_query_unique_id).

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This value is not supported until Windows Server 2008 R2 and Windows 7.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_UNLOCK"></span><span id="guid_io_volume_unlock"></span>**GUID\_IO\_VOLUME\_UNLOCK**
</dt> <dd> <dl> <dt>

9a8c3d68-d0cb-11d1-8fef-00a0c9a06d32
</dt> <dt>



The volume has been unlocked by another process. You may open one or more handles to it.


</dt> </dl> </dd> <dt>

<span id="GUID_IO_VOLUME_WEARING_OUT"></span><span id="guid_io_volume_wearing_out"></span>**GUID\_IO\_VOLUME\_WEARING\_OUT**
</dt> <dd> <dl> <dt>

873113ca-1486-4508-82ac-c3b2e5297aaa
</dt> <dt>



The media is wearing out. This event is sent when a file system determines that the error rate on a volume is too high, or its defect replacement space is almost exhausted.

**Windows Server 2003 and Windows XP:** This value is not supported.


</dt> </dl> </dd> </dl>

## Remarks

The **GUID\_IO\_VOLUME\_DISMOUNT** and **GUID\_IO\_VOLUME\_DISMOUNT\_FAILED** events are related, as are the **GUID\_IO\_VOLUME\_LOCK** and **GUID\_IO\_VOLUME\_LOCK\_FAILED** event. The **GUID\_IO\_VOLUME\_DISMOUNT** and **GUID\_IO\_VOLUME\_LOCK** events indicate that an operation is being attempted. You should act on the event notification, and record the action taken. The **GUID\_IO\_VOLUME\_DISMOUNT\_FAILED** and **GUID\_IO\_VOLUME\_LOCK\_FAILED** events indicate that the attempted operation failed. You may then use your record to undo the actions you made in response to the operation.

The **dbch\_hdevnotify** member of the [**DEV\_BROADCAST\_HANDLE**](/windows/desktop/api/Dbt/ns-dbt-dev_broadcast_handle) structure indicates the affected device. Note that this is the device notification handle returned by [**RegisterDeviceNotification**](/windows/desktop/api/Winuser/nf-winuser-registerdevicenotificationa), not a volume handle. To perform operations on the volume, map this handle to the corresponding volume handle.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>IoEvent.h</dt> </dl> |



 

