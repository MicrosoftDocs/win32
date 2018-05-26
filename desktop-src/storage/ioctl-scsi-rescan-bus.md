---
title: IOCTL\_SCSI\_RESCAN\_BUS control code
description: Rescans the LUNs on the bus(es).
ms.assetid: d2b1ec10-3d59-469f-a92e-e28a6c2aef92
keywords:
- IOCTL_SCSI_RESCAN_BUS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_RESCAN_BUS
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_SCSI\_RESCAN\_BUS control code

Rescans the LUNs on the bus(es). It collects SCSI inquiry data about all devices on the bus(es), while preserving any claims on their respective devices for SCSI class drivers.

This request is obsolete and is supported for legacy code only. This request must be directed to an FDO and is valid only for legacy (non-PnP) class drivers and SCSI bus enumeration. If the bus can detect device insertion, this request is not relevant.

Usually, this request originates in a system-supplied Win32 application such as Windisk or Setup when the user connects new device(s) for which the system has no Plug and Play drivers on a SCSI bus dynamically, that is, without shutting down the system. When this request is satisfied, such an application next makes an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to the system port driver and examines the returned inquiry data. If the application finds any unclaimed devices of a given type, it then sends one or more [**IOCTL\_STORAGE\_FIND\_NEW\_DEVICES**](ioctl-storage-find-new-devices.md) requests to the appropriate storage class drivers.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_RESCAN_BUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






