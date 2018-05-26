---
title: SCSI Port I/O Control Codes
description: SCSI Port I/O Control Codes
ms.assetid: ec9a73f9-ff80-42c6-a88c-1a017e30cb8f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSI Port I/O Control Codes

## 

All storage class drivers are required to set the minor function code with IRP\_MJ\_DEVICE\_CONTROL in the port driver's I/O stack location of any IRP that a class driver allocates and sets up to send on to the system port driver. For example, a legacy class driver must set this minor function code when it makes an IOCTL\_SCSI\_GET\_ADDRESS request to obtain the address of a target device.

For incoming IRPs originating with a user I/O request or with a higher-level driver, storage class drivers should ignore the minor function code in the port driver's I/O stack location, leaving it as is. In general, such requests can be sent directly to the system-supplied port driver *only if no storage class driver for the target device exists*. Otherwise, such requests must be directed to the storage class driver for the appropriate type of underlying storage device.

This section contains I/O control requests that a storage port driver supports. All public I/O control codes for the port driver use buffered I/O. Consequently, most input or output data for these requests is at **Irp-&gt;AssociatedIrp.SystemBuffer**.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI%20Port%20I/O%20Control%20Codes%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




