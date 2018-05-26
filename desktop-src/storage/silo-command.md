---
title: SILO\_COMMAND structure
description: This structure describes a storage silo driver command.
ms.assetid: 3258FA16-E1FE-4CBF-8C87-0C7A8B2A7EBF
keywords:
- SILO_COMMAND structure Storage Devices
- PSILO_COMMAND structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SILO_COMMAND
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SILO\_COMMAND structure

This structure describes a storage silo driver command.

## Syntax


```C++
typedef struct tagSILO_COMMAND {
  UCHAR SiloIndex;
  UCHAR Command;
  ULONG cbCommandBuffer;
  UCHAR rgbCommandBuffer[ANYSIZE_ARRAY];
} SILO_COMMAND, *PSILO_COMMAND;
```



## Members

<dl> <dt>

**SiloIndex**
</dt> <dd></dd> <dt>

**Command**
</dt> <dd>

This member contains the 1667 command value.

</dd> <dt>

**cbCommandBuffer**
</dt> <dd>

This member contains the size of the 1667 command buffer.

</dd> <dt>

**rgbCommandBuffer**
</dt> <dd></dd> </dl>

## Remarks

Together, **cbCommandBufferSize** and **rgbCommandBuffer** members indicate the raw data payload for the silo command, and are sent as-is to the device. The structure of the data in this buffer is silo-dependent. The structure is assumed to be shared knowledge between the client issuing this IOCTL and the device firmware implementation of this particular silo.

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SILO_COMMAND%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





