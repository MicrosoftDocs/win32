---
title: ChangerMoveMedium function
description: ChangerMoveMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_MOVE\_MEDIUM.
ms.assetid: 7532c8b5-e77b-4fd0-bac2-78254f6eb9f6
keywords:
- ChangerMoveMedium function Storage Devices
topic_type:
- apiref
api_name:
- ChangerMoveMedium
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

# ChangerMoveMedium function

**ChangerMoveMedium** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md).

## Syntax


```C++
NTSTATUS ChangerMoveMedium(
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

**ChangerMoveMedium** returns the status returned by the system port driver, or one of the following values:

STATUS\_SUCCESS

STATUS\_DESTINATION\_ELEMENT\_FULL

STATUS\_INVALID\_ELEMENT\_ADDRESS

STATUS\_INVALID\_DEVICE\_REQUEST

STATUS\_INVALID\_PARAMETER

STATUS\_INSUFFICIENT\_RESOURCES

STATUS\_SOURCE\_ELEMENT\_EMPTY

## Remarks

This routine is required.

**ChangerMoveMedium** moves a piece of media from one element to another.

The changer class driver checks the input buffer length in the I/O stack location before calling **ChangerMoveMedium**. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_MOVE\_MEDIUM**](changer-move-medium.md) structure that indicates the transport element, the source, the destination, and whether to flip the medium.

**ChangerMoveMedium** first verifies that the transport, source, and destination element addresses are valid and then converts zero-based element addresses to device-specific addresses. It then builds an SRB with a CDB to move the piece of media and sends it to the system port driver.

**ChangerMoveMedium** sets the **Information** field in the I/O status block to **sizeof**(CHANGER\_MOVE\_MEDIUM) before returning to the changer class driver.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**ChangerExchangeMedium**](changerexchangemedium.md)
</dt> <dt>

[**CHANGER\_MOVE\_MEDIUM**](changer-move-medium.md)
</dt> <dt>

[**,**](ioctl-changer-move-medium.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerMoveMedium%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






