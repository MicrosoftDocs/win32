---
title: BLOCK\_DEVICE\_RANGE\_DESCRIPTOR structure
description: The BLOCK\_DEVICE\_RANGE\_DESCRIPTOR structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation.
ms.assetid: '6B262D38-8BD6-43B5-96AB-6D311B8EBA88'
keywords: ["BLOCK_DEVICE_RANGE_DESCRIPTOR structure Storage Devices", "PBLOCK_DEVICE_RANGE_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- BLOCK_DEVICE_RANGE_DESCRIPTOR
api_location:
- scsi.h
api_type:
- HeaderDef
---

# BLOCK\_DEVICE\_RANGE\_DESCRIPTOR structure

The **BLOCK\_DEVICE\_RANGE\_DESCRIPTOR** structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation.

## Syntax


```C++
typedef struct _BLOCK_DEVICE_RANGE_DESCRIPTOR {
  UCHAR LogicalBlockAddress[8];
  UCHAR TransferLength[4];
  UCHAR Reserved[4];
} BLOCK_DEVICE_RANGE_DESCRIPTOR, *PBLOCK_DEVICE_RANGE_DESCRIPTOR;
```



## Members

<dl> <dt>

**LogicalBlockAddress**
</dt> <dd>

The starting logical block address of a block range.

</dd> <dt>

**TransferLength**
</dt> <dd>

The length, in logical blocks, of the block range.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved bytes.

</dd> </dl>

## Remarks

If *TransferLength* is set to 0, the range descriptor is considered valid and does not cause an error when included in a token parameter list. No operation will be performed for this descriptor.

All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**POPULATE\_TOKEN\_HEADER**](populate-token-header.md)
</dt> <dt>

[**WRITE\_USING\_TOKEN\_HEADER**](write-using-token-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BLOCK_DEVICE_RANGE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






