---
title: NV\_FEATURE\_PARAMETER structure
description: The NV\_FEATURE\_PARAMETER structure is used in conjunction with the IOCTL\_SCSI\_MINIPORT\_NVCACHE request to get NV Cache Manager feature support information from the device.
ms.assetid: 06b07b50-577c-4762-aea6-38bd1ada8973
keywords:
- NV_FEATURE_PARAMETER structure Storage Devices
- PNV_FEATURE_PARAMETER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- NV_FEATURE_PARAMETER
api_location:
- ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# NV\_FEATURE\_PARAMETER structure

The NV\_FEATURE\_PARAMETER structure is used in conjunction with the [**IOCTL\_SCSI\_MINIPORT\_NVCACHE**](ioctl-scsi-miniport-nvcache.md) request to get NV Cache Manager feature support information from the device. The NV Cache Manager feature parameters structure is returned by the miniport driver upon the successful return from the NRB\_NVCACHE\_INFO function, as requested in the Function field of the [**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md) structure.

The values in these fields come from the IDENTIFY DEVICE command in section 7.16 of the [ATA8-ACS specification](http://go.microsoft.com/fwlink/p/?linkid=74996).

## Syntax


```C++
typedef struct _NV_FEATURE_PARAMETER {
  USHORT NVPowerModeEnabled;
  USHORT NVParameterReserv1;
  USHORT NVCmdEnabled;
  USHORT NVParameterReserv2;
  USHORT NVPowerModeVer;
  USHORT NVCmdVer;
  ULONG  NVSize;
  USHORT NVReadSpeed;
  USHORT NVWrtSpeed;
  ULONG  DeviceSpinUpTime;
} NV_FEATURE_PARAMETER, *PNV_FEATURE_PARAMETER;
```



## Members

<dl> <dt>

**NVPowerModeEnabled**
</dt> <dd>

Taken from word 214, bit 0 of the IDENTIFY DEVICE data, a value of one means the NV Cache Power Mode feature set is enabled.

</dd> <dt>

**NVParameterReserv1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**NVCmdEnabled**
</dt> <dd>

Taken from word 214, bit 4 of the IDENTIFY DEVICE data, a value of one means the NV Cache feature set is enabled.

</dd> <dt>

**NVParameterReserv2**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**NVPowerModeVer**
</dt> <dd>

Taken from word 214, bits 8 through 11 of the IDENTIFY DEVICE data, this field contains the NV Cache Power Mode feature set version.

</dd> <dt>

**NVCmdVer**
</dt> <dd>

Taken from word 214, bits 12 through 15 of the IDENTIFY DEVICE data, this field contains the NV Cache feature set version.

</dd> <dt>

**NVSize**
</dt> <dd>

Taken from words 215 and 216 of the IDENTIFY DEVICE data, this field contains the NV Cache Size, in logical blocks.

</dd> <dt>

**NVReadSpeed**
</dt> <dd>

Taken from word 217 of the IDENTIFY DEVICE data, this field contains the NV Cache Read Transfer Speed, in megabytes per second (MB/s).

</dd> <dt>

**NVWrtSpeed**
</dt> <dd>

Taken from word 218 of the IDENTIFY DEVICE data, this field contains the NV Cache Write Transfer Speed, in megabytes per second (MB/s).

</dd> <dt>

**DeviceSpinUpTime**
</dt> <dd>

Taken from word 219, bits 0 through 7 of the IDENTIFY DEVICE data, this field contains the device's estimated time to spin up, in seconds.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20NV_FEATURE_PARAMETER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






