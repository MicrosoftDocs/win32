---
title: RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER structure
description: A token, created as a representation of data (ROD), for an offload read data operation is returned in a RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER structure.
ms.assetid: 54168476-1C55-4343-858C-7FBA863D35D0
keywords:
- RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure Storage Devices
- PRECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER
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

# RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER structure

A token, created as a representation of data (ROD), for an offload read data operation is returned in a **RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER** structure.

## Syntax


```C++
typedef struct _RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER {
  UCHAR TokenDescriptorsLength[4];
  UCHAR TokenDescriptor[ANYSIZE_ARRAY];
} RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER, *PRECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER;
```



## Members

<dl> <dt>

**TokenDescriptorsLength**
</dt> <dd>

The length, in bytes, of the **TokenDescriptor** member.

</dd> <dt>

**TokenDescriptor**
</dt> <dd>

The data containing a token created as the offload read ROD.

</dd> </dl>

## Remarks

The **RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER** structure is included with a [**RECEIVE\_TOKEN\_INFORMATION\_HEADER**](receive-token-information-header.md)structure as a response to a POPULATE TOKEN command. The **RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER** structure follows the **SenseData** member of **RECEIVE\_TOKEN\_INFORMATION\_HEADER**.

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

[**RECEIVE\_TOKEN\_INFORMATION\_HEADER**](receive-token-information-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






