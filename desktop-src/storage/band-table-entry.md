---
title: BAND\_TABLE\_ENTRY structure
description: Banding information entries in BAND\_TABLE are represented as BAND\_TABLE\_ENTRY structures. These entries contain location and security properties for a band configuration.
ms.assetid: 6956327E-5407-4771-9BB9-F59D752A5410
keywords:
- BAND_TABLE_ENTRY structure Storage Devices
- PBAND_TABLE_ENTRY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- BAND_TABLE_ENTRY
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

# BAND\_TABLE\_ENTRY structure

Banding information entries in [**BAND\_TABLE**](band-table.md) are represented as **BAND\_TABLE\_ENTRY** structures. These entries contain location and security properties for a band configuration.

## Syntax


```C++
typedef struct _BAND_TABLE_ENTRY {
  ULONG              BandId;
  BAND_LOCATION_INFO LocationInfo;
  BAND_SECURITY_INFO SecurityInfo;
} BAND_TABLE_ENTRY, *PBAND_TABLE_ENTRY;
```



## Members

<dl> <dt>

**BandId**
</dt> <dd>

The band identifier for a configured band on a storage device.

</dd> <dt>

**LocationInfo**
</dt> <dd>

The band location information.

</dd> <dt>

**SecurityInfo**
</dt> <dd>

The band security information. This includes encryption algorithm information when selected in [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md).

</dd> </dl>

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_LOCATION\_INFO**](band-location-info.md)
</dt> <dt>

[**BAND\_SECURITY\_INFO**](band-security-info.md)
</dt> <dt>

[**BAND\_TABLE**](band-table.md)
</dt> <dt>

[**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BAND_TABLE_ENTRY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






