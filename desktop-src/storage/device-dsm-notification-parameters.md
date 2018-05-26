---
title: DEVICE\_DSM\_NOTIFICATION\_PARAMETERS structure
description: The DEVICE\_DSM\_NOTIFICATION\_PARAMETERS structure specifies the parameters for a notification action related to the data-set attributes for a device.
ms.assetid: 57885E58-C7EC-493E-9AB8-B9DABC6CEA2A
keywords:
- DEVICE_DSM_NOTIFICATION_PARAMETERS structure Storage Devices
- PDEVICE_DSM_NOTIFICATION_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_DSM_NOTIFICATION_PARAMETERS
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DEVICE\_DSM\_NOTIFICATION\_PARAMETERS structure

The **DEVICE\_DSM\_NOTIFICATION\_PARAMETERS** structure specifies the parameters for a notification action related to the data-set attributes for a device.

The notification action is specified in the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure that is contained in the system buffer of an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

## Syntax


```C++
typedef struct _DEVICE_DSM_NOTIFICATION_PARAMETERS {
  DWORD Size;
  DWORD Flags;
  DWORD NumFileTypeIDs;
  GUID  FileTypeIDs[1];
} DEVICE_DSM_NOTIFICATION_PARAMETERS, *PDEVICE_DSM_NOTIFICATION_PARAMETERS;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Specifies the total size, in bytes, of this structure. The value of this member must include the total size, in bytes, of the **FileTypeIDs** member.

</dd> <dt>

**Flags**
</dt> <dd>

A flag that specifies the characteristics of the notification operation. The **Flags** member must be set to one of the following values:

<dl> <dt>

<span id="DEVICE_DSM_NOTIFY_FLAG_BEGIN"></span><span id="device_dsm_notify_flag_begin"></span>**DEVICE\_DSM\_NOTIFY\_FLAG\_BEGIN**
</dt> <dd>

The Logical Block Address (LBA) range is currently being used by the file types that are specified in the **FileTypeIDs** member.

> [!Note]  
> The LBA range is specified by the data set range of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure.

 

</dd> <dt>

<span id="DEVICE_DSM_NOTIFY_FLAG_END"></span><span id="device_dsm_notify_flag_end"></span>**DEVICE\_DSM\_NOTIFY\_FLAG\_END**
</dt> <dd>

The LBA range is no longer being used by the file types that are specified in the **FileTypeIDs** member.

</dd> </dl> </dd> <dt>

**NumFileTypeIDs**
</dt> <dd>

The number of entries in the **FileTypeIDs** member.

</dd> <dt>

**FileTypeIDs**
</dt> <dd>

One or more [*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid) values that specify the file type for the notification operation. The following table describes the **FileTypeIDs** GUID values.



| GUID value                                        | Description                                                         |
|---------------------------------------------------|---------------------------------------------------------------------|
| FILE\_TYPE\_NOTIFICATION\_GUID\_PAGE\_FILE        | Specifies a notification operation for a page file.                 |
| FILE\_TYPE\_NOTIFICATION\_GUID\_HIBERNATION\_FILE | Specifies a notification operation for the system hibernation file. |
| FILE\_TYPE\_NOTIFICATION\_GUID\_CRASHDUMP\_FILE   | Specifies a notification operation for a system crash dump file.    |



 

</dd> </dl>

## Remarks

Starting with Windows 7, the NTFS file system notifies the storage stack when the LBA data set range changes for a specified set of files. The file system issues this notification by sending the storage stack an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request with a system buffer that contains a [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure. For the notification operation, the file system sets the members of the **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES** structure as follows:

-   The **Action** member is set to **DeviceDsmAction\_Notification**.

-   The **ParameterBlockOffset** and **ParameterBlockLength** members specify the location and size of the parameter block for the notification operation. The parameter block is formatted as a **DEVICE\_DSM\_NOTIFICATION\_PARAMETERS** structure.

-   If the **Flags** member is set to zero, the **DataSetRangesOffset** and **DataSetRangesLength** members specify the data set range block within the IOCTL payload.

    If the **Flags** member is set to **DEVICE\_DSM\_FLAG\_ENTIRE\_DATA\_SET\_RANGE**, the **DataSetRangesOffset** and **DataSetRangesLength** members are set to zero and the notification action includes the entire data set range for the specified files.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_DSM_NOTIFICATION_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






