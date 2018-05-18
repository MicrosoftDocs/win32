---
title: BLOCK\_DEVICE\_TOKEN\_DESCRIPTOR structure
description: BLOCK\_DEVICE\_TOKEN\_DESCRIPTOR contains the token returned from a the POPULATE TOKEN command for an offload read data operation.
ms.assetid: 'AD4E4EF6-F033-4226-9DC6-A6E55E965B4C'
keywords: ["BLOCK_DEVICE_TOKEN_DESCRIPTOR structure Storage Devices", "PBLOCK_DEVICE_TOKEN_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- BLOCK_DEVICE_TOKEN_DESCRIPTOR
api_location:
- scsi.h
api_type:
- HeaderDef
---

# BLOCK\_DEVICE\_TOKEN\_DESCRIPTOR structure

**BLOCK\_DEVICE\_TOKEN\_DESCRIPTOR** contains the token returned from a the POPULATE TOKEN command for an offload read data operation. The token information is included as part of the [**RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER**](receive-token-information-response-header.md) structure.

## Syntax


```C++
typedef struct _BLOCK_DEVICE_TOKEN_DESCRIPTOR {
  UCHAR TokenIdentifier[2];
  UCHAR Token[BLOCK_DEVICE_TOKEN_SIZE];
} BLOCK_DEVICE_TOKEN_DESCRIPTOR, *PBLOCK_DEVICE_TOKEN_DESCRIPTOR;
```



## Members

<dl> <dt>

**TokenIdentifier**
</dt> <dd>

An identifier value assigned by the copy provider to provide uniqueness to **Token** while the value of **Token** is valid. This member is reserved for system use and must not be modified.

</dd> <dt>

**Token**
</dt> <dd>

A data value defining a token as a point-in-time representation of data (ROD) for an offload read data operation. **Token** is an opaque value and must be used unmodified in offload write data operations.

</dd> </dl>

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER**](receive-token-information-response-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BLOCK_DEVICE_TOKEN_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






