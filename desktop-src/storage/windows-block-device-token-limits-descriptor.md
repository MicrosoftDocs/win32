---
title: WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR structure
description: The WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR structure is the third party copy descriptor for Windows systems.
ms.assetid: A4DB93FE-96ED-4E6D-B912-31C53AD000FF
keywords:
- WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure Storage Devices
- PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR
api_location:
- scsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR structure

The **WINDOWS\_BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR** structure is the third party copy descriptor for Windows systems. This structure serves as the descriptor for the vital product data (VPD) third party copy page.

## Syntax


```C++
typedef struct _WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR {
  UCHAR DescriptorType[2];
  UCHAR DescriptorLength[2];
  UCHAR VendorSpecific[6];
  UCHAR MaximumRangeDescriptors[2];
  UCHAR MaximumInactivityTimer[4];
  UCHAR DefaultInactivityTimer[4];
  UCHAR MaximumTokenTransferSize[8];
  UCHAR OptimalTransferCount[8];
} WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR, *PWINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR;
```



## Members

<dl> <dt>

**DescriptorType**
</dt> <dd>

The descriptor type identifying this structure. The descriptor type is defined in *storport.h* as **BLOCK\_DEVICE\_TOKEN\_LIMITS\_DESCRIPTOR\_TYPE\_WINDOWS**.

</dd> <dt>

**DescriptorLength**
</dt> <dd>

The length of this structure starting with the **VendorSpecific** member.

</dd> <dt>

**VendorSpecific**
</dt> <dd>

Vendor specific bytes included in the descriptor. Windows applications must treat this member as reserved and ignore the reported value.

</dd> <dt>

**MaximumRangeDescriptors**
</dt> <dd>

The maximum number of range descriptors that may be included along with the [**POPULATE\_TOKEN\_HEADER**](populate-token-header.md) or the [**WRITE\_USING\_TOKEN\_HEADER**](write-using-token-header.md) structures.

</dd> <dt>

**MaximumInactivityTimer**
</dt> <dd>

The maximum available to specify as the timeout value in the **InactivityTimeout** member of the [**POPULATE\_TOKEN\_HEADER**](populate-token-header.md) structure.

</dd> <dt>

**DefaultInactivityTimer**
</dt> <dd>

The default value that is used by the copy provider when the **InactivityTimeout** of the [**POPULATE\_TOKEN\_HEADER**](populate-token-header.md) structure is set to 0.

</dd> <dt>

**MaximumTokenTransferSize**
</dt> <dd>

The maximum number of logical blocks that can be specified as a total of the block range descriptors in the [**POPULATE\_TOKEN\_HEADER**](populate-token-header.md) or the [**WRITE\_USING\_TOKEN\_HEADER**](write-using-token-header.md) structures.

</dd> <dt>

**OptimalTransferCount**
</dt> <dd>

The optimal number of logical blocks, as a maximum, to specify as a total of the block range descriptors in the [**POPULATE\_TOKEN\_HEADER**](populate-token-header.md) or the [**WRITE\_USING\_TOKEN\_HEADER**](write-using-token-header.md) structures. Offload data transfer performance may degrade if the transfer count is larger than this value.

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

[**POPULATE\_TOKEN\_HEADER**](populate-token-header.md)
</dt> <dt>

[**VPD\_THIRD\_PARTY\_COPY\_PAGE**](vpd-third-party-copy-page.md)
</dt> <dt>

[**WRITE\_USING\_TOKEN\_HEADER**](write-using-token-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






