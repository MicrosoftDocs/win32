---
title: SMART\_SEND\_DRIVE\_COMMAND control code
description: Sends one of the following Self-Monitoring Analysis and Reporting Technology (SMART) commands to the device Enable or disable reporting on the device Enable or disable autosaving of attributes Save current attributes now Execute offline diagnostics Get current SMART status Write to SMART log This IOCTL must be handled by drivers that support SMART.
ms.assetid: df616f55-8291-4ba7-bdb1-e5dd5be62c5c
keywords:
- SMART_SEND_DRIVE_COMMAND control code Storage Devices
topic_type:
- apiref
api_name:
- SMART_SEND_DRIVE_COMMAND
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SMART\_SEND\_DRIVE\_COMMAND control code

Sends one of the following Self-Monitoring Analysis and Reporting Technology (SMART) commands to the device:

-   Enable or disable reporting on the device

-   Enable or disable autosaving of attributes

-   Save current attributes now

-   Execute offline diagnostics

-   Get current SMART status

-   Write to SMART log

This IOCTL must be handled by drivers that support SMART.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**SENDCMDINPARAMS**](sendcmdinparams.md) structure that describes the command being sent to the device. The **irDriveRegs.bCommandReg** member must specify SMART\_CMD. The **irDriveRegs.bFeaturesReg** member must specify a SMART subcommand. For a list of subcommands, see [**IDEREGS**](ideregs.md).

## Input Buffer Length

If the caller specifies a SMART subcommand of SMART\_WRITE\_LOG in **irDriveRegs.bFeaturesReg**, caller must also indicate the number of sectors to write in **irDriveRegs.bSectorCountReg**. The input buffer size must be &gt;= **sizeof**(SENDCMDINPARAMS) - 1) + (**irDriveRegs.bSectorCountReg** \* SMART\_LOG\_SECTOR\_SIZE). Caller must put the data to write in the buffer indicated by the **bBuffer** member of SENDCMDINPARAMS.

**Parameters.DeviceIoControl.InputBufferLength** specifies the size in, bytes, of the input buffer, which must be &gt;= (**sizeof**(SENDCMDINPARAMS) - 1).

**Parameters.DeviceIoControl.OutputBufferLength** specifies the size, in bytes, of the output buffer, which must be &gt;= (**sizeof**(SENDCMDOUTPARAMS) - 1). If SMART status is being requested, the output buffer must be &gt;= (**sizeof**(SENDCMDOUTPARAMS) - 1 + **sizeof**(IDEREGS)).

## Output Buffer

The driver returns the [**SENDCMDOUTPARAMS**](sendcmdoutparams.md) structure to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. If SMART status was requested and successfully received from the device, the driver includes the IDEREGS structure in the output buffer.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** specifies the size, in bytes, of the output buffer, which must be &gt;= (**sizeof**(SENDCMDOUTPARAMS) - 1 + 512).

## Status block

When the driver sets the **Status** field to STATUS\_SUCCESS, it sets the **Information** field is set to ((**sizeof**(SENDCMDOUTPARAMS) - 1) + **sizeof**(IDEREGS)) for returning SMART status and to (**sizeof**(SENDCMDOUTPARAMS) - 1) for all other commands. The driver should set the **Status** field to STATUS\_INVALID\_PARAMETER if an input parameter is incorrect or to STATUS\_IO\_DEVICE\_ERROR if the device aborts a command it does not support. If **Status** is not STATUS\_SUCCESS, the driver sets the **Information** field to zero.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Supported in Microsoft Windows 2000 and later operating systems.<br/>                                |
| Header<br/>  | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SENDCMDINPARAMS**](sendcmdinparams.md)
</dt> <dt>

[**SENDCMDOUTPARAMS**](sendcmdoutparams.md)
</dt> <dt>

[Creating IOCTL Requests in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542894)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548651)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548656)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SMART_SEND_DRIVE_COMMAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






