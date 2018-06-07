---
title: GET\_BAND\_METADATA\_PARAMETERS structure
description: The metadata for a configured band is retrieved according to the parameters in a GET\_BAND\_METADATA\_PARAMETERS structure. This structure is input for an IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA request.
ms.assetid: CE8160C5-8C64-4BA5-864E-EC634754E062
keywords:
- GET_BAND_METADATA_PARAMETERS structure Storage Devices
- PGET_BAND_METADATA_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GET_BAND_METADATA_PARAMETERS
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

# GET\_BAND\_METADATA\_PARAMETERS structure

The metadata for a configured band is retrieved according to the parameters in a **GET\_BAND\_METADATA\_PARAMETERS** structure. This structure is input for an [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md) request.

## Syntax


```C++
typedef struct _GET_BAND_METADATA_PARAMETERS {
  ULONG         StructSize;
  ULONG         BandId;
  LARGE_INTEGER BandStart;
  ULONG         MetadataOffset;
                MetadataSize;
} GET_BAND_METADATA_PARAMETERS, *PGET_BAND_METADATA_PARAMETERS;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(GET\_BAND\_METADATA\_PARAMETERS).

</dd> <dt>

**BandId**
</dt> <dd>

The identifier of a single band to return information for. **BandSize** must be 0 when a single band is selected with **BandId.** To use **BandStart** and **BandSize** instead of **BandId** to select a band, set **BandId** = (ULONG)  1.

</dd> <dt>

**BandStart**
</dt> <dd>

The starting byte location on the storage device to begin a band search. An attempt is made to match a band at or after **BandStart**.

</dd> <dt>

**MetadataOffset**
</dt> <dd>

The offset from the start of the band metadata property to retrieve data from.

</dd> <dt>

**MetadataSize**
</dt> <dd>

The length of metadata bytes to retrieve.

</dd> </dl>

## Remarks

Precedence is given to **BandID** for band selection. If **BandID** is greater than 0 and **BandID** is less than the **MaxBandCount** member of [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md), then **BandID** is used as the only selection criteria for a band match. If **BandID** ==  1, then **BandStart** is used as the match criteria to select a band. If no band matches either selection criteria, then STATUS\_INVALID\_PARAMETER is returned in the *IoStatus* block for [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md).

If **BandID** and **BandStart** are both set to  1, then the [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md) returns metadata for the global band.

If [**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md) was successful, *Parameters.DeviceIoControl.InputBufferLength* equals the value in **MetadataSize**.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA**](ioctl-ehstor-bandmgmt-get-band-metadata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GET_BAND_METADATA_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






