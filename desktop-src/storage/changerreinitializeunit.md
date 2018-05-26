---
title: ChangerReinitializeUnit function
description: ChangerReinitializeUnit handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT.
ms.assetid: 161156e3-0da0-458d-b623-67665b2a56c0
keywords:
- ChangerReinitializeUnit function Storage Devices
topic_type:
- apiref
api_name:
- ChangerReinitializeUnit
api_location:
- mcd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ChangerReinitializeUnit function

**ChangerReinitializeUnit** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](ioctl-changer-reinitialize-transport.md).

## Syntax


```C++
NTSTATUS ChangerReinitializeUnit(
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

If the changer supports recalibrating a transport element, **ChangerReinitializeUnit** returns the STATUS\_*XXX* value returned by the system port driver, or one of the following values:

STATUS\_SUCCESS

STATUS\_INVALID\_ELEMENT\_ADDRESS

STATUS\_INVALID\_PARAMETER

STATUS\_INSUFFICIENT\_RESOURCES

If the changer does not support recalibrating a transport element, ChangerReinitializeUnit returns STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

This routine is required.

**ChangerReinitializeUnit** causes the changer to recalibrate its transport element. Depending on the changer, this may return the transport to a "home" position. The changer class driver typically calls **ChangerReinitializeUnit** after the changer has been powered on or a calling application has initiated a recovery operation. The CHANGER\_DEVICE\_REINITIALIZE\_CAPABLE flag in **Features0** of [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) indicates whether the changer's transport supports recalibration in those circumstances.

The changer class driver checks the input buffer length in the I/O stack location before calling **ChangerReinitializeUnit**. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_ELEMENT**](changer-element.md) structure that indicates the element to recalibrate.

**ChangerReinitializeUnit** builds an SRB with a CDB to position the transport element and sends it to the system port driver.

**ChangerReinitializeUnit** sets the **Information** field in the I/O status block to **sizeof**(CHANGER\_ELEMENT) before returning to the changer class driver.

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

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**, IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](ioctl-changer-reinitialize-transport.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerReinitializeUnit%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






