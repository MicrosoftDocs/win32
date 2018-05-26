---
title: IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES control code
description: This IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES request is used to send a manage data set attributes request to a storage device.
ms.assetid: 678bbca6-f21f-480a-897d-a30e922d01e3
keywords:
- IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES control code

This **IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES** request is used to send a manage data set attributes request to a storage device.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains a [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure. Note that the buffer may include parameter and data set range blocks. Also, the **Action** member of this structure defines the action to be performed through a [**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520) enumeration value.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least **sizeof**([**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)).

## Output Buffer

Depending on the value set in the **Action** member of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md), the request may return data in the buffer at *Irp-&gt;AssociatedIrp.SystemBuffer*. The system buffer will contain valid data if the manage data set action operation returns output and *Parameters.DeviceIoControl.InputBufferLength* &gt; 0.

## Output Buffer Length

The length of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md).

## Status block

The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_BUFFER\_TOO\_SMALL, STATUS\_BUFFER\_OVERFLOW, or some other error status.

## Remarks

Due to memory pool requirements by the storage driver stack, completion of the IRP containing this IOCTL must be at IRQL &lt; DISPATCH\_LEVEL.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |
| IRQL<br/>   | IRQL &lt; DISPATCH\_LEVEL (See Remarks section.)<br/>                                                |



## See also

<dl> <dt>

[**DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552520)
</dt> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






