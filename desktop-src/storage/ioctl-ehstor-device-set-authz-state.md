---
title: IOCTL\_EHSTOR\_DEVICE\_SET\_AUTHZ\_STATE control code
description: This IOCTL is used to inform the owning driver for the IEEE 1667 device PDOs that the authorization state has changed.
ms.assetid: 8C71F597-2141-4DA6-8A14-8B10CB69E5CC
keywords:
- IOCTL_EHSTOR_DEVICE_SET_AUTHZ_STATE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_SET_AUTHZ_STATE
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_EHSTOR\_DEVICE\_SET\_AUTHZ\_STATE control code

This IOCTL is used to inform the owning driver for the IEEE 1667 device PDOs that the authorization state has changed. The owning driver may choose to change the state of the disk PDO in response to this IOCTL. In the case of *EhStorClass.sys*, the disk PDO is added or removed based on the authorization value in the input buffer of this IOCTL. Typically this IOCTL is issued by a UMDF authentication silo driver, such as the password or certificate driver, immediately following a successful silo operation which has changed the authentication state of the silo.

## Input Buffer

The input buffer at Irp-&gt;AssociatedIrp.SystemBuffer must contain a structure of type [**ACT\_AUTHZ\_STATE**](act-authz-state.md).

## Input Buffer Length

The length of an [**ACT\_AUTHZ\_STATE**](act-authz-state.md) structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values may be returned in the Status field:

<dl> STATUS\_SUCCESS - The authorization state for the ACT was successfully set according to the data contained in the input buffer.  
</dl>

<dl> STATUS\_INVALID\_BUFFER\_SIZE - The input buffer length supplied is of incorrect size.  
</dl>

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_SET_AUTHZ_STATE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





