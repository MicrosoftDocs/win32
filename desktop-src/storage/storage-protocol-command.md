---
title: STORAGE\_PROTOCOL\_COMMAND structure
description: This structure is used as an input buffer when using the pass-through mechanism to issue a vendor-specific command to a storage device (via IOCTL\_STORAGE\_PROTOCOL\_COMMAND).
ms.assetid: 1AA59350-2475-4BF7-B447-42FDDB311882
keywords:
- STORAGE_PROTOCOL_COMMAND structure Storage Devices
- PSTORAGE_PROTOCOL_COMMAND structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_COMMAND
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_PROTOCOL\_COMMAND structure

This structure is used as an input buffer when using the pass-through mechanism to issue a vendor-specific command to a storage device (via [**IOCTL\_STORAGE\_PROTOCOL\_COMMAND**](ioctl-storage-protocol-command.md)).

## Syntax


```C++
typedef struct _STORAGE_PROTOCOL_COMMAND {
  ULONG                                        Version;
  ULONG                                        Length;
  STORAGE_PROTOCOL_TYPE                        ProtocolType;
  ULONG                                        Flags;
  ULONG                                        ReturnStatus;
  ULONG                                        ErrorCode;
  ULONG                                        CommandLength;
  ULONG                                        ErrorInfoLength;
  ULONG                                        DataToDeviceTransferLength;
  ULONG                                        DataFromDeviceTransferLength;
  ULONG                                        TimeOutValue;
  ULONG                                        ErrorInfoOffset;
  ULONG                                        DataToDeviceBufferOffset;
  ULONG                                        DataFromDeviceBufferOffset;
  ULONG                                        CommandSpecific;
  ULONG                                        Reserved0;
  ULONG                                        FixedProtocolReturnData;
  ULONG                                        Reserved1[3];
  _Field_size_bytes_full_(CommandLength) UCHAR Command[ANYSIZE_ARRAY];
} STORAGE_PROTOCOL_COMMAND, *PSTORAGE_PROTOCOL_COMMAND;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to **STORAGE\_PROTOCOL\_STRUCTURE\_VERSION**.

</dd> <dt>

**Length**
</dt> <dd>

The size of this structure. This should be set to sizeof(**STORAGE\_PROTOCOL\_COMMAND**).

</dd> <dt>

**ProtocolType**
</dt> <dd>

The protocol type.

</dd> <dt>

**Flags**
</dt> <dd>

Flags set for this request. The following are valid flags.



| Flag                                                   | Description                                                             |
|--------------------------------------------------------|-------------------------------------------------------------------------|
| **STORAGE\_PROTOCOL\_COMMAND\_FLAG\_ADAPTER\_REQUEST** | This flag indicates the request to target an adapter instead of device. |



 

</dd> <dt>

**ReturnStatus**
</dt> <dd>

The status of the request made to the storage device. In Windows 10, possible values include:



| Status value                                           | Description                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------|
| **STORAGE\_PROTOCOL\_STATUS\_PENDING**                 | The request is pending.                                               |
| **STORAGE\_PROTOCOL\_STATUS\_SUCCESS**                 | The request has completed successfully.                               |
| **STORAGE\_PROTOCOL\_STATUS\_ERROR**                   | The request has encountered an error.                                 |
| **STORAGE\_PROTOCOL\_STATUS\_INVALID\_REQUEST**        | The request is not valid.                                             |
| **STORAGE\_PROTOCOL\_STATUS\_NO\_DEVICE**              | A device is not available to make a request to.                       |
| **STORAGE\_PROTOCOL\_STATUS\_BUSY**                    | The device is busy acting on the request.                             |
| **STORAGE\_PROTOCOL\_STATUS\_DATA\_OVERRUN**           | The device encountered a data overrun while acting on the request.    |
| **STORAGE\_PROTOCOL\_STATUS\_INSUFFICIENT\_RESOURCES** | The device cannot complete the request due to insufficient resources. |
| **STORAGE\_PROTOCOL\_STATUS\_NOT\_SUPPORTED**          | The request is not supported.                                         |



 

</dd> <dt>

**ErrorCode**
</dt> <dd>

The error code for this request. This is optionally set.

</dd> <dt>

**CommandLength**
</dt> <dd>

The length of the command. A non-zero value must be set by the caller.

</dd> <dt>

**ErrorInfoLength**
</dt> <dd>

The length of the error buffer. This is optionally set and can be set to 0.

</dd> <dt>

**DataToDeviceTransferLength**
</dt> <dd>

The size of the buffer that is to be transferred to the device. This is only used with a WRITE request.

</dd> <dt>

**DataFromDeviceTransferLength**
</dt> <dd>

The size of the buffer this is to be transferred from the device. This is only used with a READ request.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

How long to wait for the device until timing out. This is set in units of seconds.

</dd> <dt>

**ErrorInfoOffset**
</dt> <dd>

The offset of the error buffer. This must be pointer-aligned.

</dd> <dt>

**DataToDeviceBufferOffset**
</dt> <dd>

The offset of the buffer that is to be transferred to the device. This must be pointer-aligned and is only used with a WRITE request.

</dd> <dt>

**DataFromDeviceBufferOffset**
</dt> <dd>

The offset of the buffer that is to be transferred from the device. This must be pointer-aligned and is only used with a READ request.

</dd> <dt>

**CommandSpecific**
</dt> <dd>

Command-specific data passed along with the command. This depends on the command from the driver, and is optionally set.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**FixedProtocolReturnData**
</dt> <dd>

The return data. This is optionally set. Some protocols such as NVMe, may return a small amount of data (DWORD0 from completion queue entry) without the need of a separate device data transfer.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Command\[ANYSIZE\_ARRAY\]**
</dt> <dd>

The vendor-specific command that is to be passed-through to the device.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_PROTOCOL\_COMMAND**](ioctl-storage-protocol-command.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_COMMAND%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






