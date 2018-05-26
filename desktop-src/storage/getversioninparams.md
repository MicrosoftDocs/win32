---
title: GETVERSIONINPARAMS structure
description: The GETVERSIONINPARAMS structure is used in conjunction with the SMART\_GET\_VERSION request to retrieve version information, a capabilities mask, and a bitmask for the indicated device.
ms.assetid: dcbfa8d2-c2ea-43ae-9d77-ce95a430a514
keywords:
- GETVERSIONINPARAMS structure Storage Devices
- PGETVERSIONINPARAMS structure pointer Storage Devices
- LPGETVERSIONINPARAMS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GETVERSIONINPARAMS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GETVERSIONINPARAMS structure

The GETVERSIONINPARAMS structure is used in conjunction with the [**SMART\_GET\_VERSION**](smart-get-version.md) request to retrieve version information, a capabilities mask, and a bitmask for the indicated device.

## Syntax


```C++
typedef struct _GETVERSIONINPARAMS {
  UCHAR bVersion;
  UCHAR bRevision;
  UCHAR bReserved;
  UCHAR bIDEDeviceMap;
  ULONG fCapabilities;
  ULONG dwReserved[4];
} GETVERSIONINPARAMS, *PGETVERSIONINPARAMS, *LPGETVERSIONINPARAMS;
```



## Members

<dl> <dt>

**bVersion**
</dt> <dd>

Contains an integer that indicates the version number of the binary driver.

</dd> <dt>

**bRevision**
</dt> <dd>

Contains an integer that indicates the revision number of the binary driver.

</dd> <dt>

**bReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**bIDEDeviceMap**
</dt> <dd>

Contains the bitmap. The following table explains the meaning of the bitmap:



| Bitmap Flags                  | Meaning                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bit 0 is set to 1.<br/> | The device is either a SATA drive or an IDE drive. If it is an IDE drive, it is the master device on the primary channel. <br/> |
| Bit 1 is set to 1.<br/> | The device is an IDE drive, and it is the subordinate device on the primary channel. <br/>                                      |
| Bit 2 is set to 1.<br/> | The device is an IDE drive, and it is the master device on the secondary channel. <br/>                                         |
| Bit 3 is set to 1.<br/> | The device is an IDE drive, and it is the subordinate device on the secondary channel. <br/>                                    |
| Bit 4 is set to 1.<br/> | The device is an ATAPI drive, and it is the master device on the primary channel. <br/>                                         |
| Bit 5 is set to 1.<br/> | The device is an ATAPI drive, and it is the subordinate device on the primary channel. <br/>                                    |
| Bit 6 is set to 1.<br/> | The device is an ATAPI drive, and it is the master device on the secondary channel. <br/>                                       |
| Bit 7 is set to 1.<br/> | The device is an ATAPI drive, and it is the subordinate device on the secondary channel. <br/>                                  |



 

</dd> <dt>

**fCapabilities**
</dt> <dd>

Contains the bitmask of driver capabilities.



| Bitmask Flags                  | Meaning                                               |
|--------------------------------|-------------------------------------------------------|
| CAP\_ATA\_ID\_CMD<br/>   | The device supports the ATA ID command. <br/>   |
| CAP\_ATAPI\_ID\_CMD<br/> | The device supports the ATAPI ID command. <br/> |
| CAP\_SMART\_CMD<br/>     | The device supports SMART commands.<br/>        |



 

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**SMART\_GET\_VERSION**](smart-get-version.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GETVERSIONINPARAMS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






