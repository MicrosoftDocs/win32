---
title: MPIO\_DEVINSTANCE\_HEALTH\_CLASS structure
description: The MPIO\_DEVINSTANCE\_HEALTH\_CLASS structure holds the health information for a instance of a device exposed through the specified path identifiers.
ms.assetid: 6d0afab5-4aba-4ebc-a864-85c83cf464d0
keywords:
- MPIO_DEVINSTANCE_HEALTH_CLASS structure Storage Devices
- PMPIO_DEVINSTANCE_HEALTH_CLASS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_DEVINSTANCE_HEALTH_CLASS
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPIO\_DEVINSTANCE\_HEALTH\_CLASS structure

The MPIO\_DEVINSTANCE\_HEALTH\_CLASS structure holds the health information for a instance of a device exposed through the specified path identifiers.

## Syntax


```C++
typedef struct _MPIO_DEVINSTANCE_HEALTH_CLASS {
  ULONGLONG PathId;
  ULONGLONG NumberReads;
  ULONGLONG NumberWrites;
  ULONGLONG NumberBytesRead;
  ULONGLONG NumberBytesWritten;
  ULONGLONG NumberRetries;
  ULONGLONG NumberIoErrors;
  ULONGLONG CreateTime;
  ULONGLONG FailTime;
  BOOLEAN   DeviceOffline;
  UCHAR     NumberReadsWrap;
  UCHAR     NumberWritesWrap;
  UCHAR     NumberBytesReadWrap;
  UCHAR     NumberBytesWrittenWrap;
  UCHAR     Pad[3];
} MPIO_DEVINSTANCE_HEALTH_CLASS, *PMPIO_DEVINSTANCE_HEALTH_CLASS;
```



## Members

<dl> <dt>

**PathId**
</dt> <dd>

An unsigned 64-bitfield that returns the path identifier that is associated with this instance of a multi-path disk.

</dd> <dt>

**NumberReads**
</dt> <dd>

An unsigned 64-bitfield that specifies the number of read requests that are serviced by the specified path identifier.

</dd> <dt>

**NumberWrites**
</dt> <dd>

An unsigned 64-bitfield that specifies the number of write requests that are serviced by the specified path identifier

</dd> <dt>

**NumberBytesRead**
</dt> <dd>

An unsigned 64-bitfield that specifies the total number of bytes that are read through the specified path identifier

</dd> <dt>

**NumberBytesWritten**
</dt> <dd>

An unsigned 64-bitfield that specifies the total number of bytes that are written through the specified path identifier.

</dd> <dt>

**NumberRetries**
</dt> <dd>

An unsigned 64-bitfield that specifies the total number of retries through the specified path identifier.

</dd> <dt>

**NumberIoErrors**
</dt> <dd>

An unsigned 64-bitfield that specifies the total number of I/O errors that are encountered through the specified path identifier.

</dd> <dt>

**CreateTime**
</dt> <dd>

A 64-bit integer that specifies the system time when this instance was created and exposed.

</dd> <dt>

**FailTime**
</dt> <dd>

A 64-bit integer that specifies the system time when the path associated with this path ID was removed.

</dd> <dt>

**DeviceOffline**
</dt> <dd>

A Boolean field that indicates whether the path associated with this path ID has been removed.

</dd> <dt>

**NumberReadsWrap**
</dt> <dd>

An unsigned character field that specifies the total number of times the *NumberReads* parameter has rolled around to zero.

</dd> <dt>

**NumberWritesWrap**
</dt> <dd>

An unsigned character field that specifies the total number of times the *NumberWrites* parameter has rolled around to zero.

</dd> <dt>

**NumberBytesReadWrap**
</dt> <dd>

An unsigned character field that specifies the total number of times the *NumberBytesRead* parameter has rolled around to zero.

</dd> <dt>

**NumberBytesWrittenWrap**
</dt> <dd>

An unsigned character field that specifies the total number of times the *NumberBytesWritten* parameter has rolled around to zero.

</dd> <dt>

**Pad**
</dt> <dd>

Should be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DEVINSTANCE_HEALTH_CLASS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





