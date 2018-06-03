---
title: PERSISTENT\_RESERVE\_COMMAND structure
description: The PERSISTENT\_RESERVE\_COMMAND structure is used together with the IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN and IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.
ms.assetid: c7debd93-0fcd-43c5-a950-8154b62175bf
keywords:
- PERSISTENT_RESERVE_COMMAND structure Storage Devices
- PPERSISTENT_RESERVE_COMMAND structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PERSISTENT_RESERVE_COMMAND
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PERSISTENT\_RESERVE\_COMMAND structure

The PERSISTENT\_RESERVE\_COMMAND structure is used together with the [**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN**](ioctl-storage-persistent-reserve-in.md) and [**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT**](ioctl-storage-persistent-reserve-out.md) requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.

## Syntax


```C++
typedef struct _PERSISTENT_RESERVE_COMMAND {
  ULONG Version;
  ULONG Size;
  union {
    struct {
      UCHAR  ServiceAction  :5;
      UCHAR  Reserved1  :3;
      USHORT AllocationLength;
    } PR_IN;
    struct {
      UCHAR ServiceAction  :5;
      UCHAR Reserved1  :3;
      UCHAR Type  :4;
      UCHAR Scope  :4;
      UCHAR ParameterList[];
    } PR_OUT;
  };
} PERSISTENT_RESERVE_COMMAND, *PPERSISTENT_RESERVE_COMMAND;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure.

</dd> <dt>

**PR\_IN**
</dt> <dd> <dl> <dt>

**ServiceAction**
</dt> <dd>

The service action code for this IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN request. PR\_IN.ServiceAction can be one of the following values: RESERVATION\_ACTION\_READ\_KEYS RESERVATION\_ACTION\_READ\_RESERVATIONS

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**AllocationLength**
</dt> <dd>

The number of bytes allocated for the returned parameter list.

</dd> </dl> </dd> <dt>

**PR\_OUT**
</dt> <dd> <dl> <dt>

**ServiceAction**
</dt> <dd>

The service action code for this IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT request. PR\_OUT.ServiceAction can be one of the following values: RESERVATION\_ACTION\_REGISTER RESERVATION\_ACTION\_RESERVE RESERVATION\_ACTION\_RELEASE RESERVATION\_ACTION\_CLEAR RESERVATION\_ACTION\_PREEMPT RESERVATION\_ACTION\_PREEMPT\_ABORT RESERVATION\_ACTION\_REGISTER\_IGNORE\_EXISTING

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**Type**
</dt> <dd>

A value that specifies the characteristics of the persistent reservation. PR\_OUT.Type can be one of the following values: RESERVATION\_TYPE\_WRITE\_EXCLUSIVE RESERVATION\_TYPE\_EXCLUSIVE RESERVATION\_TYPE\_WRITE\_EXCLUSIVE\_REGISTRANTS RESERVATION\_TYPE\_EXCLUSIVE\_REGISTRANTS

</dd> <dt>

**Scope**
</dt> <dd>

A value that specifies whether the persistent reservation applies to the entire logical unit or a specific element of the logical unit. PR\_OUT.Scope can be one of the following values: RESERVATION\_SCOPE\_LU RESERVATION\_SCOPE\_ELEMENT

</dd> <dt>

**ParameterList**
</dt> <dd>

The space for additional SCSI Persistent Reserve Out command parameters.

</dd> </dl> </dd> </dl>

## Remarks

The behavior of the storage device when a SCSI Persistent Reserve In command or a SCSI Persistent Reserve Out command is received is described in the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN**](ioctl-storage-persistent-reserve-in.md)
</dt> <dt>

[**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT**](ioctl-storage-persistent-reserve-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PERSISTENT_RESERVE_COMMAND%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






