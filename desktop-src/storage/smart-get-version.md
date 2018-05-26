---
title: SMART\_GET\_VERSION control code
description: Returns version information, a capabilities mask, and a bitmask for the device. This IOCTL must be handled by drivers that support Self-Monitoring Analysis and Reporting Technology (SMART).
ms.assetid: 27c6ae5e-fd7d-47ed-8a54-43e9b26e86ca
keywords:
- SMART_GET_VERSION control code Storage Devices
topic_type:
- apiref
api_name:
- SMART_GET_VERSION
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

# SMART\_GET\_VERSION control code

Returns version information, a capabilities mask, and a bitmask for the device. This IOCTL must be handled by drivers that support Self-Monitoring Analysis and Reporting Technology (SMART).

## Input Buffer

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(GETVERSIONINPARAMS).

## Input Buffer Length

**sizeof**(GETVERSIONINPARAMS).

## Output Buffer

The driver returns the information to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Status block

The driver sets the **Information** field to **sizeof**(GETVERSIONINPARAMS) when it sets the **Status** field to STATUS\_SUCCESS. Otherwise, the driver sets the **Information** field to zero and sets the **Status** field to possibly STATUS\_INVALID\_PARAMETER.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Supported in Microsoft Windows 2000 and later operating systems.<br/>                                |
| Header<br/>  | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**GETVERSIONINPARAMS**](getversioninparams.md)
</dt> <dt>

[Creating IOCTL Requests in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542894)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548651)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548656)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SMART_GET_VERSION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






