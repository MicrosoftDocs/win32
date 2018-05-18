---
title: IOCTL\_DVD\_GET\_REGION control code
description: Returns Region Playback Control (RPC) information for a DVD device, such as whether the player supports the RPC2 standard, the current region code of the player, and the remaining number of times the player's region code can be changed by the user.
ms.assetid: '2c3d6962-1d72-47e7-aa7c-226e5a3aa3d4'
keywords: ["IOCTL_DVD_GET_REGION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_DVD_GET_REGION
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
---

# IOCTL\_DVD\_GET\_REGION control code

Returns Region Playback Control (RPC) information for a DVD device, such as whether the player supports the RPC2 standard, the current region code of the player, and the remaining number of times the player's region code can be changed by the user. This IOCTL also indicates the region code of the currently mounted disc. This only works if a DVD is in the drive. The [**IOCTL\_DVD\_READ\_KEY**](ioctl-dvd-read-key.md) operation should be used to obtain only the device region code. If the drive region has not been set previously (if it is still at factory default) and if the inserted media has a region, the device region will be set to the current media region.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**DVD\_REGION**](dvd-region.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

None. **Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof(**DVD\_REGION**)**.

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS or possibly STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_REGION**](dvd-region.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_DVD_GET_REGION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






