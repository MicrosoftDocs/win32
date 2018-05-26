---
title: SMART\_RCV\_DRIVE\_DATA control code
description: Returns version information, a capabilities mask, and a bitmask for the device. This IOCTL must be handled by drivers that support Self-Monitoring Analysis and Reporting Technology (SMART).
ms.assetid: dd9087d0-4fbd-4446-a35d-92629192defb
keywords:
- SMART_RCV_DRIVE_DATA control code Storage Devices
topic_type:
- apiref
api_name:
- SMART_RCV_DRIVE_DATA
api_location:
- Ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMART\_RCV\_DRIVE\_DATA control code

Returns version information, a capabilities mask, and a bitmask for the device. This IOCTL must be handled by drivers that support Self-Monitoring Analysis and Reporting Technology (SMART).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**SENDCMDINPARAMS**](sendcmdinparams.md) structure that describes the request being sent to the device. The **irDriveRegs.bCommandReg** member specifies ID\_CMD when identify data is requested and SMART\_CMD when SMART data is requested. For a list of values that can be assigned to the features register (**irDriveRegs.bFeaturesReg**), see [**IDEREGS**](ideregs.md).

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** specifies the size, in bytes, of the input buffer, which must be &gt;= (**sizeof**(SENDCMDINPARAMS) - 1).

## Output Buffer

The driver returns the [**SENDCMDOUTPARAMS**](sendcmdoutparams.md) structure and a 512-byte buffer of drive data to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

If the caller specifies a SMART subcommand of SMART\_READ\_LOG in **rDriveRegs.bFeaturesReg**, the caller must also indicate the number of sectors to read in **irDriveRegs.bSectorCountReg**. The output buffer size must be &gt;= the maximum of two values:

1.  **sizeof**(SENDCMDOUTPARAMS) or

2.  **sizeof**(SENDCMDINPARAMS)) -1 + (**irDriveRegs.bSectorCountReg** \* SMART\_LOG\_SECTOR\_SIZE).

The data read from the log will be placed in the buffer specified by the **bBuffer** member of SENDCMDOUTPARAMS.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** specifies the size, in bytes, of the output buffer, which must be &gt;= (**sizeof**(SENDCMDOUTPARAMS) - 1 + 512).

## Status block

The driver sets the **Information** field to (**sizeof**(SENDCMDOUTPARAMS) - 1 + 512) when it sets the **Status** field to STATUS\_SUCCESS. Otherwise, the driver sets the **Information** field to zero and the **Status** field to possibly STATUS\_INVALID\_PARAMETER or STATUS\_INSUFFICIENT\_RESOURCES.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SMART_RCV_DRIVE_DATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






