---
title: STOR\_RICH\_DEVICE\_DESCRIPTION structure
description: The STOR\_RICH\_DEVICE\_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA (direct memory access) adapter.
ms.assetid: 765A420C-F406-4A46-BDCC-26A451549F8D
keywords:
- STOR_RICH_DEVICE_DESCRIPTION structure Storage Devices
- PSTOR_RICH_DEVICE_DESCRIPTION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_RICH_DEVICE_DESCRIPTION
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STOR\_RICH\_DEVICE\_DESCRIPTION structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **STOR\_RICH\_DEVICE\_DESCRIPTION** structure describes the attributes of the **physical device** for which a driver is requesting a DMA (direct memory access) adapter.

## Syntax


```C++
typedef struct _STOR_RICH_DEVICE_DESCRIPTION {
  ULONG Version;
  ULONG Size;
  Char  VendorId[STOR_VENDOR_ID_LENGTH +1];
  Char  ModelNumber[STOR_MODEL_NUMBER_LENGTH + 1];
  Char  FirmwareRevision[STOR_FIRMWARE_REVISION_LENGTH + 1];
} STOR_RICH_DEVICE_DESCRIPTION, *PSTOR_RICH_DEVICE_DESCRIPTION;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of the structure. Must be STOR\_RICH\_DEVICE\_DESCRIPTION\_STRUCTURE\_VERSION.

</dd> <dt>

**Size**
</dt> <dd>

The size of the structure.

</dd> <dt>

**VendorId**
</dt> <dd>

A string representing the device s vendor ID. May be an empty string if ModelNumber is provided.

</dd> <dt>

**ModelNumber**
</dt> <dd>

A string representing the device s model.

</dd> <dt>

**FirmwareRevision**
</dt> <dd>

A string representing the device s currently active firmware revision.

</dd> </dl>

## Remarks

Miniport can choose to support this UnitControl if the device reports longer Model or Firmware information than defined in SCSI.

This is invoked during the Unit enumeration process or the device description update process. ScsiUnitRichDescription is a caller-allocated version of this structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1607<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/>                   | <dl> <dt>Storport.h</dt> </dl> |



## See also

<dl> <dt>

[**HwStorUnitControl**](https://msdn.microsoft.com/library/windows/hardware/hh920398)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_RICH_DEVICE_DESCRIPTION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






