---
title: IOCTL\_CHANGER\_GET\_PARAMETERS control code
description: Returns the parameters of the device.
ms.assetid: 'c4a6faa4-f3ea-4504-8d3b-a34465c90273'
keywords: ["IOCTL_CHANGER_GET_PARAMETERS control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_GET_PARAMETERS
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
---

# IOCTL\_CHANGER\_GET\_PARAMETERS control code

Returns the parameters of the device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(GET\_CHANGER\_PARAMETERS).

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH or STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_GET_PARAMETERS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






