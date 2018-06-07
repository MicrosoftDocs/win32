---
title: ChangerGetElementStatus function
description: ChangerGetElementStatus handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS.
ms.assetid: 8114d029-fe6e-4466-9e54-5ceadef96949
keywords:
- ChangerGetElementStatus function Storage Devices
topic_type:
- apiref
api_name:
- ChangerGetElementStatus
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

# ChangerGetElementStatus function

**ChangerGetElementStatus** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md).

## Syntax


```C++
NTSTATUS ChangerGetElementStatus(
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

**ChangerGetElementStatus** returns the status returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INFO\_LENGTH\_MISMATCH

STATUS\_INSUFFICIENT\_RESOURCES

STATUS\_INVALID\_DEVICE\_REQUEST

STATUS\_INVALID\_ELEMENT\_ADDRESS

If VolumeTagInfo is set for a changer that does not support volume tag information, ChangerGetElementStatus returns STATUS\_INVALID\_PARAMETER.

## Remarks

This routine is required.

**ChangerGetElementStatus** returns the status and, optionally, volume tag information for all elements in a changer, or the status of a specific number of elements of a particular type.

The changer class driver checks the input and output buffer lengths in the I/O stack location before calling **ChangerGetElementStatus**.

*Irp***-&gt;SystemBuffer** points to a [**CHANGER\_READ\_ELEMENT\_STATUS**](changer-read-element-status.md) structure as an input parameter that indicates the elements for which to report status and whether to report volume tag information.

**ChangerGetElementStatus** first builds an SRB with a CDB to read element status command and sends it to the system port driver to retrieve the status of the changer's elements. For most element types, **ChangerGetElementStatus** then fills in a [**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md) structure at *Irp***-&gt;AssociatedIrp.SystemBuffer** for each element for which it reports status. However, some elements of type **ChangerDrive** return product information data. If the device provides product information, the miniclass driver must report the element status data in a structure of type [**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md) instead of using CHANGER\_ELEMENT\_STATUS. **ChangerGetElementStatus** must indicate that product information is present by setting ELEMENT\_STATUS\_PRODUCT\_DATA in the **Flags** member of the structure.

**ChangerGetElementStatus** sets the **Information** field in the I/O status block to the number of bytes returned before returning to the changer class driver.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**ChangerGetStatus**](changergetstatus.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> <dt>

[**ChangerQueryVolumeTags**](changerqueryvolumetags.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md)
</dt> <dt>

[**CHANGER\_READ\_ELEMENT STATUS**](changer-read-element-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerGetElementStatus%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






