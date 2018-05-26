---
title: IDENTIFY\_DEVICE\_DATA\_LOG\_PAGE\_ZONED\_DEVICE\_INFO structure
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: 2F0B6C1F-54CC-47CF-B0D0-A53FAB80AF91
keywords:
- IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO structure Storage Devices
- PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO
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

# IDENTIFY\_DEVICE\_DATA\_LOG\_PAGE\_ZONED\_DEVICE\_INFO structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef struct _IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO {
  IDENTIFY_DEVICE_DATA_LOG_PAGE_HEADER Header;
  struct {
    ULONGLONG URSWRZ  :1;
    ULONGLONG Reserved  :62;
    ULONGLONG Valid  :1;
  } ZonedDeviceCapabilities;
  struct {
    ULONGLONG Reserved  :63;
    ULONGLONG Valid  :1;
  } ZonedDeviceSettings;
  struct {
    ULONGLONG Number  :32;
    ULONGLONG Reserved  :31;
    ULONGLONG Valid  :1;
  } OptimalNumberOfOpenSequentialWritePreferredZones;
  struct {
    ULONGLONG Number  :32;
    ULONGLONG Reserved  :31;
    ULONGLONG Valid  :1;
  } OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZones;
  struct {
    ULONGLONG Number  :32;
    ULONGLONG Reserved  :31;
    ULONGLONG Valid  :1;
  } MaxNumberOfOpenSequentialWriteRequiredZones;
  struct {
    ULONGLONG ZacMinorVersion  :16;
    ULONGLONG Reserved0  :47;
    ULONGLONG Valid  :1;
  } Version;
  UCHAR                                Reserved[456];
} IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO, *PIDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

N/A

</dd> <dt>

**ZonedDeviceCapabilities**
</dt> <dd> <dl> <dt>

**URSWRZ**
</dt> <dd>

N/A

</dd> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**ZonedDeviceSettings**
</dt> <dd> <dl> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**OptimalNumberOfOpenSequentialWritePreferredZones**
</dt> <dd> <dl> <dt>

**Number**
</dt> <dd>

N/A

</dd> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZones**
</dt> <dd> <dl> <dt>

**Number**
</dt> <dd>

N/A

</dd> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**MaxNumberOfOpenSequentialWriteRequiredZones**
</dt> <dd> <dl> <dt>

**Number**
</dt> <dd>

N/A

</dd> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

**ZacMinorVersion**
</dt> <dd>

N/A

</dd> <dt>

**Reserved0**
</dt> <dd>

N/A

</dd> <dt>

**Valid**
</dt> <dd>

N/A

</dd> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                  |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ata.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDENTIFY_DEVICE_DATA_LOG_PAGE_ZONED_DEVICE_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





