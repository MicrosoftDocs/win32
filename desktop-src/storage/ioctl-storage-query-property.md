---
title: IOCTL\_STORAGE\_QUERY\_PROPERTY control code
description: A driver can use IOCTL\_STORAGE\_QUERY\_PROPERTY to return properties of a storage device or adapter.
ms.assetid: b68c5971-6d09-49a8-873d-8736068f6003
keywords:
- IOCTL_STORAGE_QUERY_PROPERTY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_QUERY_PROPERTY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_STORAGE\_QUERY\_PROPERTY control code

A driver can use **IOCTL\_STORAGE\_QUERY\_PROPERTY** to return properties of a storage device or adapter. The request indicates the kind of information to retrieve, such as inquiry data for a device or capabilities and limitations of an adapter. **IOCTL\_STORAGE\_QUERY\_PROPERTY** can also be used to determine whether the port driver supports a particular property or which fields in the property descriptor can be modified with a subsequent change-property request.

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)).

**Irp-&gt;AssociatedIrp.SystemBuffer** contains [**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md) data that specifies whether to query the device or the adapter, the type of query to perform, and any additional parameters required for the query, such as the page code for a particular SCSI mode sense page. Device properties must be retrieved only from a device; attempting to retrieve device properties from an adapter will cause an error.

**Parameters.DeviceIoControl.OutputBufferLength** indicates the number of bytes that can be written to **Irp-&gt;AssociatedIrp.SystemBuffer**. **OutputBufferLength** can be zero to determine whether a property exists without retrieving its data.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)).

## Output Buffer

The driver returns query data to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. Varying amounts of bus-specific data can be appended to the structure.

## Output Buffer Length

Cast the structure returned to a [**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md) and check its **Size** member to determine the number of bytes the structure actually requires.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_INVALID\_PARAMETER, or STATUS\_NOT\_SUPPORTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_DESCRIPTOR\_HEADER**](storage-descriptor-header.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_RPMB\_DATA\_FRAME**](storage-storage_rpmb_data_frame)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_QUERY_PROPERTY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






