---
title: SENDCMDINPARAMS structure
description: The SENDCMDINPARAMS structure contains the input parameters for the SMART\_SEND\_DRIVE\_COMMAND request.
ms.assetid: 4c02da7e-2d93-4e0c-9666-acb380c6d39a
keywords:
- SENDCMDINPARAMS structure Storage Devices
- PSENDCMDINPARAMS structure pointer Storage Devices
- LPSENDCMDINPARAMS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SENDCMDINPARAMS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SENDCMDINPARAMS structure

The SENDCMDINPARAMS structure contains the input parameters for the [**SMART\_SEND\_DRIVE\_COMMAND**](smart-send-drive-command.md) request.

## Syntax


```C++
typedef struct _SENDCMDINPARAMS {
  ULONG   cBufferSize;
  IDEREGS irDriveRegs;
  UCHAR   bDriveNumber;
  UCHAR   bReserved[3];
  ULONG   dwReserved[4];
  UCHAR   bBuffer[1];
} SENDCMDINPARAMS, *PSENDCMDINPARAMS, *LPSENDCMDINPARAMS;
```



## Members

<dl> <dt>

**cBufferSize**
</dt> <dd>

Contains the buffer size, in bytes.

</dd> <dt>

**irDriveRegs**
</dt> <dd>

Contains a [**IDEREGS**](ideregs.md) structure used to report the contents of the IDE controller registers.

</dd> <dt>

**bDriveNumber**
</dt> <dd>

The **bDriveNumber** member is opaque. Do not use it. The operating system ignores this member, because the physical drive that receives the request depends on the handle that the caller uses when making the request.

</dd> <dt>

**bReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**bBuffer**
</dt> <dd>

Pointer to the input buffer.

</dd> </dl>

## Remarks

The [**SMART\_SEND\_DRIVE\_COMMAND**](smart-send-drive-command.md) is used to send a Self-Monitoring Analysis and Reporting Technology (SMART) commands to a device.

The SENDCMDINPARAMS structure is also used with the [**SMART\_RCV\_DRIVE\_DATA**](smart-rcv-drive-data.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SMART\_SEND\_DRIVE\_COMMAND**](smart-send-drive-command.md)
</dt> <dt>

[**SMART\_RCV\_DRIVE\_DATA**](smart-rcv-drive-data.md)
</dt> <dt>

[**SENDCMDOUTPARAMS**](sendcmdoutparams.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SENDCMDINPARAMS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






