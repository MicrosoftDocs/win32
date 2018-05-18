---
title: DISK\_SIGNATURE structure
description: DISK\_SIGNATURE contains the disk signature information for a disk's partition table.
ms.assetid: 'f3fdb436-53b6-4fb3-8746-1f852f7d928a'
keywords: ["DISK_SIGNATURE structure Storage Devices", "PDISK_SIGNATURE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_SIGNATURE
api_location:
- ntddk.h
api_type:
- HeaderDef
---

# DISK\_SIGNATURE structure

DISK\_SIGNATURE contains the disk signature information for a disk's partition table.

## Syntax


```C++
typedef struct _DISK_SIGNATURE {
  ULONG PartitionStyle;
  union {
    struct {
      ULONG Signature;
      ULONG CheckSum;
    } Mbr;
    struct {
      GUID DiskId;
    } Gpt;
  };
} DISK_SIGNATURE, *PDISK_SIGNATURE;
```



## Members

<dl> <dt>

**PartitionStyle**
</dt> <dd>

Specifies the type of partition. See [**PARTITION\_STYLE**](partition-style.md) for a description of the possible values.

</dd> <dt>

**Mbr**
</dt> <dd> <dl> <dt>

**Signature**
</dt> <dd>

Specifies the signature value, which uniquely identifies the disk. The **Mbr** member of the union is used to specify the disk signature data for a disk formatted with a Master Boot Record (MBR) format partition table. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_MBR.

</dd> <dt>

**CheckSum**
</dt> <dd>

Specifies the checksum for the master boot record. The **Mbr** member of the union is used to specify the disk signature data for a disk formatted with a Master Boot Record (MBR) format partition table. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_MBR.

</dd> </dl> </dd> <dt>

**Gpt**
</dt> <dd> <dl> <dt>

**DiskId**
</dt> <dd>

Specifies the GUID that uniquely identifies the disk. The **Gpt** member of the union is used to specify the disk signature data for a disk that is formatted with a GUID Partition Table (GPT) format partition table. The GUID data type is described on the [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392) reference page. This member is valid when **PartitionStyle** is PARTITION\_STYLE\_GPT.

</dd> </dl> </dd> </dl>

## Remarks

## Requirements



|                    |                                                                                                      |
|--------------------|------------------------------------------------------------------------------------------------------|
| Version<br/> | This structure is only available on Windows XP and later.<br/>                                 |
| Header<br/>  | <dl> <dt>Ntddk.h (include Ntddk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoReadDiskSignature**](ioreaddisksignature.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_SIGNATURE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






