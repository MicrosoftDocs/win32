---
title: VPD\_THIRD\_PARTY\_COPY\_PAGE structure
description: The VPD\_THIRD\_PARTY\_COPY\_PAGE structure defines the vital product data (VPD) page for offload data transfer operations.
ms.assetid: E8D9E05C-26C3-474C-854F-9AD12C8834DF
keywords:
- VPD_THIRD_PARTY_COPY_PAGE structure Storage Devices
- PVPD_THIRD_PARTY_COPY_PAGE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- VPD_THIRD_PARTY_COPY_PAGE
api_location:
- scsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VPD\_THIRD\_PARTY\_COPY\_PAGE structure

The **VPD\_THIRD\_PARTY\_COPY\_PAGE** structure defines the vital product data (VPD) page for offload data transfer operations.

## Syntax


```C++
typedef struct _VPD_THIRD_PARTY_COPY_PAGE {
  UCHAR DeviceType  :5;
  UCHAR DeviceTypeQualifier  :3;
  UCHAR PageCode;
  UCHAR PageLength[2];
  UCHAR ThirdPartyCopyDescriptors[ANYSIZE_ARRAY];
} VPD_THIRD_PARTY_COPY_PAGE, *PVPD_THIRD_PARTY_COPY_PAGE;
```



## Members

<dl> <dt>

**DeviceType**
</dt> <dd>

The device type. This is the same device type defined for use in the inquiry data for the storage device.

</dd> <dt>

**DeviceTypeQualifier**
</dt> <dd>

A qualifier code for the device. Currently, **DEVICE\_CONNECTED**, is the only valid value.

</dd> <dt>

**PageCode**
</dt> <dd>

The page code for the VPD third party copy page. This page code is defined as 0x8f.

</dd> <dt>

**PageLength**
</dt> <dd>

The length, in bytes, of the VPD page. For offload data transfer on Windows, **PageLength** must be &gt;= 0x24.

</dd> <dt>

**ThirdPartyCopyDescriptors**
</dt> <dd>

Support descriptors for copy operations. On Windows systems, **ThirdPartyCopyDescriptors** will contain one descriptor formatted as a [**WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR**](windows-block-device-token-limits-descriptor.md) structure.

</dd> </dl>

## Remarks

All multibyte values are in big endian format. Prior to evaluation, these values must be converted to match the endian format of the current platform.

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR**](windows-block-device-token-limits-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VPD_THIRD_PARTY_COPY_PAGE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






