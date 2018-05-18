---
title: DEVICE\_COPY\_OFFLOAD\_DESCRIPTOR structure
description: Used in conjunction with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to describe the copy offload capabilities of a storage device.
ms.assetid: '192684D1-3D01-4EAA-989F-2E21E7187B3B'
keywords: ["DEVICE_COPY_OFFLOAD_DESCRIPTOR structure Storage Devices", "PDEVICE_COPY_OFFLOAD_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DEVICE_COPY_OFFLOAD_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# DEVICE\_COPY\_OFFLOAD\_DESCRIPTOR structure

Used in conjunction with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to describe the copy offload capabilities of a storage device.

## Syntax


```C++
typedef struct _DEVICE_COPY_OFFLOAD_DESCRIPTOR {
  ULONG      Version;
  ULONG      Size;
  ULONG      MaximumTokenLifetime;
  ULONG      DefaultTokenLifetime;
  ULONGULONG MaximumTransferSize;
  ULONGULONG OptimalTransferCount;
  ULONG      MaximumDataDescriptors;
  ULONG      MaximumTransferLengthPerDescriptor;
  ULONG      OptimalTransferLengthPerDescriptor;
  USHORT     OptimalTransferLengthGranularity;
  UCHAR      Reserved[2];
} DEVICE_COPY_OFFLOAD_DESCRIPTOR, *PDEVICE_COPY_OFFLOAD_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**MaximumTokenLifetime**
</dt> <dd>

The maximum lifetime of the token, in seconds.

</dd> <dt>

**DefaultTokenLifetime**
</dt> <dd>

The default lifetime of the token, in seconds.

</dd> <dt>

**MaximumTransferSize**
</dt> <dd>

The maximum transfer size, in bytes.

</dd> <dt>

**OptimalTransferCount**
</dt> <dd>

The optimal transfer size, in bytes.

</dd> <dt>

**MaximumDataDescriptors**
</dt> <dd>

The maximum number of data descriptors.

</dd> <dt>

**MaximumTransferLengthPerDescriptor**
</dt> <dd>

The maximum transfer length, in blocks, per descriptor.

</dd> <dt>

**OptimalTransferLengthPerDescriptor**
</dt> <dd>

The optimal transfer length, in blocks, per descriptor.

</dd> <dt>

**OptimalTransferLengthGranularity**
</dt> <dd>

The granularity of the optimal transfer length, in blocks. Transfer lengths that are not an even multiple of this length may be delayed.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_COPY_OFFLOAD_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






