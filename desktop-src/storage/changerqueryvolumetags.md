---
title: ChangerQueryVolumeTags function
description: ChangerQueryVolumeTags handles the device-specific aspects of a device-control IRP with the IOCTL code of IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS.
ms.assetid: '65579299-829c-48e2-b2f6-dc1a09578e9a'
keywords: ["ChangerQueryVolumeTags function Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerQueryVolumeTags
api_location:
- mcd.h
api_type:
- HeaderDef
---

# ChangerQueryVolumeTags function

**ChangerQueryVolumeTags** handles the device-specific aspects of a device-control IRP with the IOCTL code of [**IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS**](ioctl-changer-query-volume-tags.md).

## Syntax


```C++
NTSTATUS ChangerQueryVolumeTags(
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

If the changer supports retrieval of volume tag information, **ChangerQueryVolumeTags** returns the STATUS\_*XXX* value returned by the system port driver, or one of the following values:

STATUS\_SUCCESS

STATUS\_INVALID\_ELEMENT\_ADDRESS

STATUS\_INSUFFICIENT\_RESOURCES

If the changer does not support retrieval of volume tag information, ChangerQueryVolumeTags returns STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

This routine combines the functionality of two SCSI commands: SEND VOLUME TAGS and REQUEST VOLUME ELEMENT ADDRESS. This routine is required.

**ChangerQueryVolumeTags** retrieves volume tag information for specified elements. It can also be used to define or clear volume tag information if the changer supports these operations. The CHANGER\_VOLUME\_IDENTIFICATION flag in the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure indicates whether the changer supports this functionality.

The changer class driver checks the input and output buffer lengths in the I/O stack location before calling **ChangerQueryVolumeTags**. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md) structure that indicates the elements, the operation to perform, and a template that specifies the volume ID to search for or to set.

**ChangerQueryVolumeTags** first checks the action code for unsupported operations, and returns STATUS\_INVALID\_DEVICE\_REQUEST for those it does not support. Next, it builds an SRB with a CDB to indicate the device-specific address of the starting element and sends it to the system port driver, passing the volume ID template as a parameter. (For a SCSI changer, the miniclass driver uses the SCSI command SEND VOLUME TAG.)

If the first SRB succeeds, **ChangerQueryVolumeTags** builds a second SRB with a CDB to transfer the results of the previous SRB. (For a SCSI changer, the miniclass driver uses the SCSI command REQUEST VOLUME ELEMENT ADDRESS.)

**ChangerQueryVolumeTags** then fills in a [**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md) structure at *Irp***-&gt;AssociatedIrp.SystemBuffer** that indicates the number of elements for which volume tag information was transferred, and the information for each element.

After filling in the system buffer, **ChangerQueryVolumeTags** sets the **Information** field in the I/O status block to the number of bytes written to the buffer before returning to the changer class driver.

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

[**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md)
</dt> <dt>

[**, GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerQueryVolumeTags%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






