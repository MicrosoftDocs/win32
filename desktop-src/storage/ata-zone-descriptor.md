---
title: ATA\_ZONE\_DESCRIPTOR structure
description: This structure is for internal use only and should not be called from your code.
ms.assetid: 2e027ac5-7b5d-43cc-8d37-c0a3e77e68c9
keywords:
- ATA_ZONE_DESCRIPTOR structure Storage Devices
- PATA_ZONE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ATA_ZONE_DESCRIPTOR
api_location:
- Ata.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ATA\_ZONE\_DESCRIPTOR structure

This structure is for internal use only and should not be called from your code.

## Syntax


```C++
typedef struct _ATA_ZONE_DESCRIPTOR {
  UCHAR     ZoneType  : 4;
  UCHAR     Reserved0  : 4;
  UCHAR     Reset  : 1;
  UCHAR     NonSeq : 1;
  UCHAR     Reserved1  : 2;
  UCHAR     ZoneCondition  : 4;
  UCHAR     Reserved2[6];
  ULONGLONG ZoneLength  : 48;
  ULONGLONG Reserved3  : 16;
  ULONGLONG ZoneStartLBA  : 48;
  ULONGLONG Reserved4  : 16;
  ULONGLONG WritePointerLBA  : 48;
  ULONGLONG Reserved5  : 16;
  UCHAR     Reserved6[32];
} ATA_ZONE_DESCRIPTOR, *PATA_ZONE_DESCRIPTOR;
```



## Members

<dl> <dt>

**ZoneType : 4**
</dt> <dd>

N/A

</dd> <dt>

**Reserved0 : 4**
</dt> <dd>

N/A

</dd> <dt>

**Reset : 1**
</dt> <dd>

N/A

</dd> <dt>

**NonSeq : 1**
</dt> <dd>

N/A

</dd> <dt>

**Reserved1 : 2**
</dt> <dd>

N/A

</dd> <dt>

**ZoneCondition : 4**
</dt> <dd>

N/A

</dd> <dt>

**Reserved2**
</dt> <dd>

N/A

</dd> <dt>

**ZoneLength : 48**
</dt> <dd>

N/A

</dd> <dt>

**Reserved3 : 16**
</dt> <dd>

N/A

N/A

</dd> <dt>

**ZoneStartLBA : 48**
</dt> <dd>

N/A

</dd> <dt>

**Reserved4 : 16**
</dt> <dd>

N/A

</dd> <dt>

**WritePointerLBA : 48**
</dt> <dd>

N/A

</dd> <dt>

**Reserved5 : 16**
</dt> <dd>

N/A

</dd> <dt>

**Reserved6**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                  |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ata.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA_ZONE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





