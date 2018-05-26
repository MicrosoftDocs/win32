---
title: IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES control code
description: The IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES request is sent to the storage class driver to determine available and used mapping resources on a storage device.
ms.assetid: 117F6507-CA52-4EA7-9633-75ADB19F4DDA
keywords:
- IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES
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

# IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES control code

The **IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES** request is sent to the storage class driver to determine available and used mapping resources on a storage device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains a [**STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES**](storage-lb-provisioning-map-resources.md) structure.

## Output Buffer Length

*Parameters.DeviceIoControl.OutputBufferLength* in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least **sizeof**(STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES).

## Status block

The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_BUFFER\_TOO\_SMALL, STATUS\_BUFFER\_OVERFLOW, or some other error status.

## Remarks

If logical block provisioning is enabled on a LUN, resource mapping counts may be reported from the storage device. Resource mapping information is obtained by using the **IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES** request. A storage monitoring application can use this IOCTL to query resource mapping conditions before a resource threshold or exhaustion event is logged.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 8 and later versions of Windows.<br/>                                           |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES**](storage-lb-provisioning-map-resources.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






