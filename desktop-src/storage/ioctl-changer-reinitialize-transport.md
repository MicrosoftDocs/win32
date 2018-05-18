---
title: IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT control code
description: Physically recalibrates a transport element, typically after the changer has been powered on or a calling application has initiated a recovery operation. Recalibration may involve returning the transport to its \ 0034;home \ 0034; position.
ms.assetid: '35b40514-a7a6-4860-a633-fe273ef21ba2'
keywords: ["IOCTL_CHANGER_REINITIALIZE_TRANSPORT control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_REINITIALIZE_TRANSPORT
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
---

# IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT control code

Physically recalibrates a transport element, typically after the changer has been powered on or a calling application has initiated a recovery operation. Recalibration may involve returning the transport to its "home" position.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** indicates the element to initialize.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**([**CHANGER\_ELEMENT**](changer-element.md)).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to **sizeof**(CHANGER\_ELEMENT). The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_ELEMENT\_ADDRESS, or STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_REINITIALIZE_TRANSPORT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






