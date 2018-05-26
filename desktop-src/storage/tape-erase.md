---
title: TAPE\_ERASE structure
description: The TAPE\_ERASE structure is used in conjunction with the IOCTL\_TAPE\_ERASE request to erase the current tape partition.
ms.assetid: 75ec5c40-1ac2-472a-9923-26018eb6267c
keywords:
- TAPE_ERASE structure Storage Devices
- PTAPE_ERASE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- TAPE_ERASE
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

# TAPE\_ERASE structure

The TAPE\_ERASE structure is used in conjunction with the [**IOCTL\_TAPE\_ERASE**](ioctl-tape-erase.md) request to erase the current tape partition.

## Syntax


```C++
typedef struct _TAPE_ERASE {
  ULONG   Type;
  BOOLEAN Immediate;
} TAPE_ERASE, *PTAPE_ERASE;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Indicates the type of erasure to perform. When this member is set to TAPE\_ERASE\_LONG, the tape partition is overwritten with a filler pattern. When it is set to TAPE\_ERASE\_SHORT, an end-of-recorded-data mark is written to the current position.

</dd> <dt>

**Immediate**
</dt> <dd>

Indicates that the target device should return status immediately, when set to **TRUE**. When this member is set to **FALSE**, the device should return status after the operation is complete.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_ERASE**](ioctl-tape-erase.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_ERASE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






