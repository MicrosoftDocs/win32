---
title: IOCTL\_MINIPORT\_PROCESS\_SERVICE\_IRP control code
description: This IOCTL is used by a user-mode application or kernel-mode driver that requires notification when something of interest happens in the virtual miniport.
ms.assetid: 5d9f695c-9a9f-4af9-8bf6-2096f3278852
keywords:
- IOCTL_MINIPORT_PROCESS_SERVICE_IRP control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_MINIPORT_PROCESS_SERVICE_IRP
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_MINIPORT\_PROCESS\_SERVICE\_IRP control code

This IOCTL is used by a user-mode application or kernel-mode driver that requires notification when something of interest happens in the virtual miniport. This IOCTL might be used, for example, when a vendor-specific, time-consuming operation such as device discovery completes.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a user-defined structure.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of all the input data.

## Output Buffer

Updated user-defined structures are returned in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The length of the buffer.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MINIPORT_PROCESS_SERVICE_IRP%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






