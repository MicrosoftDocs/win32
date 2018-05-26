---
title: ChangerSetPosition function
description: ChangerSetPosition handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_SET\_POSITION.
ms.assetid: cab12c57-dd2b-4453-90ed-7f8954e0fe5d
keywords:
- ChangerSetPosition function Storage Devices
topic_type:
- apiref
api_name:
- ChangerSetPosition
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

# ChangerSetPosition function

**ChangerSetPosition** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md).

## Syntax


```C++
NTSTATUS ChangerSetPosition(
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

If the changer supports setting the position of the transport element, **ChangerSetPosition** returns the status returned by the system port driver, or one of the following values:

STATUS\_SUCCESS

STATUS\_INFO\_LENGTH\_MISMATCH

STATUS\_INVALID\_PARAMETER

STATUS\_INSUFFICIENT\_RESOURCES

If the changer does not support setting the position of the transport element, ChangerSetPosition returns STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

This routine is required.

**ChangerSetPosition** sets the changer's robotic transport mechanism to the specified destination, typically to optimize moving or exchanging media by first positioning the transport.

The CHANGER\_POSITION\_TO\_ELEMENT flag in **Features0** of [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) indicates whether the changer supports this functionality.

The changer class driver checks the input buffer length in the I/O stack location before calling **ChangerSetPosition**. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_SET\_POSITION**](changer-set-position.md) structure as an input parameter that indicates the transport element and the destination to set.

**ChangerSetPosition** first verifies that the transport and destination element addresses are valid and converts zero-based element addresses to device-specific addresses. It then builds an SRB with a CDB to position the element and sends it to the system port driver.

**ChangerSetPosition** sets the **Information** field in the I/O status block to **sizeof**(CHANGER\_SET\_POSITION) before returning to the changer class driver.

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

[**CHANGER\_SET\_POSITION**](changer-set-position.md)
</dt> <dt>

[**, IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerSetPosition%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






