---
title: IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS control code
description: Initializes the status of all elements or of specified number of elements of a particular type.
ms.assetid: 25cbb42a-7263-47b7-84c7-cfcb41a858c8
keywords:
- IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS control code

Initializes the status of all elements or of specified number of elements of a particular type.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an [**CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](changer-initialize-element-status.md) structure that indicates the element type and the number of elements to initialize. If the **BarCodeScan** member is **TRUE** and CHANGER\_BAR\_CODE\_SCANNER\_INSTALLED is also set in **Features0** of [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md), the elements should be initialized using a bar code scan.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(CHANGER\_INITIALIZE\_ELEMENT\_STATUS).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to **sizeof**(CHANGER\_INITIALIZE\_ELEMENT\_STATUS). The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_ELEMENT\_ADDRESS, or STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](changer-initialize-element-status.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






