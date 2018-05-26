---
title: DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES structure
description: The DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES structure specifies a management action for the data-set attributes for a device.
ms.assetid: be0bfcef-09df-4259-a034-0d51db9819ce
keywords:
- DEVICE_MANAGE_DATA_SET_ATTRIBUTES structure Storage Devices
- PDEVICE_MANAGE_DATA_SET_ATTRIBUTES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DEVICE_MANAGE_DATA_SET_ATTRIBUTES
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

# DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES structure

The **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES** structure specifies a management action for the data-set attributes for a device.

The management action is specified in the **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES** structure that is contained in the system buffer of an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

## Syntax


```C++
typedef struct _DEVICE_MANAGE_DATA_SET_ATTRIBUTES {
  ULONG                             Size;
  DEVICE_DATA_MANAGEMENT_SET_ACTION Action;
  ULONG                             Flags;
  ULONG                             ParameterBlockOffset;
  ULONG                             ParameterBlockLength;
  ULONG                             DataSetRangesOffset;
  ULONG                             DataSetRangesLength;
} DEVICE_MANAGE_DATA_SET_ATTRIBUTES, *PDEVICE_MANAGE_DATA_SET_ATTRIBUTES;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Contains the size of the structure **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**. The value of this member will change as members are added to the structure.

</dd> <dt>

**Action**
</dt> <dd>

The action to be performed as specified by a [**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520) enumeration value.

Starting with Windows 7, this value can be a bitwise OR of one or more of the following flags:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="DeviceDsmActionFlag_NonDestructive"></span><span id="devicedsmactionflag_nondestructive"></span><span id="DEVICEDSMACTIONFLAG_NONDESTRUCTIVE"></span><dl> <dt><strong><strong>DeviceDsmActionFlag_NonDestructive</strong></strong></dt> </dl></td>
<td>The specified action is non-destructive. If this flag is set, the driver can safely forward the [<strong>IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</strong>](ioctl-storage-manage-data-set-attributes.md) request to the next lower driver in the stack even if the driver does not handle the specified action.<br/>
<blockquote>
[!Note]<br />
Before it forwards the [<strong>IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</strong>](ioctl-storage-manage-data-set-attributes.md) request, the driver should still perform the normal processing of the data set ranges block that is specified by the <strong>DataSetRangesOffset</strong> and <strong>DataSetRangesLength</strong> members.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

**Flags**
</dt> <dd>

These flags are global to all control actions. The following flags can be set in the **Flags** member:



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DEVICE_DSM_FLAG_ENTIRE_DATA_SET_RANGE"></span><span id="device_dsm_flag_entire_data_set_range"></span><dl> <dt>****DEVICE\_DSM\_FLAG\_ENTIRE\_DATA\_SET\_RANGE****</dt> </dl> | Specifies that the control action is specified for the entire block of data set ranges. If this flag is set, the **DataSetRangesOffset** and **DataSetRangesLength** members must be set to zero.<br/> |



 

</dd> <dt>

**ParameterBlockOffset**
</dt> <dd>

Specifies the start of the parameter block within the system buffer of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request. The format of the parameter block depends on the value of the **Action** member. For more information, see [**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520).

> [!Note]  
> The offset of the parameter block must be aligned on the address boundary of the corresponding parameter structure.

 

If set to zero, then the parameter block does not exist.

</dd> <dt>

**ParameterBlockLength**
</dt> <dd>

Specifies the length, in bytes, of the parameter block within the payload of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

If set to zero, then the parameter block does not exist.

</dd> <dt>

**DataSetRangesOffset**
</dt> <dd>

Specifies the start of the block of data set ranges within the system buffer of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request. This block consists of one or more contiguous entries that are formatted as [**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md) structures.

> [!Note]  
> The offset of the data set range block must be aligned on the address boundary of the [**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md) structure.

 

If set to zero, then the block of data set ranges does not exist.

</dd> <dt>

**DataSetRangesLength**
</dt> <dd>

Specifies the length, in bytes, of the block of data set ranges within the payload of the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) request.

If set to zero, then the block of data set ranges does not exist.

</dd> </dl>

## Remarks

The block of data set ranges is specified by the **DataSetRangesOffset** and **DataSetRangesLength** members. If this block exists, it contains contiguous [**DEVICE\_DATA\_SET\_RANGE**](device-data-set-range.md) structures. The total size of the buffer should be at least:

`sizeof(DEVICE_MANAGE_DATA_SET_ATTRIBUTES) + ParameterBlockLength + DataSetRangesLength`

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_MANAGE_DATA_SET_ATTRIBUTES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






