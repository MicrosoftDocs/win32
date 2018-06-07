---
title: DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS structure
description: The DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS structure specifies the parameters of a storage spaces repair operation specified for a data set management action.
ms.assetid: BBA834D0-4D21-42EF-98B0-9AF3FF28E6E2
keywords:
- DEVICE_DATA_SET_REPAIR_PARAMETERS structure Storage Devices
- PDEVICE_DATA_SET_REPAIR_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_DATA_SET_REPAIR_PARAMETERS
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS structure

The **DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS** structure specifies the parameters of a storage spaces repair operation specified for a data set management action.

This parameter structure is used in a repair action for an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request. The **Action** member of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure is set to **DeviceDsmAction\_Repair**, and **ParameterBlockOffset** indicates the location of **DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS**.

## Syntax


```C++
typedef struct _DEVICE_DATA_SET_REPAIR_PARAMETERS {
  ULONG NumberOfRepairCopies;
  ULONG SourceCopy;
  ULONG RepairCopies[ANYSIZE_ARRAY];
} DEVICE_DATA_SET_REPAIR_PARAMETERS, *PDEVICE_DATA_SET_REPAIR_PARAMETERS;
```



## Members

<dl> <dt>

**NumberOfRepairCopies**
</dt> <dd>

The total number of copies to repair.

</dd> <dt>

**SourceCopy**
</dt> <dd>

The source copy number.

</dd> <dt>

**RepairCopies**
</dt> <dd>

An array of copy numbers for the copies to repair.

</dd> </dl>

## Remarks

The **ParameterBlockOffset** and **ParameterBlockLength** members of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) are set to the location and length of the **DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS** structure in the system buffer of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

The **DataSetRangesOffset** and **DataSetRangesLength** members of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) specify the [**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md) structures containing the extents of the repair copies.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520)
</dt> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_DATA_SET_REPAIR_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






