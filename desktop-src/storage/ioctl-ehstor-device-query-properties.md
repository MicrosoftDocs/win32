---
title: IOCTL\_EHSTOR\_DEVICE\_QUERY\_PROPERTIES control code
description: A silo driver sends this IOCTL to the storage device stack to query for storage device properties. The Enhanced Storage Class Driver (EHSTOR) will handle the request and return the available properties.
ms.assetid: 2F9B880F-7F3A-4B2B-816E-AD85ADFB280B
keywords:
- IOCTL_EHSTOR_DEVICE_QUERY_PROPERTIES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_QUERY_PROPERTIES
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_EHSTOR\_DEVICE\_QUERY\_PROPERTIES control code

A silo driver sends this IOCTL to the storage device stack to query for storage device properties. The Enhanced Storage Class Driver (EHSTOR) will handle the request and return the available properties.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an **EHSTOR\_DEVICE\_PROPERTIES** structure. **EHSTOR\_DEVICE\_PROPERTIES** is declared in *ehstorioctl.h* as the following.


```
typedef struct _EHSTOR_DEVICE_PROPERTIES
{
    ULONG  StructSize;
    ULONG  BytesPerSector;
} EHSTOR_DEVICE_PROPERTIES;
```



<dl> <dt>

<span id="StructSize"></span><span id="structsize"></span><span id="STRUCTSIZE"></span>StructSize
</dt> <dd>

The size of the structure. This is set to **sizeof**(EHSTOR\_DEVICE\_PROPERTIES).

</dd> <dt>

<span id="BytesPerSector"></span><span id="bytespersector"></span><span id="BYTESPERSECTOR"></span>BytesPerSector
</dt> <dd>

The size, in bytes, of a sector on the underlying storage device.

</dd> </dl>

## Output Buffer Length

an **EHSTOR\_DEVICE\_PROPERTIES** structure.

## Status block

STATUS\_SUCCESS is returned in the **Status** field if device properties are returned in the system buffer. Otherwise, another appropriate status code is returned.

## Remarks

Currently, bytes per sector is the only property available in **EHSTOR\_DEVICE\_PROPERTIES**.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**SILO\_DRIVER\_CAPABILITES**](act-authz-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_QUERY_PROPERTIES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






