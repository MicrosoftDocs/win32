---
title: POPULATE\_TOKEN\_HEADER structure
description: A populate token parameter list starts with a POPULATE\_TOKEN\_HEADER structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command.
ms.assetid: '897C74A3-041D-487E-8891-7161B76ABAA1'
keywords: ["POPULATE_TOKEN_HEADER structure Storage Devices", "PPOPULATE_TOKEN_HEADER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- POPULATE_TOKEN_HEADER
api_location:
- scsi.h
api_type:
- HeaderDef
---

# POPULATE\_TOKEN\_HEADER structure

A populate token parameter list starts with a **POPULATE\_TOKEN\_HEADER** structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command.

## Syntax


```C++
typedef struct _POPULATE_TOKEN_HEADER {
  UCHAR PopulateTokenDataLength[2];
  UCHAR Immediate  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2;
  UCHAR InactivityTimeout[4];
  UCHAR Reserved3[6];
  UCHAR BlockDeviceRangeDescriptorListLength[2];
  UCHAR BlockDeviceRangeDescriptor[ANYSIZE_ARRAY];
} POPULATE_TOKEN_HEADER, *PPOPULATE_TOKEN_HEADER;
```



## Members

<dl> <dt>

**PopulateTokenDataLength**
</dt> <dd>

The length of this structure beginning with the *Immediate* parameter and include all of the elements of the **BlockDeviceRangeDescriptor** array.

</dd> <dt>

**Immediate**
</dt> <dd>

If set, the status of the POPULATE TOKEN command is returned immediately after receipt and validation of the range descriptors. Otherwise, status is returned after all command processing is complete.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved bits.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**InactivityTimeout**
</dt> <dd>

The timeout duration for which the copy provider waits for the next command using the token created for this representation of data (ROD). The validity of the token created for the ROD described by this structure expires at this timeout value.

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

An array of [**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md) structures which describe the logical blocks representing the file being read from the LUN.

</dd> </dl>

## Remarks

The **POPULATE\_TOKEN\_HEADER** structure contains a series of [**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md) structures which describe the token ROD.

All multibyte values are in big endian format. Prior to setting, these values must be converted from the endian format of the current platform.

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**BLOCK\_DEVICE\_RANGE\_DESCRIPTOR**](block-device-range-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20POPULATE_TOKEN_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






