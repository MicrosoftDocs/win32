---
title: ENUMERATE\_BANDS\_PARAMETERS structure
description: The ENUMERATE\_BANDS\_PARAMETERS structure is used to select which band information entries are selected for return from an IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS request.
ms.assetid: A493EF45-AA62-43FE-8E19-613B66FA0D83
keywords:
- ENUMERATE_BANDS_PARAMETERS structure Storage Devices
- PENUMERATE_BANDS_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ENUMERATE_BANDS_PARAMETERS
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ENUMERATE\_BANDS\_PARAMETERS structure

The **ENUMERATE\_BANDS\_PARAMETERS** structure is used to select which band information entries are selected for return from an [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request.

## Syntax


```C++
typedef struct _ENUMERATE_BANDS_PARAMETERS {
  ULONG         StructSize;
  ULONG         Flags;
  ULONG         Reserved;
  ULONG         BandId;
  LARGE_INTEGER BandStart;
  LARGE_INTEGER BandSize;
} ENUMERATE_BANDS_PARAMETERS, *PENUMERATE_BANDS_PARAMETERS;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(ENUMERATE\_BANDS\_PARAMETERS).

</dd> <dt>

**Flags**
</dt> <dd>

Band enumeration flags. This value is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                        | Meaning                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ENUMBANDS_ENUM_ALL_BANDS"></span><span id="enumbands_enum_all_bands"></span><dl> <dt>**ENUMBANDS\_ENUM\_ALL\_BANDS**</dt> </dl>             | All bands are returned. When this flag is set, the **BandId**, **BandStart**, and **BandSize** members are ignored.<br/>              |
| <span id="ENUMBANDS_REPORT_CRYPTO_ALGO"></span><span id="enumbands_report_crypto_algo"></span><dl> <dt>**ENUMBANDS\_REPORT\_CRYPTO\_ALGO**</dt> </dl> | Include media encryption algorithm information in the **SecurityInfo** member of [**BAND\_TABLE\_ENTRY**](band-table-entry.md).<br/> |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**BandId**
</dt> <dd>

The identifier of a single band to return information for. **BandSize** must be 0 when a single band is selected with **BandId.** To use **BandStart** and **BandSize** instead of **BandId** to select a band, set **BandId** = (ULONG)  1.

</dd> <dt>

**BandStart**
</dt> <dd>

The starting byte location on the storage device to begin a band search. An attempt is made to match a band at or after **BandStart**.

</dd> <dt>

**BandSize**
</dt> <dd>

An optional band size match value in bytes. If **BandSize** == 0 and **BandId** ==  1, then **BandStart** is the only match value for selecting a band. Otherwise, a band at or after **BandStart** and matching **BandSize** exactly is selected.

</dd> </dl>

## Remarks

When **ENUMBANDS\_ENUM\_ALL\_BANDS** is not set in **Flags**, a selection attempt is made to match a single band. A single band match is made based on the values in **BandID**, **BandStart**, and **BandSize**. Precedence is given to **BandID** for band selection. If **BandID** &gt; 0 and **BandID** &lt; **MaxBandCount** member of [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) If **BandID** is greater than 0 and **BandID** is less than the **MaxBandCount** member of **BAND\_MANAGEMENT\_CAPABILITIES**, then **BandID** is used as the only selection criteria for a band match. If **BandID** ==  1, then **BandStart** and **BandSize** are used as match criteria to select a band.

When **BandStart** and **BandSize** are used to match a band, the first band configured at or after the **BandStart** location having the exact size of **BandSize** is returned. If **BandSize** == 0, when **BandStart** is valid, then the first band configured at or after **BandStart** is returned.

If **BandID** == 0 or no bands are configured and **Flags** is not set to ENUMBANDS\_ENUM\_ALL\_BANDS, then the global band for the entire device is returned.

**BandStart** and **BandSize** are not valid unless their values, in bytes, are exact multiples of the sector size of the underlying storage device.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)
</dt> <dt>

[**BAND\_TABLE**](band-table.md)
</dt> <dt>

[**BAND\_TABLE\_ENTRY**](band-table-entry.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ENUMERATE_BANDS_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






