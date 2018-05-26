---
title: ChangerExchangeMedium function
description: ChangerExchangeMedium handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_EXCHANGE\_MEDIUM.
ms.assetid: 4cb6e9af-ddd0-48d9-9f07-43c828e4187b
keywords:
- ChangerExchangeMedium function Storage Devices
topic_type:
- apiref
api_name:
- ChangerExchangeMedium
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

# ChangerExchangeMedium function

**ChangerExchangeMedium** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md).

## Syntax


```C++
NTSTATUS ChangerExchangeMedium(
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

If the changer supports exchanging media, **ChangerExchangeMedium** returns the status returned by the system port driver, or one of the following values:

STATUS\_SUCCESS

STATUS\_DESTINATION\_ELEMENT\_FULL

STATUS\_INVALID\_ELEMENT\_ADDRESS

STATUS\_SOURCE\_ELEMENT\_EMPTY

If the changer does not support exchanging media, ChangerExchangeMedium returns STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

This routine is required.

**ChangerExchangeMedium** moves a piece of media from a source element to one destination and from that destination to another destination. The source and second destination are often the same, resulting in a simple exchange of media.

The CHANGER\_EXCHANGE\_MEDIA flag in **Features0** of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure indicates whether the changer supports this functionality. A changer that supports exchanging media typically has two picker mechanisms on a single transport element, or at least two transport elements. A changer that has a single picker mechanism might support exchanging medium through emulation of the command.

The changer class driver checks the input buffer length in the I/O stack location before calling a miniclass driver's **ChangerExchangeMedium** routine. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_EXCHANGE\_MEDIUM**](changer-exchange-medium.md) structure as an input parameter that indicates the transport element and the destination to set.

**ChangerExchangeMedium** first verifies that the transport, source, and destination element addresses are valid, then converts zero-based element addresses to device-specific element addresses. It then builds an SRB with a CDB to exchange the media and sends it to the system port driver.

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

[**ChangerMoveMedium**](changermovemedium.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_EXCHANGE\_MEDIUM**](changer-exchange-medium.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerExchangeMedium%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






