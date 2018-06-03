---
title: ChangerGetStatus function
description: ChangerGetStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_GET\_STATUS.
ms.assetid: f5719dfa-e48a-4f81-8344-31b349fadb48
keywords:
- ChangerGetStatus function Storage Devices
topic_type:
- apiref
api_name:
- ChangerGetStatus
api_location:
- mcd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerGetStatus function

**ChangerGetStatus** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_STATUS**](ioctl-changer-get-status.md).

## Syntax


```C++
NTSTATUS ChangerGetStatus(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object that represents the changer.

</dd> <dt>

*Irp* \[in\]
</dt> <dd>

Pointer to the IRP.

</dd> </dl>

## Return value

**ChangerGetStatus** returns the STATUS\_*XXX* value returned by the system port driver. If there is not enough memory to process the request or to process the STATUS\_*XXX* value returned by the system port driver **ChangerGetStatus** returns STATUS\_INSUFFICIENT\_RESOURCES.

## Remarks

This routine is required.

**ChangerGetStatus** indicates whether the changer is able to accept requests.

**ChangerGetStatus** builds an SRB with a CDB to get the changer's status (using the SCSI command TEST UNIT READY or non-SCSI equivalent) and sends it to the system port driver to obtain status of the changer.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_STATUS**](ioctl-changer-get-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerGetStatus%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






