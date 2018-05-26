---
title: DEVICE\_LB\_PROVISIONING\_DESCRIPTOR structure
description: The DEVICE\_LB\_PROVISIONING\_DESCRIPTOR structure is one of the query result structures returned from an IOCTL\_STORAGE\_QUERY\_PROPERTY request. This structure contains the thin provisioning capabilities for a storage device.
ms.assetid: E7287A50-2BB8-4D11-AB9B-6E65EEDD698D
keywords:
- DEVICE_LB_PROVISIONING_DESCRIPTOR structure Storage Devices
- PDEVICE_LB_PROVISIONING_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_LB_PROVISIONING_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DEVICE\_LB\_PROVISIONING\_DESCRIPTOR structure

The **DEVICE\_LB\_PROVISIONING\_DESCRIPTOR** structure is one of the query result structures returned from an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request. This structure contains the thin provisioning capabilities for a storage device.

## Syntax


```C++
typedef struct _DEVICE_LB_PROVISIONING_DESCRIPTOR {
  ULONG     Version;
  ULONG     Size;
  UCHAR     ThinProvisioningEnabled  :1;
  UCHAR     ThinProvisioningReadZeros  :1;
  UCHAR     AnchorSupported  :3;
  UCHAR     UnmapGranularityAlignmentValid  :1;
  UCHAR     Reserverd0  :2;
  UCHAR     Reserverd1[7];
  ULONGLONG OptimalUnmapGranularity;
  ULONGLONG UnmapGranularityAlignment;
  ULONG     MaxUnmapLbaCount;
  ULONG     MaxUnmapBlockDescriptorCount;
} DEVICE_LB_PROVISIONING_DESCRIPTOR, *PDEVICE_LB_PROVISIONING_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. This is set to **sizeof**(DEVICE\_LB\_PROVISIONING\_DESCRIPTOR).

</dd> <dt>

**ThinProvisioningEnabled**
</dt> <dd>

The thin provisioning enabled status.



| Value                                                                        | Meaning                                   |
|------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>0</dt> </dl> | Thin provisioning is disabled.<br/> |
| <dl> <dt>1</dt> </dl> | Thin provisioning is enabled.<br/>  |



 

</dd> <dt>

**ThinProvisioningReadZeros**
</dt> <dd>

Reads to unmapped regions return zeros.



| Value                                                                        | Meaning                                                  |
|------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Data read from unmapped regions is undefined.<br/> |
| <dl> <dt>1</dt> </dl> | Reads return zeros.<br/>                           |



 

</dd> <dt>

**AnchorSupported**
</dt> <dd>

Support for the anchored LBA mapping state.



| Value                                                                        | Meaning                                                     |
|------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The anchored LBA mapping state is not supported.<br/> |
| <dl> <dt>1</dt> </dl> | The anchored LBA mapping state is supported.<br/>     |



 

</dd> <dt>

**UnmapGranularityAlignmentValid**
</dt> <dd>

The validity of unmap granularity alignment for the device.



| Value                                                                        | Meaning                                              |
|------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Unmap granularity alignment is not valid.<br/> |
| <dl> <dt>1</dt> </dl> | Unmap granularity alignment is valid.<br/>     |



 

</dd> <dt>

**Reserverd0**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserverd1**
</dt> <dd>

Reserved.

</dd> <dt>

**OptimalUnmapGranularity**
</dt> <dd>

The optimal number of blocks for unmap granularity for the device.

</dd> <dt>

**UnmapGranularityAlignment**
</dt> <dd>

The current value, in blocks, set for unmap granularity alignment on the device. The value **UnmapGranularityAlignmentValid** indicates the validity of this member.

</dd> <dt>

**MaxUnmapLbaCount**
</dt> <dd>

Maximum amount of LBAs that can be unmapped in a single UNMAP command, in units of logical blocks. This is valid only in Windows 10 and above.

</dd> <dt>

**MaxUnmapBlockDescriptorCount**
</dt> <dd>

Maximum number of descriptors allowed in a single UNMAP command. This is valid only in Windows 10 and above.

</dd> </dl>

## Remarks

This structure is returned in the system buffer from a [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request when the **PropertyId** member of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) is set to **StorageDeviceLBProvisioningProperty**.

The **DEVICE\_LB\_PROVISIONING\_DESCRIPTOR** structure is written to the system buffer, *Irp-&gt;AssociatedIrp.SystemBuffer*, with a value of **sizeof**(DEVICE\_LB\_PROVISIONING\_DESCRIPTOR) set in *Parameters.DeviceIoControl.OutputBufferLength* for the current IRP stack location.

If **UnmapGranularityAlignmentValid** = 0, then any code using **UnmapGranularityAlignment** should assume it has a value of 0.

If the underlying storage device is a SCSI device, unmapping capability can be queried. If the **TrimEnabled** member of the [**DEVICE\_TRIM\_DESCRIPTOR**](device-trim-descriptor.md) structure is TRUE, UNMAP is supported. The **DEVICE\_TRIM\_DESCRIPTOR** structure is returned in the system buffer from a [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request when the **PropertyId** member of [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) is set to **StorageDeviceTrimProperty**.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_LB_PROVISIONING_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






