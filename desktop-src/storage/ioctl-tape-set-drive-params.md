---
title: IOCTL\_TAPE\_SET\_DRIVE\_PARAMS control code
description: Adjusts a tape drive's configurable parameters.
ms.assetid: 'aa625cbf-fa0f-420a-b8ec-2babf4c4ec17'
keywords: ["IOCTL_TAPE_SET_DRIVE_PARAMS control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_TAPE_SET_DRIVE_PARAMS
api_location:
- Ntddtape.h
api_type:
- HeaderDef
---

# IOCTL\_TAPE\_SET\_DRIVE\_PARAMS control code

Adjusts a tape drive's configurable parameters. The miniclass driver can ignore parameters that its device does not support. The calling application is responsible for determining whether a device supports a particular feature before attempting to set it.

## Input Buffer

The [**TAPE\_SET\_DRIVE\_PARAMETERS**](tape-set-drive-parameters.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the values to be set.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(TAPE\_SET\_DRIVE\_PARAMETERS).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_IO\_DEVICE\_ERROR, STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_DEVICE\_DATA\_ERROR, STATUS\_NO\_SUCH\_DEVICE, STATUS\_IO\_TIMEOUT, STATUS\_INFO\_LENGTH\_MISMATCH, or STATUS\_DEVICE\_NOT\_READY.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_SET\_DRIVE\_PARAMETERS**](tape-set-drive-parameters.md)
</dt> <dt>

[**TapeMiniSetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567952)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_SET_DRIVE_PARAMS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






