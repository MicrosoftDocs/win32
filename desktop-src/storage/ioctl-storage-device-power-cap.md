---
title: IOCTL\_STORAGE\_DEVICE\_POWER\_CAP control code
description: A driver can use IOCTL\_STORAGE\_DEVICE\_POWER\_CAP to specify a maximum operational power consumption level for a storage device.
ms.assetid: 88DEC1F2-F0E7-4E95-9A46-D9E8EF72B1BB
keywords:
- IOCTL_STORAGE_DEVICE_POWER_CAP control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_DEVICE_POWER_CAP
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_DEVICE\_POWER\_CAP control code

A driver can use **IOCTL\_STORAGE\_DEVICE\_POWER\_CAP** to specify a maximum operational power consumption level for a storage device. The OS will do it's best to transition the device to a power state that will not exceed the given maximum. However, this depends on what the device supports. The actual maximum may be less than or greater than the desired maximum.

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md)).

**Irp-&gt;AssociatedIrp.SystemBuffer** contains [**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md) data that specifies the maximum power.

**Parameters.DeviceIoControl.OutputBufferLength** indicates the number of bytes that can be written to **Irp-&gt;AssociatedIrp.SystemBuffer**. **OutputBufferLength** must be **sizeof**([**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md)).

## Input Buffer Length

The length of .

## Output Buffer

If the operation is successful, the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** will contain a [**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md) structure.

## Output Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md)).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_INVALID\_PARAMETER, or STATUS\_NOT\_SUPPORTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_DEVICE\_POWER\_CAP**](storage-device-power-cap.md)
</dt> <dt>

[**STORAGE\_DEVICE\_POWER\_CAP\_UNITS**](storage-device-power-cap-units.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_DEVICE_POWER_CAP%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






