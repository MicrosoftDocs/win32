---
title: IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS control code
description: Returns the status of all elements or the status of a specified number of elements of a particular type. For a description of the possible element types, see CHANGER\_ELEMENT.
ms.assetid: '5611bd28-16ed-4af1-a01c-07ef590bad65'
keywords: ["IOCTL_CHANGER_GET_ELEMENT_STATUS control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_GET_ELEMENT_STATUS
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
---

# IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS control code

Returns the status of all elements or the status of a specified number of elements of a particular type.

For a description of the possible element types, see [**CHANGER\_ELEMENT**](changer-element.md).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the [**CHANGER\_READ\_ELEMENT\_STATUS**](changer-read-element-status.md) data that indicates the element type and the number of elements for which to return status.

If the caller sets the **VolumeTagInfo** member of CHANGER\_READ\_ELEMENT\_STATUS to **TRUE**, the element status that is returned will include volume tag information.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer for input, which must be &gt;= **sizeof**(CHANGER\_READ\_ELEMENT\_STATUS).

## Output Buffer

The changer miniclass driver returns the changer element status data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. Some elements of type **ChangerDrive** return product information data. If the device provides product information, the miniclass driver will report the element status data in a structure of type [**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md). The miniclass driver sets ELEMENT\_STATUS\_PRODUCT\_DATA in the **Flags** member of the structure to indicate that it contains product information data. For elements of all types other than **ChangerDrive**, the driver reports element status data in a structure of type [**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md).

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the parameter buffer for output. For elements of type **ChangerDrive**, this value must be &gt;= *NumberOfElements* \* **sizeof**(CHANGER\_ELEMENT\_STATUS\_EX). For elements of all other types, this value must be &gt;= *NumberOfElements* \* **sizeof**(CHANGER\_ELEMENT\_STATUS).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL, STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_ELEMENT\_ADDRESS, or STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT\_STATUS**](changer-element-status.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_STATUS\_EX**](changer-element-status-ex.md)
</dt> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_GET_ELEMENT_STATUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






