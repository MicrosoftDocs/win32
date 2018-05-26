---
title: IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES control code
description: This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of the silo drivers capabilities.
ms.assetid: AD78ABAD-5DCF-4E1A-B521-8063B5BEA6A6
keywords:
- IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES
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

# IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES control code

This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of the silo driver's capabilities. The silo driver sends this IOCTL with a [**SILO\_DRIVER\_CAPABILITES**](act-authz-state.md) structure that indicates whether authentication and banding are supported along with a list of EHSTOR IOCTLs it will handle.

## Input Buffer

The input buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** must contain a structure of type [**SILO\_DRIVER\_CAPABILITES**](act-authz-state.md). This structure is followed immediately by a list of which redirected IOCTLs the silo driver will handle.

## Input Buffer Length

The length of the buffer.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                    | Description                                                                  |
|---------------------------------|------------------------------------------------------------------------------|
| STATUS\_SUCCESS                 | The silo driver's capabilities were registered with the EHSTOR class driver. |
| STATUS\_INVALID\_BUFFER\_SIZE   | The input buffer length supplied is of incorrect size.                       |
| STATUS\_INVALID\_PARAMETER      | A capability parameter is incorrect.                                         |
| STATUS\_INSUFFICIENT\_RESOURCES | The IOCTL redirection list cannot be copied.                                 |
| STATUS\_NOT\_SUPPORTED          | The sending device is not a silo device.                                     |



 

## Remarks

This IOCTL is used by the Trusted Computing Group (TCG) standard authentication silo driver in Windows 8. On device initialization, the TCG silo driver will notify the EHSTOR class driver (EhStorClass.sys) of its capabilities by sending a **IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES** request with a [**SILO\_DRIVER\_CAPABILITIES**](silo-driver-capabilities.md) structure.

Silo device objects exist outside the storage device stack. Any EHSTOR request intended for a silo driver must be explicitly forwarded to it. This is the case for all band management IOCTLs. Band management requests are made on a file object representing a physical drive. These requests are sent down the storage device stack. If the silo driver has registered support for the IOCTL, the EHSTOR class driver will redirect the request to the silo driver.

IOCTL requests supported by a silo driver are included in an array following [**SILO\_DRIVER\_CAPABILITIES**](silo-driver-capabilities.md) in the system buffer. The size of the information in the system buffer should be specified as **sizeof**(SILO\_DRIVER\_CAPABILITIES) + (**sizeof**(ULONG) \* *RedirectedIoctlListCount*).

A vendor supplied non-TCG authentication silo driver must notify the EHSTOR class driver of its capabilities using this IOCTL.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**SILO\_DRIVER\_CAPABILITIES**](silo-driver-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






