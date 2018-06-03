---
title: DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT structure
description: The DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT structure describes output for IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES control code requests for some data set management actions.
ms.assetid: FFC52136-8A1C-48F6-A846-C1C5BFB4570C
keywords:
- DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure Storage Devices
- PDEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT
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

# DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT structure

The **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT** structure describes output for [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) control code requests for some data set management actions.

## Syntax


```C++
typedef struct _DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT {
  ULONG                             Size;
  DEVICE_DATA_MANAGEMENT_SET_ACTION Action;
  ULONG                             Flags;
  ULONG                             OperationStatus;
  ULONG                             ExtendedError;
  ULONG                             TargetDetailedError;
  ULONG                             ReservedStatus;
  ULONG                             OutputBlockOffset;
  ULONG                             OutputBlockLength;
} DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT, *PDEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of this structure. This is set to **sizeof**(DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT).

</dd> <dt>

**Action**
</dt> <dd>

The action related to the instance of this structure. This is a value from the [**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](device-manage-data-set-attributes.md) enumeration.

</dd> <dt>

**Flags**
</dt> <dd>

Flags for the data set management action. See the **Flags** member of [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md).

</dd> <dt>

**OperationStatus**
</dt> <dd>

An status resulting from the operation a performed for **Action**.

</dd> <dt>

**ExtendedError**
</dt> <dd>

An extended error value originating from Windows or a driver.

</dd> <dt>

**TargetDetailedError**
</dt> <dd>

An error value resulting from a failure execute the operation for **Action** at the target.

</dd> <dt>

**ReservedStatus**
</dt> <dd>

Reserved.

</dd> <dt>

**OutputBlockOffset**
</dt> <dd>

The position, after the beginning of this structure, where action-specific data is located.

</dd> <dt>

**OutputBlockLength**
</dt> <dd>

The length of the action-specific data.

</dd> </dl>

## Remarks

Depending on the value of **Action**, an output block is written at an offset of **OutputBlockOffset** after the beginning of this structure. The size of the output block is specified in **OutputBlockLength**.

Currently, only the **DeviceDsmAction\_Allocation** action uses this structure.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](device-manage-data-set-attributes.md)
</dt> <dt>

[**DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE**](device-data-set-lb-provisioning-state.md)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUTPUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






