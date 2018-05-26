---
title: IDE\_TASK\_FILE structure
description: The IDE\_TASK\_FILE structure contains the current and previous IDE task file.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: f18b46c0-975b-49ba-b398-45f2a44d6d3b
keywords:
- IDE_TASK_FILE structure Storage Devices
- PIDE_TASK_FILE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_TASK_FILE
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDE\_TASK\_FILE structure

The IDE\_TASK\_FILE structure contains the current and previous IDE task file.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_TASK_FILE {
  IDEREGISTERS Current;
  IDEREGISTERS Previous;
} IDE_TASK_FILE, *PIDE_TASK_FILE;
```



## Members

<dl> <dt>

**Current**
</dt> <dd>

Contains a structure of type [**IDEREGISTERS**](ideregisters.md) that holds the current contents of the ATA task file registers.

</dd> <dt>

**Previous**
</dt> <dd>

Contains a structure of type [**IDEREGISTERS**](ideregisters.md) that holds the previous contents of the ATA task file registers in the case of a 48-bit LBA command.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDEREGISTERS**](ideregisters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_TASK_FILE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






