---
title: IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS control code
description: Returns volume tag information for the specified elements.
ms.assetid: d2edc681-2a12-4281-81f5-147cf6c5e68f
keywords:
- IOCTL_CHANGER_QUERY_VOLUME_TAGS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_QUERY_VOLUME_TAGS
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS control code

Returns volume tag information for the specified elements.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** indicates the starting element for which to return information, the action to perform, and a template to use when searching for volume IDs.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**([**CHANGER\_SEND\_VOLUME\_TAG\_INFORMATION**](changer-send-volume-tag-information.md)).

## Output Buffer

The driver returns the [**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the parameter buffer for output, which must be &gt;= **sizeof**(READ\_ELEMENT\_ADDRESS\_INFO).

## Status block

The **Information** field is set to the correct output buffer size, in bytes. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_DEVICE\_REQUEST, or STATUS\_INVALID\_ELEMENT\_ADDRESS.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**READ\_ELEMENT\_ADDRESS\_INFO**](read-element-address-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_QUERY_VOLUME_TAGS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






