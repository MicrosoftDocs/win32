---
title: TAPE\_GET\_MEDIA\_PARAMETERS structure
description: The TAPE\_GET\_MEDIA\_PARAMETERS structure is used in conjunction with the TapeMiniGetMediaParameters routine to retrieve tape media parameters.
ms.assetid: 3e12c431-4f6d-4d07-be52-e4809e8bc798
keywords:
- TAPE_GET_MEDIA_PARAMETERS structure Storage Devices
- PTAPE_GET_MEDIA_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- TAPE_GET_MEDIA_PARAMETERS
api_location:
- ntddtape.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TAPE\_GET\_MEDIA\_PARAMETERS structure

The TAPE\_GET\_MEDIA\_PARAMETERS structure is used in conjunction with the [**TapeMiniGetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567937) routine to retrieve tape media parameters.

## Syntax


```C++
typedef struct _TAPE_GET_MEDIA_PARAMETERS {
  LARGE_INTEGER Capacity;
  LARGE_INTEGER Remaining;
  ULONG         BlockSize;
  ULONG         PartitionCount;
  BOOLEAN       WriteProtected;
} TAPE_GET_MEDIA_PARAMETERS, *PTAPE_GET_MEDIA_PARAMETERS;
```



## Members

<dl> <dt>

**Capacity**
</dt> <dd>

Indicates the total number of bytes of user data the tape can hold.

</dd> <dt>

**Remaining**
</dt> <dd>

Indicates the number of bytes from the current position to the end of the tape.

</dd> <dt>

**BlockSize**
</dt> <dd>

Indicates the block size, in bytes, or zero if the drive is using variable block size.

</dd> <dt>

**PartitionCount**
</dt> <dd>

Indicates the number of partitions on the tape. If the tape is not partitioned, **PartitionCount** is 1.

</dd> <dt>

**WriteProtected**
</dt> <dd>

Is set to **TRUE** if the tape is write-protected.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeMiniGetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567937)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_GET_MEDIA_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






