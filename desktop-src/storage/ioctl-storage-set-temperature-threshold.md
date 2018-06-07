---
title: IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD control code
description: A driver can use IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD to set the temperature threshold of a storage device (when supported by the hardware).
ms.assetid: 5D7348DC-1114-4346-9486-FCCE2C0F3E0F
keywords:
- IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD control code

A driver can use **IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD** to set the temperature threshold of a storage device (when supported by the hardware). Use [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to determine if the device supports changing the over and under temperature thresholds.

## Input Buffer

A [**STORAGE\_TEMPERATURE\_THRESHOLD**](storage-temperature-threshold.md) structure.

## Input Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**([**STORAGE\_TEMPERATURE\_THRESHOLD**](storage-temperature-threshold.md)).

## Output Buffer

This IOCTL has no output structure.

## Output Buffer Length

This IOCTL has no output structure.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to **STATUS\_SUCCESS**, or possibly to **STATUS\_INSUFFICIENT\_RESOURCES**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_ID**](storage-property-id.md)
</dt> <dt>

[**STORAGE\_TEMPERATURE\_INFO**](storage-temperature-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






