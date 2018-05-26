---
title: IOCTL\_CDROM\_SEND\_OPC\_INFORMATION control code
description: The IOCTL\_CDROM\_SEND\_OPC\_INFORMATION control code can be used in file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish. The optical drive performs the OPC procedure to determine the optimum power of the laser during write. The procedure is necessary to ensure quality, but it wears out the media and should not be performed too often.
ms.assetid: 77289AB6-7733-4DA1-B4E9-585AA73D137C
keywords:
- IOCTL_CDROM_SEND_OPC_INFORMATION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_SEND_OPC_INFORMATION
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_CDROM\_SEND\_OPC\_INFORMATION control code

The **IOCTL\_CDROM\_SEND\_OPC\_INFORMATION** control code can be used in file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish. The optical drive performs the OPC procedure to determine the optimum power of the laser during write. The procedure is necessary to ensure quality, but it wears out the media and should not be performed too often.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with **IOCTL\_CDROM\_SEND\_OPC\_INFORMATION** as the *dwIoControlCode* parameter.

## Input Buffer

[**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md)

## Input Buffer Length

Length of a [**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to the number of bytes returned.

Because of status code propagation from other APIs, the **Status** field can be set to (but is not limited to) the following:

<dl> <dt>

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS
</dt> <dd>

The request completed successfully.

</dd> <dt>

<span id="STATUS_INFO_LENGTH_MISMATCH"></span><span id="status_info_length_mismatch"></span>STATUS\_INFO\_LENGTH\_MISMATCH
</dt> <dd>

The input buffer length is smaller than required.

</dd> <dt>

<span id="STATUS_INVALID_PARAMETER"></span><span id="status_invalid_parameter"></span>STATUS\_INVALID\_PARAMETER
</dt> <dd>

The request type is not **SimpleOpcInfo**.

</dd> </dl>

## Remarks

The **IOCTL\_CDROM\_SEND\_OPC\_INFORMATION** IOCTL is a wrapper over the SEND OPC INFORMATION command of the MMC specification. The **Exclude0** and **Exclude1** fields directly map to the SEND OPC INFORMATION fields with the same names. On failures, this IOCTL returns standard errors, such as STATUS\_DEVICE\_NOT\_READY, STATUS\_IO\_TIMEOUT, STATUS\_IO\_DEVICE\_ERROR.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Winioctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**CDROM\_SIMPLE\_OPC\_INFO**](cdrom-simple-opc-info.md)
</dt> <dt>

[**IOCTL\_CDROM\_SEND\_OPC\_INFORMATION**](ioctl-cdrom-send-opc-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_SEND_OPC_INFORMATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






