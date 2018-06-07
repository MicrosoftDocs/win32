---
title: WRITE\_USING\_TOKEN\_HEADER structure
description: The WRITE\_USING\_TOKEN\_HEADER structure describes the destination data locations for an offload write data operation.
ms.assetid: A46ED23A-7DB0-4792-B903-F748BCDAD55E
keywords:
- WRITE_USING_TOKEN_HEADER structure Storage Devices
- PWRITE_USING_TOKEN_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- WRITE_USING_TOKEN_HEADER
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

# WRITE\_USING\_TOKEN\_HEADER structure

The **WRITE\_USING\_TOKEN\_HEADER** structure describes the destination data locations for an offload write data operation. The offload write data operation described by this structure is associated with a token representation of data (ROD).

## Syntax


```C++
typedef struct _WRITE_USING_TOKEN_HEADER {
  UCHAR WriteUsingTokenDataLength[2];
  UCHAR Immediate  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2[5];
  UCHAR BlockOffsetIntoToken[8];
  UCHAR Token[BLOCK_DEVICE_TOKEN_SIZE];
  UCHAR Reserved3[6];
  UCHAR BlockDeviceRangeDescriptorListLength[2];
  UCHAR BlockDeviceRangeDescriptor[ANYSIZE_ARRAY];
} WRITE_USING_TOKEN_HEADER, *PWRITE_USING_TOKEN_HEADER;
```



## Members

<dl> <dt>

**WriteUsingTokenDataLength**
</dt> <dd>

The length of this structure beginning with the *Immediate* parameter and include all of the elements of the **BlockDeviceRangeDescriptor** array.

</dd> <dt>

**Immediate**
</dt> <dd>

If set, the status of the WRITE USING TOKEN command is returned immediately after receipt and validation of the token ROD and range descriptors. Otherwise, status is returned after all command processing is complete.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved bits.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**BlockOffsetIntoToken**
</dt> <dd>

The offset, in logical blocks, in the ROD for **Token** indicating the start of the source data for the offload write data operation.

</dd> <dt>

**Token**
</dt> <dd>

A token created by a previous the POPULATE TOKEN command operation.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**BlockDeviceRangeDescriptorListLength**
</dt> <dd>

The length, in bytes, for all of the [**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md) structures in the **BlockDeviceRangeDescriptor** array.

</dd> <dt>

**BlockDeviceRangeDescriptor**
</dt> <dd>

An array of [**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md) structures which describe the destination data blocks for the offload write data transfer.

</dd> </dl>

## Remarks

All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md)
</dt> <dt>

[**POPULATE\_TOKEN\_HEADER**](populate-token-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_USING_TOKEN_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






