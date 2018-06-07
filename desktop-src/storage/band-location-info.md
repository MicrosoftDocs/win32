---
title: BAND\_LOCATION\_INFO structure
description: The BAND\_LOCATION\_INFO structure specifies the location information for a band table entry query.
ms.assetid: A9E28600-45B2-4082-917F-29B3237DEC84
keywords:
- BAND_LOCATION_INFO structure Storage Devices
- PBAND_LOCATION_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- BAND_LOCATION_INFO
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BAND\_LOCATION\_INFO structure

The **BAND\_LOCATION\_INFO** structure specifies the location information for a band table entry query.

## Syntax


```C++
typedef struct _BAND_LOCATION_INFO {
  ULONG         StructSize;
  ULONG         Reserved;
  LARGE_INTEGER BandStart;
  LARGE_INTEGER BandSize;
  BYTE          Metadata[32];
} BAND_LOCATION_INFO, *PBAND_LOCATION_INFO;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of the structure in bytes. Set to **sizeof**(BAND\_LOCATION\_INFO).

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**BandStart**
</dt> <dd>

The offset in bytes of this band location on the storage device. This value is always 0 for the global band.

</dd> <dt>

**BandSize**
</dt> <dd>

The size in bytes of the band configured at this location. This value is set to the maximum size possible for the global band.

</dd> <dt>

**Metadata**
</dt> <dd>

A metadata field used as a data area for a band management application.

</dd> </dl>

## Remarks

**BandStart** and **BandSize** must be a multiple of the sector size of the underlying storage device.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_TABLE\_ENTRY**](band-table-entry.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BAND_LOCATION_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






