---
title: TAPE\_CREATE\_PARTITION structure
description: The TAPE\_CREATE\_PARTITION structure is used in conjunction with the IOCTL\_TAPE\_CREATE\_PARTITION request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media.
ms.assetid: 'da220281-a08d-4aeb-abb4-471aacb2461a'
keywords: ["TAPE_CREATE_PARTITION structure Storage Devices", "PTAPE_CREATE_PARTITION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_CREATE_PARTITION
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_CREATE\_PARTITION structure

The TAPE\_CREATE\_PARTITION structure is used in conjunction with the [**IOCTL\_TAPE\_CREATE\_PARTITION**](ioctl-tape-create-partition.md) request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media.

## Syntax


```C++
typedef struct _TAPE_CREATE_PARTITION {
  ULONG Method;
  ULONG Count;
  ULONG Size;
} TAPE_CREATE_PARTITION, *PTAPE_CREATE_PARTITION;
```



## Members

<dl> <dt>

**Method**
</dt> <dd>

Indicates the method used to create the partitions. This member can have one of the following values:



| Method                                 | Meaning                                                                                                                                                                                                                                                                                  |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TAPE\_FIXED\_PARTITIONS<br/>     | Partitions the tape based on the device's default definition of partitions. The **Count** and **Size** parameters are ignored. <br/>                                                                                                                                               |
| TAPE\_SELECT\_PARTITIONS<br/>    | Partitions the tape into the number of partitions specified by **Count**. The **Size** parameter is ignored. The size of the partitions is determined by the device's default partition size. For more specific information, refer to the documentation for your tape device.<br/> |
| TAPE\_INITIATOR\_PARTITIONS<br/> | Partitions the tape into the number and size of partitions specified by **Count** and **Size**, respectively, except for the last partition. The size of the last partition is the remainder of the tape. <br/>                                                                    |



 

</dd> <dt>

**Count**
</dt> <dd>

Indicates the number of partitions to create.

</dd> <dt>

**Size**
</dt> <dd>

Indicates the size of each partition, in bytes.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeMiniCreatePartition**](tapeminicreatepartition.md)
</dt> <dt>

[**IOCTL\_TAPE\_CREATE\_PARTITION**](ioctl-tape-create-partition.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_CREATE_PARTITION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






