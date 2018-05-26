---
title: DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS structure
description: The DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS structure specifies the parameters for an offload read action related to the data-set attributes for a device.
ms.assetid: 4C0B2CFD-B981-4304-B3F9-AD534BF5A823
keywords:
- DEVICE_DSM_OFFLOAD_READ_PARAMETERS structure Storage Devices
- PDEVICE_DSM_OFFLOAD_READ_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_DSM_OFFLOAD_READ_PARAMETERS
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

# DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS structure

The **DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS** structure specifies the parameters for an offload read action related to the data-set attributes for a device.

This parameter structure is used in an offload read action for an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request. The **Action** member of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure is set to **DeviceDsmAction\_OffloadRead**, and **ParameterBlockOffset** indicates the location of **DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**.

## Syntax


```C++
typedef struct _DEVICE_DSM_OFFLOAD_READ_PARAMETERS {
  ULONG Flags;
  ULONG TimeToLive;
  ULONG Reserved[2];
} DEVICE_DSM_OFFLOAD_READ_PARAMETERS, *PDEVICE_DSM_OFFLOAD_READ_PARAMETERS;
```



## Members

<dl> <dt>

**Flags**
</dt> <dd>

Not used. Set to 0.

</dd> <dt>

**TimeToLive**
</dt> <dd>

The duration, in milliseconds, for which the requested data ranges should remain valid.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

The **ParameterBlockOffset** and **ParameterBlockLength** members of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) are set to the location and length of the **DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS** structure in the system buffer of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

The **DataSetRangesOffset** and **DataSetRangesLength** members of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) specify the [**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md) structures for the extents of the offload read.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 8 and later versions of Windows.<br/>                                           |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md)
</dt> <dt>

[**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](device-dsm-offload-write-parameters.md)
</dt> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_DSM_OFFLOAD_READ_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






