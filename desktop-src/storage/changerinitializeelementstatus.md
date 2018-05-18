---
title: ChangerInitializeElementStatus function
description: ChangerInitializeElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS.
ms.assetid: '1f8f13e0-b0d3-4c94-bd1f-0e42bb75142d'
keywords: ["ChangerInitializeElementStatus function Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerInitializeElementStatus
api_location:
- mcd.h
api_type:
- HeaderDef
---

# ChangerInitializeElementStatus function

**ChangerInitializeElementStatus** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md).

## Syntax


```C++
NTSTATUS ChangerInitializeElementStatus(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
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

**ChangerInitializeElementStatus** returns the status returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INVALID\_PARAMETER

STATUS\_INSUFFICIENT\_RESOURCES

If the changer does not support initializing a range of elements of a particular type and ChangerInitializeElementStatus is called with an element type other than AllElements, it returns STATUS\_INVALID\_PARAMETER.

## Remarks

This routine is required.

**ChangerInitializeElementStatus** updates the changer's internal memory with current information about its elements.

The changer class driver checks the input buffer length in the I/O stack location before calling **ChangerInitializeElementStatus**.

*Irp***-&gt;SystemBuffer** points to a [**CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](changer-initialize-element-status.md) structure as an input parameter that indicates the elements for which to initialize status and whether to initialize element status with data obtained from bar code labels.

For a SCSI changer, **ChangerInitializeElementStatus** builds an SRB with a CDB to initialize element status, translates zero-based element addresses to device-specific addresses, and sends the SRB to the system port driver.

**ChangerInitializeElementStatus** sets the **Information** field in the I/O status block to **sizeof**(CHANGER\_INITIALIZE\_ELEMENT\_STATUS) before returning to the changer class driver.

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

[**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)
</dt> <dt>

[**CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](changer-initialize-element-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerInitializeElementStatus%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






