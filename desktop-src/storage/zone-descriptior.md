---
title: ZONE\_DESCRIPTIOR structure
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: 8326f683-3952-486e-b322-80ce96759366
keywords:
- ZONE_DESCRIPTIOR structure Storage Devices
- PZONE_DESCRIPTIOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ZONE_DESCRIPTIOR
api_location:
- scsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ZONE\_DESCRIPTIOR structure

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef struct _ZONE_DESCRIPTIOR {
  UCHAR      ZoneType  :4;
  UCHAR      Reserved1  :4;
  UCHAR  : 1 Reset  :1;
  UCHAR      Non_Seq  :1;
  UCHAR      Reserved2  :2;
  UCHAR      ZoneCondition  :4;
  UCHAR      Reserved3[6];
  UCHAR      ZoneLength[8];
  UCHAR      ZoneStartLBA[8];
  UCHAR      WritePointerLBA[8];
  UCHAR      Reserved4[32];
} ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR;
```



## Members

<dl> <dt>

**ZoneType**
</dt> <dd>

N/A

</dd> <dt>

**Reserved1**
</dt> <dd>

N/A

</dd> <dt>

**Reset**
</dt> <dd>

N/A

</dd> <dt>

**Non\_Seq**
</dt> <dd>

N/A

</dd> <dt>

**Reserved2**
</dt> <dd>

N/A

</dd> <dt>

**ZoneCondition**
</dt> <dd>

N/A

</dd> <dt>

**Reserved3**
</dt> <dd>

N/A

</dd> <dt>

**ZoneLength**
</dt> <dd>

N/A

</dd> <dt>

**ZoneStartLBA**
</dt> <dd>

N/A

</dd> <dt>

**WritePointerLBA**
</dt> <dd>

N/A

</dd> <dt>

**Reserved4**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsi.h (include Minitape.h or Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ZONE_DESCRIPTIOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





