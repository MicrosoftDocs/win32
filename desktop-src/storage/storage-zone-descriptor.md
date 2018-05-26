---
title: STORAGE\_ZONE\_DESCRIPTOR structure
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: 33AE6D40-F54D-427D-B811-2188EA623A26
keywords:
- STORAGE_ZONE_DESCRIPTOR structure Storage Devices
- PSTORAGE_ZONE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_ZONE_DESCRIPTOR
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

# STORAGE\_ZONE\_DESCRIPTOR structure

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef struct _STORAGE_ZONE_DESCRIPTOR {
  ULONG                  Size;
  STORAGE_ZONE_TYPES     ZoneType;
  STORAGE_ZONE_CONDITION ResetWritePointerRecomend;
  BOOLEAN                ResetWritePointerRecomend;
                         Reserved0[3];
  ULONGLONG              ZoneSize;
  ULONGLONG              WriterPointerOffset;
} STORAGE_ZONE_DESCRIPTOR, *PSTORAGE_ZONE_DESCRIPTOR;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

N/A

</dd> <dt>

**ZoneType**
</dt> <dd>

N/A

</dd> <dt>

**ResetWritePointerRecomend**
</dt> <dd>

N/A

</dd> <dt>

**ResetWritePointerRecomend**
</dt> <dd>

N/A

</dd> <dt>

**Reserved0**
</dt> <dd>

N/A

</dd> <dt>

**ZoneSize**
</dt> <dd>

N/A

</dd> <dt>

**WriterPointerOffset**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ZONE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





